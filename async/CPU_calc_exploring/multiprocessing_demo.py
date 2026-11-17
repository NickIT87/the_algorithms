
"""
MULTIPROCESSING DEMO
====================

Демонстрация основных возможностей multiprocessing в Python.

Совместимость:
- macOS (Apple Silicon M1/M2/M3/M4)
- Windows
- Linux

Зависимости: только стандартная библиотека Python.

Запуск:
    python3 multiprocessing_demo.py

Рекомендуется Python 3.10+.
"""

import multiprocessing as mp
from multiprocessing import shared_memory
import os
import time
import random
import traceback
from concurrent.futures import ProcessPoolExecutor


# ============================================================
# 1. ОБЩИЕ WORKER-ФУНКЦИИ
# ============================================================

def simple_worker(number):
    """Простейший независимый процесс."""
    print(
        f"[Process] PID={os.getpid()}, "
        f"number={number}"
    )
    time.sleep(1)
    return number * number


def calculate_square(number):
    """Вычисление квадрата числа."""
    return number * number


def calculate_sum(numbers):
    """Подсчёт суммы переданного списка."""
    return sum(numbers)


def slow_calculation(number):
    """Искусственная CPU-нагрузка."""
    result = 0

    for i in range(number):
        result += i * i

    return result


# ============================================================
# 2. PROCESS: СОЗДАНИЕ И УПРАВЛЕНИЕ ПРОЦЕССАМИ
# ============================================================

def demo_process():

    print("\n=== 1. PROCESS ===")

    processes = []

    for i in range(4):

        process = mp.Process(
            target=simple_worker,
            args=(i,),
            name=f"Worker-{i}"
        )

        processes.append(process)
        process.start()

    for process in processes:
        process.join()

        print(
            f"{process.name}: "
            f"PID={process.pid}, "
            f"exitcode={process.exitcode}, "
            f"alive={process.is_alive()}"
        )


# ============================================================
# 3. POOL: ПУЛ ПРОЦЕССОВ
# ============================================================

def demo_pool():

    print("\n=== 2. POOL ===")

    numbers = list(range(20))

    workers = min(4, os.cpu_count() or 1)

    with mp.Pool(processes=workers) as pool:

        # map: результаты в исходном порядке
        results = pool.map(
            calculate_square,
            numbers
        )

        print("map:", results)

        # imap: постепенное получение результатов
        print("imap:")

        for result in pool.imap(
            calculate_square,
            numbers
        ):
            print(result, end=" ")

        print()

        # imap_unordered: по мере готовности
        print("imap_unordered:")

        for result in pool.imap_unordered(
            slow_calculation,
            [100_000] * 8,
            chunksize=1
        ):
            print(result, end=" ")

        print()

        # apply_async: отдельная асинхронная задача
        async_result = pool.apply_async(
            calculate_square,
            (25,)
        )

        print("apply_async:", async_result.get())


# ============================================================
# 4. QUEUE: ОБМЕН СООБЩЕНИЯМИ
# ============================================================

def queue_worker(queue, number):

    result = number * number

    queue.put({
        "pid": os.getpid(),
        "number": number,
        "result": result
    })


def demo_queue():

    print("\n=== 3. QUEUE ===")

    queue = mp.Queue()
    processes = []

    for i in range(5):

        process = mp.Process(
            target=queue_worker,
            args=(queue, i)
        )

        processes.append(process)
        process.start()

    results = [
        queue.get()
        for _ in processes
    ]

    for process in processes:
        process.join()

    for result in results:
        print(result)

    queue.close()
    queue.join_thread()


# ============================================================
# 5. PIPE: ПРЯМОЙ КАНАЛ СВЯЗИ
# ============================================================

def pipe_worker(connection):

    connection.send({
        "message": "Hello from child process",
        "pid": os.getpid()
    })

    connection.close()


def demo_pipe():

    print("\n=== 4. PIPE ===")

    parent_conn, child_conn = mp.Pipe()

    process = mp.Process(
        target=pipe_worker,
        args=(child_conn,)
    )

    process.start()

    child_conn.close()

    message = parent_conn.recv()

    print("Received:", message)

    parent_conn.close()
    process.join()


