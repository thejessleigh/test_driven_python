# This lesson introduces the concept of floating point math in Python

# Note: It's important for this lesson to know what version of python you're running.

# type `python --version` in your terminal to see what version of python you're using.

# As usual, run your python command in your terminal to see your first failure.

# `python -m unittest -vf tests.test_lesson_4_temperature`

# This challenge asks you to create two functions: `f_to_c` and `c_to_f`
# Your functions should be able to receive a float and return an integer.
# Try adding you own tests to make sure your functions are returning the correct values!

import unittest

from lessons.lesson_4_temperature import temperature


class CtoFTestCase(unittest.TestCase):
    def test_handles_freezing_point(self):
        freezing = temperature.c_to_f(0)
        self.assertEqual(freezing, 32)

    def test_handles_boiling_point(self):
        boiling = temperature.c_to_f(100)
        self.assertEqual(boiling, 212)

    def test_handle_room_temp(self):
        arbitrary = temperature.c_to_f(20)
        self.assertEqual(arbitrary, 68)

    def test_handles_body_temp(self):
        body_temp = temperature.c_to_f(37)
        self.assertEqual(body_temp, 98)


class FtoCTestCase(unittest.TestCase):
    def test_handles_freezing_point(self):
        freezing = temperature.f_to_c(32)
        self.assertEqual(freezing, 0)

    def test_handles_boiling_point(self):
        boiling = temperature.f_to_c(212)
        self.assertEqual(boiling, 100)

    def test_handles_arbitrary_temp(self):
        arbitrary = temperature.f_to_c(68)
        self.assertEqual(arbitrary, 20)

    def test_handles_body_temp(self):
        body_temp = temperature.f_to_c(98.6)
        self.assertEqual(body_temp, 37)
