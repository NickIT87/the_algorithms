# lambda_calculus.py
# Минимальная реализация чистого лямбда-исчисления на Python

# ------------------------------
# 1. Логические значения
# ------------------------------

TRUE  = lambda x: lambda y: x
FALSE = lambda x: lambda y: y

# Условное выражение
IF = lambda cond: lambda a: lambda b: cond(a)(b)

# Проверки
print("=== Логика ===")
print("TRUE →", TRUE("кот")("пёс"))    # кот
print("FALSE →", FALSE("кот")("пёс"))  # пёс
print("IF TRUE →", IF(TRUE)("да")("нет"))   # да
print("IF FALSE →", IF(FALSE)("да")("нет")) # нет

# ------------------------------
# 2. Числа Чёрча
# ------------------------------

ZERO  = lambda f: lambda x: x
ONE   = lambda f: lambda x: f(x)
TWO   = lambda f: lambda x: f(f(x))
THREE = lambda f: lambda x: f(f(f(x)))
FOUR  = lambda f: lambda x: f(f(f(f(x))))
FIVE  = lambda f: lambda x: f(f(f(f(f(x)))))

# Утилита для перевода в обычное число
to_int = lambda n: n(lambda x: x + 1)(0)

print("\n=== Числа Чёрча ===")
print("ZERO  =", to_int(ZERO))
print("THREE =", to_int(THREE))

# ------------------------------
# 3. Арифметика
# ------------------------------

ADD = lambda m: lambda n: lambda f: lambda x: m(f)(n(f)(x))
MUL = lambda m: lambda n: lambda f: m(n(f))

# Предшественник (n-1)
PRED = lambda n: (
    lambda f: lambda x:
        n(lambda g: lambda h: h(g(f)))(lambda u: x)(lambda u: u)
)

# Проверка на ноль
IS_ZERO = lambda n: n(lambda x: FALSE)(TRUE)

print("\n=== Арифметика ===")
print("2 + 3 =", to_int(ADD(TWO)(THREE)))
print("2 * 3 =", to_int(MUL(TWO)(THREE)))
print("PRED(3) =", to_int(PRED(THREE)))
print("IS_ZERO(0) =", IS_ZERO(ZERO)("да")("нет"))
print("IS_ZERO(1) =", IS_ZERO(ONE)("да")("нет"))

# ------------------------------
# 4. Рекурсия и факториал (через Y-комбинатор)
# ------------------------------

Y = lambda f: (lambda x: f(lambda v: x(x)(v)))(lambda x: f(lambda v: x(x)(v)))

FACT = Y(lambda f: lambda n:
    IF(IS_ZERO(n))
      (lambda _: ONE)
      (lambda _: MUL(n)(f(PRED(n))))
)

print("\n=== Факториал через Y-комбинатор ===")
print("3! =", to_int(FACT(THREE)))
print("4! =", to_int(FACT(FOUR)))
print("5! =", to_int(FACT(FIVE)))

# -------------------
# 5. Факториал через Python-рекурсию
# -------------------

def FACT2(n):
    if to_int(n) == 0:
        return ONE
    else:
        return MUL(n)(FACT2(PRED(n)))

print("\n=== Факториал через Python-рекурсию ===")
print("3! =", to_int(FACT2(THREE)))
print("4! =", to_int(FACT2(FOUR)))
print("5! =", to_int(FACT2(FIVE)))

# ------------------------------
# 6. Завершение
# ------------------------------

print("\nВсе вычисления завершены успешно ✅")
