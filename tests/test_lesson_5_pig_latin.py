# In this lesson you'll be working with regular expressions for the first time. For an introduction to
# regular expressions, refer to `lesson_5_pig_latin/index.html`. If you're still unsure how to proceed,
# check out the additional resources linked in the lesson.

# Regular expressions are rules you construct to figure out patterns inside strings.

# You'll need to write a function called `translate` in your lesson_5_pig_latin.pig_latin file. However
# you might want to construct one or more helper methods that do the heavy lifting of your translation
# operation. This lesson's `index.html` file has more information about helper methods and separation
# of concerns.

# Run your tests!
# `python -m unittest -vf tests.test_lesson_5_pig_latin`

# Rules:
# - Single letter words are appended with "ay"
# - Ex: "i" -> "iay"
# - Words that start with vowels are appended with "ay"
# - Ex: "apple" -> "appleay"
# - Words that start with consonants have the beginning consonant group shifted to the end of the word.
#       The new "shifted" word is appended with "ay"
# - Ex: "whiskers" -> "iskerswhay"
# - "qu" is treated as a single consonant
# - Ex: "quit" -> "itquay"
# - If a string contains multiple words, it should transform each word individually.
# - Ex: "hello world" -> "ellohay orldway"

# BONUS
# There is an additional bonus test class with a `skip` decorator on top of it. For more information
# on decorators, refer to `lesson_5_pig_latin/bonus.html`
# To run the bonus tests, comment out or remove the skip decorator
# Bonus Rules:
# - Words that are capitalized should have the first letter of the translated word capitalized.
#        If the initial letter of the word has been shifted, it should no longer be capitalized.
# - Ex: "Mary" -> "Arymay", "Eliose" -> "Eloiseay"
# - Punctionation that occurs at the end of a word or phrase, like periods or question marks, should
#        stay at the end of that word or phrase.
# - Ex: "Wow!" -> "Owway!", "When did that happen?" -> "Ehenway idday atthay appenhay?"
# - Punctuation that occurs in the middle of a word, like an apostrophe, should stay where it is.
# - Ex: "isn't" -> "isn'tay", "wasn't" -> "asn'tway"


import unittest

from lessons.lesson_5_pig_latin import pig_latin


class PigLatinTestCase(unittest.TestCase):
    def test_word_starting_with_vowel(self):
        word = pig_latin.translate("apple")
        self.assertEqual(word, "appleay")
        word = pig_latin.translate("am")
        self.assertEqual(word, "amay")

    def test_word_starting_with_consonant(self):
        word = pig_latin.translate("word")
        self.assertEqual(word, "ordway")
        word = pig_latin.translate("whiskers")
        self.assertEqual(word, "iskerswhay")

    def test_translates_phrases(self):
        phrase = pig_latin.translate("number games")
        self.assertEqual(phrase, "umbernay amesgay")
        phrase = pig_latin.translate("monster offspring")
        self.assertEqual(phrase, "onstermay offspringay")

    def test_translates_word_beginning_with_three_consonants(self):
        word = pig_latin.translate("three")
        self.assertEqual(word, "eethray")
        word = pig_latin.translate("shrug")
        self.assertEqual(word, "ugshray")

    def test_handles_qu_at_the_beginning_of_a_word(self):
        word = pig_latin.translate("quit")
        self.assertEqual(word, "itquay")
        word = pig_latin.translate("quiet")
        self.assertEqual(word, "ietquay")

    def test_handles_qu_after_initial_consonant(self):
        word = pig_latin.translate("square")
        self.assertEqual(word, "aresquay")
        word = pig_latin.translate("squish")
        self.assertEqual(word, "ishsquay")

    def test_one_letter_words(self):
        word = pig_latin.trainslate("a")
        self.assertEqual(word, "aay")
        word = pig_latin.translate("i")
        self.assertEqual(word, "iay")


###################
###STRETCH GOALS###
###################
# To attempt these, remove the "skip" line from the test case

@unittest.skip
class PigLatinStretchGoalsTestCase(unittest.TestCase):
    def test_handles_punctuation(self):
        sentence = pig_latin.translate("we had fun!")
        self.assertEqual(sentence, "eway adhay unfay!")
        sentence = pig_latin.translate("the quick brown fox went home.")
        self.assertEqual(sentence, "ethay ickquay ownbray oxfay entway omehay.")

    def test_handles_capitalization(self):
        name = pig_latin.translate("Emily")
        self.assertEqual(name, "Emilyay")
        name = pig_latin.translate("Zelda Fitzgerald")
        self.assertEqual(name, "Eldazay Itzgeraldfay")

    def test_handles_apostrophes(self):
        sentence = pig_latin.translate("She doesn't understand French.")
        self.assertEqual(sentence, "Eshay oesn'tday understanday Enchfray.")
        title = pig_latin.translate("It's a Wonderful Life")
        self.assertEqual(title, "It'say aay Onderfulway Ifelay")
