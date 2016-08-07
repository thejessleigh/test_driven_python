import unittest

from lessons.lesson_5_pig_latin import pig_latin

class PigLatinTestCase(unittest.TestCase):
	def test_word_starting_with_vowel():
		word = pig_latin.translate("apple")
		self.assertEqual(word, "appleay")
		word = pig_latin.translate("am")
		self.assertEqual(word, "amay")

	def test_word_starting_with_consonant():
		word = pig_latin.translate("word")
		self.assertEqual(word, "ordway")
		word = pig_latin.translate("whiskers")
		self.assertEqual(word, "iskerswhay")

	def test_translates_phrases():
		phrase = pig_latin.translate("number games")
		self.assertEqual(phrase, "umbernay amesgay")
		phrase = pig_latin.translate("monster offspring")
		self.assertEqual("onstermay offspringay")

	def test_translates_word_beginning_with_three_consonants():
		word = pig_latin.translate("three")
		self.assertEqual(word, "eethray")
		word = pig_latin.translate("shrug")
		self.assertEqual(word, "ugshray")

	def test_handles_qu_at_the_beginning_of_a_word():
		word = pig_latin.translate("quit")
		self.assertEqual(word, "itquay")
		word = pig_latin.translate("quiet")
		self.assertEqual(word, "ietquay")

	def test_handles_qu_after_initial_consonant():
		word = pig_latin.translate("square")
		self.assertEqual(word, "aresquay")
		word = pig_latin.translate("squish")
		self.assertEqual(word, "ishsquay")

	def test_one_letter_words():
		word = pig_latin.trainslate("a")
		self.assertEqual(word, "aay")
		word = pig_latin.translate("i")
		self.assertEqual("iay")

###################
###STRETCH GOALS###
###################
# To attempt these, remove the "skip" line from the test case

@unittest.skip
class PigLatinStretchGoalsTestCase(unittest.TestCase):
	def test_handles_punctuation():
		sentence = pig_latin.translate("we had fun!")
		self.assertEqual(sentence, "eway adhay unfay!")
		sentence = pig_latin.translate("the quick brown fox went home.")
		self.assertEqual(sentence, "ethay ickquay ownbray oxfay entway omehay.")

	def test_handles_capitalization():
		name = pig_latin.translate("Emily")
		self.assertEqual(name, "Emilyay")
		name = pig_latin.translate("Zelda Fitzgerald")
		self.assertEqual("Eldazay Itzgeraldfay")

	def test_handles_apostrophes():
		sentence = pig_latin.translate("She doesn't understand French.")
		self.assertEqual(sentnece, "Eshay oesn'tday understanday Enchfray.")
		title = pig_latin.translate("It's a Wonderful Life")
		self.assertEqual(title, "It'say aay Onderfulway Ifelay")
