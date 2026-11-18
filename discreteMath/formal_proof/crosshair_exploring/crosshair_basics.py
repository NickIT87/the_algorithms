
"""
CROSSHAIR BASICS
================

Учебные примеры формальной проверки Python-программ.

Установка:
    pip install crosshair-tool

Запуск:
    crosshair check crosshair_basics.py

Обозначения:
    pre  - предусловие (Precondition)
    post - постусловие (Postcondition)

CrossHair будет искать входные значения,
при которых нарушаются математические условия.
"""


# ============================================================
# 1. ABSOLUTE VALUE — абсолютное значение
# ============================================================

def absolute(x: int) -> int:
    """
    Абсолютное значение числа.

    post: __return__ >= 0
    post: __return__ == x or __return__ == -x
    """
    if x >= 0:
        return x
    return -x


# ============================================================
# 2. ADDITION — сложение
# ============================================================

def add(a: int, b: int) -> int:
    """
    Проверяем корректность сложения.

    post: __return__ == a + b
    post: __return__ >= a
    post: __return__ >= b

    Последние два свойства верны только для
    неотрицательных b и a соответственно.
    Поэтому здесь добавлены предусловия.
    """
    return a + b


# ============================================================
# 3. MAXIMUM — максимум двух чисел
# ============================================================

def maximum(a: int, b: int) -> int:
    """
    Возвращает максимальное число.

    post: __return__ >= a
    post: __return__ >= b
    post: __return__ == a or __return__ == b
    """
    if a > b:
        return a
    return b


# ============================================================
# 4. DIVISION — деление
# ============================================================

def divide(a: int, b: int) -> float:
    """
    Деление двух чисел.

    pre: b != 0

    post: __return__ == a / b
    """
    return a / b


# ============================================================
# 5. CLAMP — ограничение значения диапазоном
# ============================================================

def clamp(x: int, low: int, high: int) -> int:
    """
    Ограничивает x диапазоном [low, high].

    pre: low <= high

    post: __return__ >= low
    post: __return__ <= high
    post: __return__ == x or __return__ == low or __return__ == high
    """
    if x < low:
        return low

    if x > high:
        return high

    return x


# ============================================================
# 6. BROKEN FUNCTION — намеренно неправильная функция
# ============================================================

def broken_absolute(x: int) -> int:
    """
    Намеренная ошибка!

    Требуем, чтобы результат был неотрицательным.

    post: __return__ >= 0

    CrossHair должен найти отрицательное x,
    при котором постусловие нарушается.
    """
    return x


# ============================================================
# 7. EVEN NUMBER — проверка чётности
# ============================================================

def is_even(x: int) -> bool:
    """
    Проверяет чётность числа.

    post: __return__ == (x % 2 == 0)
    """
    return x % 2 == 0


# ============================================================
# 8. BINARY SEARCH — бинарный поиск
# ============================================================

def binary_search(arr: list[int], target: int) -> int:
    """
    Бинарный поиск в отсортированном массиве.

    pre: all(arr[i] <= arr[i+1] for i in range(len(arr)-1))
    
    post: (
        (__return__ == -1 and target not in arr)
        or
        (0 <= __return__ < len(arr)
         and arr[__return__] == target)
    )
    """
    # post: (__return__ == -1 and target not in arr) or (0 <= __return__ < len(arr) and arr[__return__] == target)
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid

        elif arr[mid] < target:
            left = mid + 1

        else:
            right = mid - 1

    return -1
