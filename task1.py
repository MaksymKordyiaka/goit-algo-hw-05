'''
Реалізуйте функцію caching_fibonacci, яка створює та використовує кеш
для зберігання і повторного використання вже обчислених значень чисел Фібоначчі.

Ряд Фібоначчі - це послідовність чисел виду: 0, 1, 1, 2, 3, 5, 8, ..., де
кожне наступне число послідовності виходить додаванням двох попередніх членів ряду.

У загальному вигляді для обчислення n-го члена ряду Фібоначчі
потрібно вирахувати вираз: Fn = F(n-1) + F(n-2).
'''

def caching_fibonacci():
    cache = {}
    def fibonacci(n):
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        elif n in cache:
            return cache[n]
        cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
        return cache[n]
    return fibonacci
fib = caching_fibonacci()

print(fib(1))
print(fib(4))
print(fib(9))
print(fib(16))
