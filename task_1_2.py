# ЗаЗАВДАННЯ 1
# замикання + кеш + рекурсія
# caching_fibonacci

from typing import Callable, Generator
import re

def caching_fibonacci() -> Callable[[int], int]:
    """
    функція створює кеш та повертає внутрішню функцію
    fibonacciб яка памяає кеш
    """
    cache = {} # словник для збереження обчислених значень

    def fibonacci(n: int) -> int:
        """
        обчислює n-e число рекурсивно з використанням кешу
        """
        # базові випадки (для зупинки рекурсії)
        if n <=0:
            return 0
        if n==1:
            return 1
        
        # якщо прораховували - повертаємо з кеш
        if n in cache:
            return cache[n]
        
        # якщо не рахували - обчислюємо
        cache[n] = fibonacci(n-1) + fibonacci(n-2)
        return cache[n]

    return fibonacci


# ЗАВДАННЯ 2

def generator_numbers(text: str) -> Generator[float, None, None]:
    """
    генератор знаходить дійсні числа
    відокремлені пробілами з обох боків
    """
    pattern = r" (?P<num>\d+\.\d+) "
    # finditer дає всі збіги по тексту 
    for match in re.finditer(pattern, text):
        yield float(match.group("num"))

def sum_profit(text: str, func: Callable[[str], Generator[float, None, None]]) -> float:
    """
    func - функція генератор
    sum(...) пыдсумовує значення які видасть генератор
    """
    return sum(func(text))

# Запуск

if __name__ =="__main__":
    print("= ЗАВДАННЯ 1 =")

    fib = caching_fibonacci()

    print("fib(10):", fib(10)) #55
    print("fib(15):", fib(15)) #610

    print("\n = ЗАВДАННЯ 2 =")

    text =(
        "Загальний дохід працівника складається з декількох частин: "
        "1000.01 як основний дохід, доповнений додатковими надхлдженнями"
        " 27.45 і 324.00 доларів. Test space-500.00 "
    )

    total_income = sum_profit(text, generator_numbers)
    print("загальний дохід:", total_income)
    
    