"""Minimal pytest suite for the demo module."""

import pytest

from calculator import add, divide, factorial, is_even, multiply, subtract


def test_add():
    assert add(1, 2) == 3


def test_subtract():
    assert subtract(5, 3) == 2


def test_multiply():
    assert multiply(4, 3) == 12


def test_divide():
    assert divide(6, 3) == 2


def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(1, 0)


def test_is_even():
    assert is_even(2)
    assert not is_even(3)


def test_factorial():
    assert factorial(0) == 1
    assert factorial(5) == 120


def test_factorial_negative():
    with pytest.raises(ValueError):
        factorial(-1)
