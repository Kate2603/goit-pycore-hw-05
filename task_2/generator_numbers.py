import re

def generator_numbers(text: str):
    """
    Generator that yields all valid numbers in the given text.
    """
    pattern = r"\b\d+(?:\.\d+)?\b"
    numbers = re.findall(pattern, text)
    for number in numbers:
        yield float(number)

def sum_profit(text: str, func: callable):
    """
    Calculate the total sum of numbers in the given text using the provided function.
    """
    numbers = func(text)
    total_sum = sum(numbers)
    return total_sum

text = "The total income of an employee consists of several parts: 1000.01 as the main income, supplemented by additional income of 27.45 and 324.00 dollars."
total_income = sum_profit(text, generator_numbers)
print(f"Total income: {total_income:.2f}") # Загальний дохід: 1351.46