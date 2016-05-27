# This lesson teaches you how to define a function that takes an input, and then uses
# it to alter the output of that function.

# Much like last time, run your python command in your terminal to see your first failure.

# `python -m unittest -vf tests.test_lesson_1_greetings`

# Again, like last time, you should see an import error indicating that you need a file titled
# `greetings` in your lesson folder.

# This challenge is very similar to the last one, but instead of always outputting the same string - "Hello World!",
# the output will change based on the input you give to the function.


import unittest

from lessons.lesson_1_greetings import greetings


class GreetingsTestCase(unittest.TestCase):
	def test_greetings_function_exists(self):
		func = greetings.greetings
		self.assertIsNotNone(func)

	def test_greetings_function_with_input(self):
		greet = greetings.greetings("Amy")
		self.assertEqual(greet, "Hi, Amy!")

	def test_grettings_function_with_another_input(self):
		greet = greetings.greetings("Belle")
		self.assertEqual(greet, "Hi, Belle!")
