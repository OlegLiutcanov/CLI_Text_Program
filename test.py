# test_core.py
from core import reverse_text, is_palindrome, count_vowels, word_count, slugify


def test_reverse_text_edge_cases():
    assert reverse_text("Abc!") == "!cbA"
    assert reverse_text("") == ""


def test_is_palindrome_rich_cases():
    assert is_palindrome("Race car!") is True
    assert is_palindrome("No lemon, no melon") is True
    assert is_palindrome("") is True
    assert is_palindrome("hello") is False


def test_count_vowels_cases():
    assert count_vowels("Queueing") == 5
    assert count_vowels("rhythm") == 0
    assert count_vowels("") == 0


def test_word_count_extra_whitespace():
    assert word_count("  one  two\nthree\tfour  ") == 4
    assert word_count("") == 0
    assert word_count("   \n\t  ") == 0


def test_slugify():
    assert slugify("Hello, World!") == "hello-world"
    assert slugify("  Multiple   spaces__here  ") == "multiple-spaceshere"
    assert slugify("A---B") == "a-b"
    assert slugify("") == ""
    # accented letters get stripped under our simple rules:
    assert slugify("Café Déjà Vu") == "caf-dj-vu"
