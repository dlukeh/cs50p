from twttr import shorten


def test_removes_lowercase_vowels():
    assert shorten("twitter") == "twttr"
    assert shorten("aeiou") == ""


def test_removes_uppercase_vowels():
    assert shorten("AEIOU") == ""
    assert shorten("TWITTER") == "TWTTR"


def test_mixed_case():
    assert shorten("TwItTeR") == "TwtTR"  # vowels removed, remaining letters keep case


def test_numbers_unchanged():
    assert shorten("cs50") == "cs50"
    assert shorten("h3ll0") == "h3ll0"


def test_punctuation_unchanged():
    assert shorten("hello, world!") == "hll, wrld!"
    assert shorten("what's up?") == "wht's p?"


def test_empty_string():
    assert shorten("") == ""


def test_no_vowels_unchanged():
    assert shorten("rhythm") == "rhythm"
    assert shorten("CRYPT") == "CRYPT"
