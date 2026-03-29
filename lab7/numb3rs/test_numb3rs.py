import pytest
from numb3rs import validate


def test_valid():
    """Valid IPv4 addresses should return True."""
    assert validate("1.2.3.4")
    assert validate("127.0.0.1")
    assert validate("255.255.255.255")
    assert validate("001.002.003.004")  # leading zeros allowed


def test_invalid_format():
    """Invalid structure or non-numeric parts."""
    assert not validate("1.2.3")
    assert not validate("1.2")
    assert not validate("1")
    assert not validate("1.2.3.4.5")
    assert not validate("1..3.4")
    assert not validate("a.b.c.d")
    assert not validate("")
    assert not validate(".1.2.3")
    assert not validate("1.2.3.")


def test_out_of_range():
    """Octets outside 0–255 should return False."""
    assert not validate("256.1.1.1")
    assert not validate("1.256.1.1")
    assert not validate("1.1.256.1")
    assert not validate("1.1.1.256")
    assert not validate("275.3.6.28")
