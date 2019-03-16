# Fizzbuzz is a common coding challenge that teaches control flow and use of the modulus operator.

# Some FizzBuzz challenges will have you print out the result for each number from 1 to x.
# In this challenge however, we'll save all of the 'Fizzbuzzed' results to an list
# and return the list at the end of the function.

# If you've worked in other programming languages before, or if you're familiar with different
# structures in math, a list is Python's name for an array. Two square brackets ("[]") are the way
# Python represents an empty list. The list can hold any number of items. The items do not need to be the same type.
# Lists are ordered. That means that to access a value inside the list, you need to know what position it occupies in
# the list.
# List positions, or "indexes" (or "indicies" - both are correct and people will use them interchangeably), start
# counting at 0, not 1.

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
#
#
# Bonus challenge:
# Amend the `test_fizzbuzz_handles_negative_integers` function below to expect FizzBuzz to handle negative integers.
# See if you can write your own test and then get your code to pass!


import pytest

from fizzbuzz import fizzbuzz


def test_fizzbuzz_returns_list():
    twelve = fizzbuzz(12)
    assert type(twelve) == list


def test_fizzbuzz_list_is_correct_length():
    twelve = fizzbuzz(12)
    assert len(twelve) == 12
    eighty = fizzbuzz(80)
    assert len(eighty) == 80


def test_fizzbuzz_multiples_of_3():
    twelve = fizzbuzz(12)
    assert twelve[2] == "Fizz"
    assert twelve[5] == "Fizz"
    assert twelve[8] == "Fizz"
    assert twelve[11] == "Fizz"


def test_fizzbuzz_handles_multiples_of_5():
    twenty_five = fizzbuzz(25)
    assert twenty_five[4] == "Buzz"
    assert twenty_five[9] == "Buzz"
    assert twenty_five[19] == "Buzz"
    assert twenty_five[24] == "Buzz"


def test_fizzbuzz_handles_multiples_of_3_and_5():
    eighty = fizzbuzz(80)
    assert eighty[14] == "FizzBuzz"
    assert eighty[29] == "FizzBuzz"
    assert eighty[44] == "FizzBuzz"
    assert eighty[59] == "FizzBuzz"


def test_fizzbuzz_saves_non_fizzbuzzable_integers_to_list():
    seventy_three = fizzbuzz(73)
    assert type(seventy_three[0]) == int
    assert seventy_three[0] == 1
    assert type(seventy_three[12]) == int
    assert seventy_three[12] == 13
    assert type(seventy_three[-1]) == int
    assert seventy_three[-1] == 73


def test_fizzbuzz_handles_zero():
    zero = fizzbuzz(0)
    assert type(zero) == list
    assert len(zero) == 0


def test_fizzbuzz_handles_negative_integers():
    negative = fizzbuzz(-15)
    assert type(negative) == list
    assert len(negative) == 0
