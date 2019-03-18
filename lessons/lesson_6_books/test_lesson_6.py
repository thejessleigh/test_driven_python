# English conventions for capitalizing titles can be a bit tricky. In this lesson you'll work on putting
# some of these finnicky rules into practice.
# Create a Book class that accepts a string parameter - the book's title - and assigns the correctly capitalized
# version of that title as a `Book.title` attribute.
# This is the first time you'll be working with classes in this course, so be sure to check out the Python documentation
# for how to declare a class and how to assign instance variables like `title`.

# Capitalization rules - we'll use the Chicago Manual of Style rules for this exercise
# 1. Capitalize the first and last word
# 2. Capitalize nouns, pronouns, adjectives, verbs, adverbs, and subordinate conjunctions (although, because)
# 3. Lowercase articles (a, an, the), coordinating conjunctions (and, but, or), and prepositions
# 4. Lowercase the `to` in an infinitive (Let's Learn to Play Chess)



import pytest

from books import Book

class TestBookClass():
    def test_can_create_book(self):
        book = Book("a")
        assert book is not None

    def test_capitalize_first_letter(self):
        book = Book("homegoing")
        assert book.title == "Homegoing"

    def test_capitalize_every_word(self):
        book = Book("animal farm")
        assert book.title == "Animal Farm"
        book = Book("true grit")
        assert book.title == "True Grit"

    def test_no_article_capitalization(self):
        book = Book("to kill a mockingbird")
        assert book.title == "To Kill a Mockingbird"

    def test_no_coordinating_conjunction_capitalization(self):
        book = Book("pride and prejudice")
        assert book.title == "Pride and Prejudice"

    def test_no_article_capitalization_except_beginning_of_title(self):
        book = Book("the great gatsby")
        assert book.title == "The Great Gatsby"
        book = Book("the sound and the fury")
        assert book.title == "The Sound and the Fury"

    def test_coordinating_conjunction_capitalized_as_first_word(self):
        book = Book("and then there were none")
        assert book.title == "And Then There Were None"

    def test_no_preposition_capitalization(self):
        book = Book("love in the time of cholera")
        assert book.title == "Love in the Time of Cholera"
        book = Book("one flew over the cuckoo's nest")
        assert book.title == "One Flew over the Cuckoo's Nest"

    def test_no_preposition_capitalization_except_beginning_of_title(self):
        book = Book("in cold blood")
        assert book.title == "In Cold Blood"
        book = Book("under the pendulum sun")
        assert book.title == "Under the Pendulum Sun"

    def test_subordinate_conjunction_is_capitalized(self):
        book = Book("because it is bitter, and because it is my heart")
        assert book.title == "Because It Is Bitter, and Because It Is My Heart"

    def test_always_capitalize_i(self):
        book = Book("everything i never told you")
        assert book.title == "Everything I Never Told You"

    def test_can_handle_mixed_case_input(self):
        book = Book("hArRy PoTtEr AnD tHe PhIlOsOpHeR's StOnE")
        assert book.title == "Harry Potter and the Philosopher's Stone"
