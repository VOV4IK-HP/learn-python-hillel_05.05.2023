# 1. Функция-генератор последовательности чисел "Фибоначчи":

def fibonacci_gen(n):
    a = 0
    b = 1
    yield a
    for _ in range(n - 1):
        yield b
        a, b = b, a + b


# Использование функции-генератора:

for num in fibonacci_gen(10):
    print(num)


# 2. Функция-генератор для разделения строки на отдельные слова:

def word_gen(s):
    words = s.split()
    for word in words:
        yield word


# Использование функции-генератора:

for word in word_gen('i am generating words from text'):
    print(word)