# ============================================================
# 6. VALUE И ARRAY: ОБЩАЯ ПАМЯТЬ
# ============================================================

def shared_counter_worker(counter, array, lock):

    with lock:

        counter.value += 1

        for i in range(len(array)):
            array[i] += 1


def demo_shared_value_array():

    print("\n=== 5. SHARED VALUE / ARRAY ===")

    counter = mp.Value("i", 0)

    array = mp.Array("i", [0] * 5)

    lock = mp.Lock()

    processes = []

    for _ in range(4):

        process = mp.Process(
            target=shared_counter_worker,
            args=(counter, array, lock)
        )

        processes.append(process)
        process.start()

    for process in processes:
        process.join()

    print("Counter:", counter.value)
    print("Array:", list(array))


# ============================================================
# 7. SHARED MEMORY
# ============================================================

def shared_memory_worker(
    shm_name,
    size,
    start,
    end
):

    import struct

    shm = shared_memory.SharedMemory(
        name=shm_name
    )

    try:

        for i in range(start, end):

            value = struct.unpack_from(
                "q",
                shm.buf,
                i * 8
            )[0]

            struct.pack_into(
                "q",
                shm.buf,
                i * 8,
                value * 2
            )

    finally:
        shm.close()


def demo_shared_memory():

    print("\n=== 6. SHARED MEMORY ===")

    size = 100

    shm = shared_memory.SharedMemory(
        create=True,
        size=size * 8
    )

    try:

        import struct

        # Заполняем общую память
        for i in range(size):
            struct.pack_into(
                "q",
                shm.buf,
                i * 8,
                i
            )

        workers = 4
        chunk = size // workers

        processes = []

        for i in range(workers):

            start = i * chunk

            end = (
                start + chunk
                if i < workers - 1
                else size
            )

            process = mp.Process(
                target=shared_memory_worker,
                args=(
                    shm.name,
                    size,
                    start,
                    end
                )
            )

            processes.append(process)
            process.start()

        for process in processes:
            process.join()

            if process.exitcode != 0:
                raise RuntimeError(
                    f"Worker failed: {process.pid}"
                )

        results = [
            struct.unpack_from(
                "q",
                shm.buf,
                i * 8
            )[0]
            for i in range(size)
        ]

        print("First 20 values:", results[:20])

    finally:

        shm.close()
        shm.unlink()


# ============================================================
# 8. LOCK: СИНХРОНИЗАЦИЯ
# ============================================================

def lock_worker(counter, lock):

    for _ in range(1000):

        with lock:
            counter.value += 1


def demo_lock():

    print("\n=== 7. LOCK ===")

    counter = mp.Value("i", 0)

    lock = mp.Lock()

    processes = []

    for _ in range(4):

        process = mp.Process(
            target=lock_worker,
            args=(counter, lock)
        )

        processes.append(process)
        process.start()

    for process in processes:
        process.join()

    print("Expected: 4000")
    print("Actual:", counter.value)


# ============================================================
# 9. EVENT: СИГНАЛ МЕЖДУ ПРОЦЕССАМИ
# ============================================================

def event_worker(event):

    print("Worker waiting for event...")

    event.wait()

    print("Event received!")


def demo_event():

    print("\n=== 8. EVENT ===")

    event = mp.Event()

    process = mp.Process(
        target=event_worker,
        args=(event,)
    )

    process.start()

    time.sleep(2)

    print("Sending event...")

    event.set()

    process.join()


# ============================================================
# 10. SEMAPHORE: ОГРАНИЧЕНИЕ ПАРАЛЛЕЛЬНОСТИ
# ============================================================

def semaphore_worker(semaphore, number):

    with semaphore:

        print(
            f"Worker {number} entered, "
            f"PID={os.getpid()}"
        )

        time.sleep(2)

        print(f"Worker {number} finished")


