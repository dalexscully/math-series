from math_series.series import fibonacci, lucas, sum_series


# Fibonacci test

def test_zero_output_zero():
    actual = fibonacci(0)
    expected = 0
    assert actual == expected


def test_one_output_one():
    actual = fibonacci(1)
    expected = 1
    assert actual == expected


def test_two_output_one():
    actual = fibonacci(2)
    expected = 1
    assert actual == expected


def test_three_output_two():
    actual = fibonacci(3)
    expected = 2
    assert actual == expected


def test_four_output_three():
    actual = fibonacci(4)
    expected = 3
    assert actual == expected


def test_five_output_five():
    actual = fibonacci(5)
    expected = 5
    assert actual == expected


def test_six_output_eight():
    actual = fibonacci(6)
    expected = 8
    assert actual == expected


def test_seven_output_thirteen():
    actual = fibonacci(7)
    expected = 13
    assert actual == expected


## Lucas test

def test_lucas_zero_output_two():
    actual = lucas(0)
    expected = 2
    assert actual == expected


def test_lucas_one_output_one():
    actual = lucas(1)
    expected = 1
    assert actual == expected


def test_lucas_two_output_three():
    actual = lucas(2)
    expected = 3
    assert actual == expected


def test_lucas_three_output_four():
    actual = lucas(3)
    expected = 4
    assert actual == expected


def test_lucas_four_output_seven():
    actual = lucas(4)
    expected = 7
    assert actual == expected


def test_lucas_five_output_eleven():
    actual = lucas(5)
    expected = 11
    assert actual == expected


def test_lucas_six_output_eighteen():
    actual = lucas(6)
    expected = 18
    assert actual == expected


def test_lucas_seven_output_twenty_nine():
    actual = lucas(7)
    expected = 29
    assert actual == expected


# Sum Series Test

def test_one_sum_series_fibonacci():
    actual = sum_series(0)
    expected = 0
    assert actual == expected


def test_two_sum_series_lucas():
    actual = sum_series(2, 2, 1)
    expected = 3
    assert actual == expected

