from seasons import get_date, format_words
from datetime import date
import pytest


def test_get_date():
    # Test a valid ISO date
    assert get_date("1999-01-01") == date(1999, 1, 1)
    assert get_date("1961-11-12") == date(1961, 11, 12)


def test_format_words():
    # Test a common year (365 days * 24 * 60 = 525600)
    # Note: Check if your version of inflect adds a comma!
    # If check50 fails, adjust the comma in the string below.
    assert (
        format_words(525600) == "Five hundred twenty-five thousand, six hundred minutes"
    )

    # Test a smaller number
    assert (
        format_words(1) == "One minutes"
    )  # (Note: The lab usually wants 'minutes' plural even for 1)


def test_invalid_date():
    # This is how we test if a function exits or raises an error
    with pytest.raises(SystemExit):
        get_date("January 1st, 1999")
    with pytest.raises(SystemExit):
        get_date("1999-13-32")  # Invalid month/day