def demo_semaphore():

    print("\n=== 9. SEMAPHORE ===")

    # Максимум два одновременно работающих процесса
    semaphore = mp.Semaphore(2)

    processes = []

    for i in range(6):

        process = mp.Process(
            target=semaphore_worker,
            args=(semaphore, i)
        )

        processes.append(process)
        process.start()

    for process in processes:
        process.join()


# ============================================================
# 11. BARRIER: СИНХРОНИЗАЦИЯ ГРУППЫ
# ============================================================

def barrier_worker(barrier, number):

    print(f"Worker {number} before barrier")

    barrier.wait()

    print(f"Worker {number} after barrier")


def demo_barrier():

    print("\n=== 10. BARRIER ===")

    workers = 4

    barrier = mp.Barrier(workers)

    processes = []

    for i in range(workers):

        process = mp.Process(
            target=barrier_worker,
            args=(barrier, i)
        )

        processes.append(process)
        process.start()

    for process in processes:
        process.join()


# ============================================================
# 12. PROCESS POOL EXECUTOR
# ============================================================

def demo_executor():

    print("\n=== 11. PROCESS POOL EXECUTOR ===")

    workers = min(4, os.cpu_count() or 1)

    tasks = list(range(20))

    with ProcessPoolExecutor(
        max_workers=workers
    ) as executor:

        results = list(
            executor.map(
                calculate_square,
                tasks
            )
        )

    print("Workers:", workers)
    print("Results:", results)


# ============================================================
# 13. BENCHMARK
# ============================================================

def benchmark():

    print("\n=== 12. BENCHMARK ===")

    tasks = [2_000_000] * 8

    for workers in [1, 2, 4, 6, 8]:

        start = time.perf_counter()

        with ProcessPoolExecutor(
            max_workers=workers
        ) as executor:

            results = list(
                executor.map(
                    slow_calculation,
                    tasks
                )
            )

        elapsed = time.perf_counter() - start

        print(
            f"Workers={workers:2d} | "
            f"Time={elapsed:.3f} sec | "
            f"Tasks={len(results)}"
        )


# ============================================================
# 14. ИНФОРМАЦИЯ О СИСТЕМЕ
# ============================================================

def system_info():

    print("\n=== SYSTEM INFO ===")

    print("Python:", os.sys.version)

    print("PID:", os.getpid())

    print("CPU count:", os.cpu_count())

    print("Start method:", mp.get_start_method())


# ============================================================
# MAIN
# ============================================================

DEMOS = [
    ("Process", demo_process),
    ("Pool", demo_pool),
    ("Queue", demo_queue),
    ("Pipe", demo_pipe),
    ("Shared Value / Array", demo_shared_value_array),
    ("Shared Memory", demo_shared_memory),
    ("Lock", demo_lock),
    ("Event", demo_event),
    ("Semaphore", demo_semaphore),
    ("Barrier", demo_barrier),
    ("ProcessPoolExecutor", demo_executor),
    ("Benchmark", benchmark),
]


def main():

    system_info()

    print("\nMULTIPROCESSING LABORATORY")

    print("0 - Run all demonstrations")

    for index, (name, _) in enumerate(DEMOS, 1):
        print(f"{index} - {name}")

    try:

        choice = input("\nSelect demo: ").strip()

        if choice == "0":

            for name, function in DEMOS:

                print(f"\n\n{'=' * 60}")
                print(f"RUNNING: {name}")
                print("=" * 60)

                function()

        elif choice.isdigit():

            index = int(choice)

            if 1 <= index <= len(DEMOS):

                name, function = DEMOS[index - 1]

                print(f"\nRunning: {name}")

                function()

            else:
                print("Invalid selection")

        else:
            print("Invalid selection")

    except KeyboardInterrupt:

        print("\nInterrupted by user")

    except Exception:

        print("\nError:")
        traceback.print_exc()

    print("\nLaboratory finished")


if __name__ == "__main__":

    # Явно используем spawn для демонстрации
    # поведения macOS и Apple Silicon.
    mp.freeze_support()

    main()
