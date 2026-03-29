from numb3rs import validate
import pytest


def test_valid():
    assert validate("1.2.3.4")
    assert validate("127.0.0.1")
    assert validate("255.255.255.255")


def test_invalid_format():
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
    assert not validate("256.1.1.1")
    assert not validate("1.256.1.1")
    assert not validate("1.1.256.1")
    assert not validate("1.1.1.256")
    assert not validate("275.3.6.28")


def test_leading_zeros():
    assert not validate("001.002.003.004")
    assert not validate("192.168.001.1")
    assert not validate("00.0.0.0")
