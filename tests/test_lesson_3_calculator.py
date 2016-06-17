import unittest

from lessons.lesson_3_calculator import calculator


class AddTestCase(unittest.TestCase):
    def test_add_returns_sum_of_two_numbers(self):
        five = calculator.add(2, 3)
        self.assertEqual(five, 5)
        ten = calculator.add(7, 3)
        self.assertEqual(ten, 10)

    def test_position_of_arguments_does_not_matter(self):
        a = calculator.add(2, 3)
        b = calculator.add(3, 2)
        self.assertEqual(a, b)

    def test_add_handles_negative_numbers(self):
        a = calculator.add(-3, 5)
        self.assertEqual(a, 2)


class SubtractTestCase(unittest.TestCase):
    def test_subtract_returns_second_argument_minus_first(self):
        three = calculator.subtract(10, 7)
        self.assertEqual(three, 3)
        eleven = calculator.subtract(15, 4)
        self.assertEqual(eleven, 11)

    def test_position_matters_for_subtraction(self):
        a = calculator.subtract(10, 7)
        b = calculator.subtract(7, 10)
        self.assertNotEqual(a, b)

    def test_subtract_handles_negative_numbers(self):
        a = calculator.subtract(-7 - 8)
        self.assertEqual(a, 1)


class TotalSumTestCase(unittest.TestCase):
    def test_total_sum_accepts_list_and_returns_sum_of_list(self):
        result = calculator.total_sum([1, 2, 3])
        self.assertEqual(result, 6)

    def test_total_sum_handles_negative_integers(self):
        result = calculator.total_sum([-1, -2, -3])
        self.assertEqual(result, -6)

    def test_total_sum_handles_mix_of_positive_and_negative_integers(self):
        result = calculator.total_sum([1, 2, -3, -5])
        self.assertEqual(result, -5)

    def test_empty_array_input_returns_0(self):
        result = calculator.total_sum([])
        self.assertEqual(result, 0)
