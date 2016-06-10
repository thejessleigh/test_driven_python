# Fizzbuzz is a common coding challenge that teaches control flow and use of the modulus operator.

# Some FizzBuzz challenges will have you print out the result for each number from 1 to x.
# In this challenge however, we'll save all of the 'Fizzbuzzed' results to an list
# and return the list at the end of the function.

# If you've worked in other programming langauges before, or if you're familiar with different
# structures in math, a list is Python's name for an array. Two square brackets ("[]") are the way
# Python represents an empty list. The list can hold any number of items. The items do not need to be the same type.
# Lists are ordered. That means that to access a value inside the list, you need to know what position it occupies in the list.
# List positions, or "indexes" (or "indicies" - both are correct and people will use them interchangeably), start counting at 0, not 1.

# Challenge Rules:
# - The function should accept an integer
# - For every integer between 1 and the input the function should save one of four options to an list
#     - If the integer is divisible by 3, save the word "Fizz" to the list
#     - If the integer is divisible by 5, save the word "Buzz" to the list
#     - If the integer is divisible by both 3 and 5, save the word "FizzBuzz" to the list
#     - If the integer is divisible by neither 3 nor 5, save that integer to the list
# - Return the list of integers and strings
# - Edge cases:
#     - If the integer input is <= 0, return an emtpy list

import unittest

from lessons.lesson_2_fizzbuzz import fizzbuzz


class FizzBuzzTestCase(unittest.TestCase):
    def test_fizzbuzz_returns_list(self):
        twelve = fizzbuzz.fizzbuzz(12)
        self.assertIsInstance(twelve, list)


    def test_fizzbuzz_list_is_the_correct_length(self):
        twelve = fizzbuzz.fizzbuzz(12)
        self.assertEqual(len(twelve), 12)
        eighty = fizzbuzz.fizzbuzz(80)
        self.assertEqual(len(eighty), 80)

    def test_fizzbuzz_handles_multiples_of_3(self):
        up_to_twelve = fizzbuzz.fizzbuzz(12)
        self.assertEqual(up_to_twelve[2], "Fizz")
        self.assertEqual(up_to_twelve[5], "Fizz")
        self.assertEqual(up_to_twelve[8], "Fizz")
        self.assertEqual(up_to_twelve[11], "Fizz")

    def test_fizzbuzz_handles_multiples_of_5(self):
        up_to_twenty_five = fizzbuzz.fizzbuzz(25)
        self.assertEqual(up_to_twenty_five[4], "Buzz")
        self.assertEqual(up_to_twenty_five[9], "Buzz")
        self.assertEqual(up_to_twenty_five[19], "Buzz")

    def test_fizzbuzz_handles_multiples_of_3_and_5(self):
        up_to_eighty = fizzbuzz.fizzbuzz(60)
        self.assertEqual(fizzbuzz[14], "FizzBuzz")
        self.assertEqual(fizzbuzz[29], "FizzBuzz")
        self.assertEqual(fizzbuzz[44], "FizzBuzz")
        self.assertEqual(fizzbuzz[59], "FizzBuzz")

    def test_fizzbuzz_saves_non_fizzbuzzable_integers_to_list(self):
        up_to_seventy_three = fizzbuzz.fizzbuzz(73)
        self.assertIsInstance(up_to_seventy_three[0], int)
        self.assertEqual(up_to_seventy_three[0], 1)
        self.assertIsInstance(up_to_seventy_three[12], int)
        self.assertEqual(up_to_seventy_three[12], 13)
        self.assertIsInstance(up_to_seventy_three[-1], int)
        self.assertEqual(up_to_seventy_three[-1], 73)

    def test_fizzbuzz_handles_zero(self):
        zero = fizzbuzz.fizzbuzz(0)
        self.assertIsInstance(zero, list)
        self.assertListEqual(zero, [])

    def test_fizzbuzz_handles_negative_integers(self):
        negative = fizzbuzz.fizzbuzz(-15)
        self.assertIsInstance(negative, list)
        self.assertListEqual(negative, [])
