# This lesson introduces the concept of floating point math in Python

# Note: It's important for this lesson to know what version of python you're running.

# type `python --version` in your terminal to see what version of python you're using.

# As usual, run your python command in your terminal to see your first failure.

# `python -m unittest -vf tests.test_lesson_4_temperature`

# This challenge asks you to create two functions: `f_to_c` and `c_to_f`
# Your functions should be able to receive a float and return an integer.
# Try adding you own tests to make sure your functions are returning the correct values!

import pytest

import temperature


class TestCtoF():
    def test_handles_freezing_point(self):
        assert temperature.c_to_f(0) == 32

    def test_handles_boiling_point(self):
        assert temperature.c_to_f(100) == 212

    def test_handle_arbitrary_temp(self):
        assert temperature.c_to_f(20) == 68

    def test_another_arbitrary_temp(self):
        assert temperature.c_to_f(-17) == 1

    def test_handles_body_temp(self):
        assert temperature.c_to_f(37) == 98

    def test_convergence_point(self):
        assert temperature.c_to_f(-40) == -40


class TestFtoC():
    def test_handles_freezing_point(self):
        assert temperature.f_to_c(32) == 0

    def test_handles_boiling_point(self):
        assert temperature.f_to_c(212) == 100

    def test_handles_arbitrary_temp(self):
        assert temperature.f_to_c(68) == 20

    def test_handles_another_arbitrary_temp(self):
        assert temperature.f_to_c(0) == -17

    def test_handles_body_temp(self):
        assert temperature.f_to_c(98.6) == 37

    def test_convergence_point(self):
        assert temperature.f_to_c(-40) == -40
