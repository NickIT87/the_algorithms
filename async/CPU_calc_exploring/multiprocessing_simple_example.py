import multiprocessing
import os
import time

def worker(number):
    print(f"Процесс {number}, PID: {os.getpid()}")
    time.sleep(2)
    return number * number

if __name__ == "__main__":
    processes = []

    for i in range(4):
        p = multiprocessing.Process(
            target=worker,
            args=(i,)
        )
        processes.append(p)
        p.start()

    for p in processes:
        p.join()

    print("Все процессы завершены")