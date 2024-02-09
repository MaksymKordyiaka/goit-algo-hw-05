'''
Необхідно створити функцію generator_numbers, яка буде аналізувати текст, ідентифікувати
всі дійсні числа, що вважаються частинами доходів, і повертати їх як генератор.
Дійсні числа у тексті записані без помилок, чітко відокремлені пробілами з обох боків.
Також потрібно реалізувати функцію sum_profit, яка буде використовувати
generator_numbers для підсумовування цих чисел і обчислення загального прибутку.
'''

import re
from typing import Callable

def generator_numbers(text: str):
    # Знаходимо всі числа з плаваючою точкою у тексті
    numbers = re.findall(r'\b\d+\.\d+\b', text)
    # Проходимося по знайденим числам і повертаємо їх як float
    for number_str in numbers:
        yield float(number_str)

def sum_profit(text: str, func: Callable):
    total = 0
    # Викликаємо функцію-генератор для отримання чисел і додаємо їх
    for number in func(text):
        total += number
    return total

text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
# Викликаємо функцію sum_profit з текстом та функцією-генератором чисел
total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")

