"""Demo module used to generate UT coverage for upload-ut-action testing."""


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ValueError('division by zero')
    return a / b


def is_even(n):
    return n % 2 == 0


def factorial(n):
    if n < 0:
        raise ValueError('n must be non-negative')
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result
