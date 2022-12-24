import pytest

from series.series import fibonacci, lucas

# proof of life
# def test_fibonacci_exists():
#     assert fibonacci


# # test fibonacci
def test_fibonacci_5():
    actual = fibonacci(5)
    expected = 5
    assert actual == expected

def test_fibonacci_9():
    actual = fibonacci(9)
    expected = 34
    assert actual == expected


def test_lucas_5():
    actual = lucas(5)
    expected = 11
    assert actual == expected


def test_lucas_7():
    actual = lucas(7)
    expected = 29
    assert actual == expected