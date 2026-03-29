import pytest
from working import convert


def test_incorrect_format():
    with pytest.raises(ValueError):
        convert("09:00 AM - 05:00 PM")  # wrong separator
    with pytest.raises(ValueError):
        convert("9:00AM to 5:00PM")  # missing spaces
    with pytest.raises(ValueError):
        convert("hello world")  # nonsense input


def test_incorrect_hours():
    with pytest.raises(ValueError):
        convert("0:00 AM to 5:00 PM")
    with pytest.raises(ValueError):
        convert("13:00 PM to 5:00 PM")
    with pytest.raises(ValueError):
        convert("9:00 AM to 0:00 PM")
    with pytest.raises(ValueError):
        convert("9:00 AM to 13:00 PM")


def test_incorrect_minutes():
    with pytest.raises(ValueError):
        convert("9:60 AM to 5:00 PM")
    with pytest.raises(ValueError):
        convert("9:00 AM to 5:60 PM")


def test_correct_format():
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("12:30 PM to 1:45 PM") == "12:30 to 13:45"
    assert convert("11:59 PM to 12:01 AM") == "23:59 to 00:01"
