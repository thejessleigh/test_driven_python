# In this lesson you'll create several functions to perform basic calculations

# Run your tests to get your first failure. Try reading the tests first to anticipate which failures
# you'll run into.

# You should create 3 functions:

# `add` should accept two integers and return the sum of those two integers
# `subtract` should accept two integers and return the first integer minus the second
# `total_sum` should accept a list of integers and return the total sum of all the array elements
#       note: if total_sum receives an empty list, it should return 0

# All three functions should be able to handle both positive and negative integers


import pytest

import calculator

class TestAdd():
    def test_add_returns_sum_of_two_numbers(self):
        assert calculator.add(2, 3) == 5
        assert calculator.add(7, 3) == 10

    def test_add_position_of_arguments_does_not_matter(self):
        a = calculator.add(2, 3)
        b = calculator.add(3, 2)
        assert a == b

    def test_add_handles_negative_numbers(self):
        assert calculator(-3, 5) == 2
        assert calculator(0, -2) == -2


class TestSubtract():
    def test_subtract_returns_first_argument_minus_second(self):
        assert calculator.subtract(10, 7) == 3

    def test_position_matters_for_subtraction(self):
        assert calculator.subtract(10, 7) != calculator.subtract(7, 10)

    def test_subtract_negative_numbers(self):
        assert calculator.subtract(-7, -8) == 1
        assert calculator.subtract(0, -3) == 3
        assert calculator.subtract(-3, 6) == -9

class TestTotalSum():
    def test_total_sum_accepts_list_and_returns_sum_of_list(self):
        assert calculator.total_sum([1, 2, 3]) == 6

    def test_total_sum_handles_negative_integers(self):
        assert calculator.total_sum([-1, -2, -3]) == -6

    def total_sum_handles_mix_of_positive_and_negative_integers(self):
        assert calculator.total_sum([1, 2, -3, -5]) == -5

    def test_empty_array_input_returns_zero(self):
        assert calculator.total_sum([]) == 0
