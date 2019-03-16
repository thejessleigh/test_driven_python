# This lesson teaches you how to define a Python method. Try running the tests for this file before doing anything!

# To run the file, navigate to the lesson 0 directory in your terminal and type `pytest`.

# What error did you get when you first ran it?
# Remember, errors are built to be **helpful**, not scary!

# It should be an ImportError. This is Python telling you that it's unable to import the file `hello_world`

# So your first step should be to create `hello_world.py` in the `lessons/lesson_0_hello_world` directory

# Run the tests again after each code change. Repeat this process until the test file runs without outputting anything.

import pytest

import hello_world


def test_hello_function_exists():
    func = hello_world.hello_world
    assert func is not None


def test_hello_output():
    assert hello_world.hello_world() == "Hello World!"
