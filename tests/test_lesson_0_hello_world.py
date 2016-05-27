# This lesson teaches you how to define a Python method. Try running the tests for this file before doing anything!

# Here's a python script you can use to run your tests from the top level directory of this project
# `python -m unittest -vf tests.test_lesson_0_hello_world`
# That command looks like a lot at first. Let's break it down.


# `python` indicates that you want to run a python file
# -m tells python to run the module (tests.test_lesson_x) as a script
# unittest tells python that we're running unit tests on something
# -vf is the combination of two options that I'll outline separately below:
# -v encourages python to be as verbose as possible with its output
# -f tells python to stop running the tests once it hits a failure. This is entirely optional, but I
# want you to try running the tests one at a time, and fix each failure as it comes, rather than trying to
# make all the tests pass at once. That way you get a feel for how to build some python functions one idea at a time
# `tests.test_lesson_0_hello_world` is the specific module (composed of unit tests) that we're executing


# What error did you get when you first ran it? 
# Remember, errors are built to be **helpful**, not scary!

# It should be an ImportError. This is Python telling you that it's unable to import the file `hello_world`

# So your first step should be to create `hello_world.py` in the `lessons/lesson_0_hello_world` directory

# Run the tests again. 

import unittest

from lessons.lesson_0_hello_world import hello_world

class HelloWorldTestClass(unittest.TestCase):
    def test_hello_function_exists(self):
        func = hello_world.hello_world
        self.assertIsNotNone(func)

    def test_hello_function_output(self):
    	greeting = hello_world.hello_world()
    	self.assertEqual(greeting, "Hello World!")
