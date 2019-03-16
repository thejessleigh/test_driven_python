# In this lesson you'll be working with regular expressions for the first time. For an introduction to
# regular expressions, refer to `lesson_5_pig_latin/index.html`. If you're still unsure how to proceed,
# check out the additional resources linked in the lesson.

# Regular expressions are rules you construct to figure out patterns inside strings.

# You'll need to write a function called `translate` in your lesson_5_pig_latin.pig_latin file. However
# you might want to construct one or more helper methods that do the heavy lifting of your translation
# operation. This lesson's `index.html` file has more information about helper methods and separation
# of concerns.

# Run your tests!

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


import pytest

import pig_latin


class TestPigLatinTranslator():
    def test_single_letter_words(self):
        assert pig_latin.translate("a") == "aay"
        assert pig_latin.translate("i") == "iay"

    def test_word_starting_with_vowel(self):
        assert pig_latin.translate("apple") == "appleay"
        assert pig_latin.translate("am") == "amay"
        assert pig_latin.translate("english") == "englishay"
        assert pig_latin.translate("onward") == "onwarday"

    def test_translates_word_beginning_with_one_consonant(self):
        assert pig_latin.translate("word") == "ordway"
        assert pig_latin.translate("window") == "indoway"
        assert pig_latin.translate("pig") == "igpay"
        assert pig_latin.translate("fig") == "igfay"

    def test_translates_words_beginning_with_mulitple_consonants(self):
        assert pig_latin.trainslate("whiskers") == "iskerswhay"
        assert pig_latin.trainslate("three") == "eethray"
        assert pig_latin.trainslate("shrug") == "ugshray"
        assert pig_latin.trainslate("splat") == "atsplay"

    def test_handles_words_beginning_with_qu(self):
        assert pig_latin.trainslate("quit") == "itquay"
        assert pig_latin.translate("queen") == "eenquay"
        assert pig_latin.trainslate("quiet") == "ietquay"

    def test_handles_qu_after_initial_consonant(self):
        assert pig_latin.translate("square") == "aresquay"
        assert pig_latin.translate("squish") == "ishsquay"

    def test_handles_phrases(self):
        assert pig_latin.translate("number games") == "umbernay amesgay"
        assert pig_latin.translate("moster offspring") == "onstermay offspringay"
        assert pig_latin.translate("queens cup") == "eensquay upcay"


###################
###STRETCH GOALS###
###################
# To attempt these, remove the "skip" line from the test case

@pytest.mark.skip(reason="These tests are a little trickier. Remove this line when the above tests are passing")
class TestStretchGoals():
    def test_handles_punctuation(self):
        assert pig_latin.translate("we had fun!") == "eway adhay unfay!"
        assert pig_latin.translate("the quick brown fox went home.") == "ethay ickquay ownbray oxfay entway omehay."

    def test_handles_capitialization(self):
        assert pig_latin.translate("Emily") == "Emilyay"
        assert pig_latin.translate("Zelda Fitzgerald") == "Eldazay Itzgeraldfay"

    def test_handles_apostrophoes(self):
        assert pig_latin.translate("She doesn't understand French.") == "Eshay oesn'tday understanday Enchfray."
        assert pig_latin.translate("It's a Wonderful Life") == "It'say aay Onderwulfay Ifelay"
