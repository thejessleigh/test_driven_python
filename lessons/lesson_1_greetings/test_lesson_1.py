# This lesson teaches you how to define a function that takes an input, and then uses
# it to alter the output of that function.

# Much like last time, navigate to the lesson_1_greetings directory in your terminal and run your python command
# `pytest`

# Again, like last time, you should see an import error indicating that you need a file titled
# `greetings` in your lesson folder.

# This challenge is very similar to the last one, but instead of always outputting the same string - "Hello World!",
# the output will change based on the input you give to the function.


import pytest

import greetings


def test_greetings_function_exists():
    func = greetings.greet
    assert func is not None


def test_greetings_function_with_input():
    greet = greetings.greet("Anna")
    assert greet == "Hi, Anna!"


def test_greetings_function_with_another_input():
    greet = greetings.greet("Elsa")
    assert greet == "Hi, Elsa!"
