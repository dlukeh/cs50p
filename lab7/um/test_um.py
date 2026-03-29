import pytest
from um import count


def test_single_um():
    assert count("um") == 1
    assert count("Um") == 1
    assert count("UM") == 1
    assert count("um?") == 1
    assert count("um,") == 1
    assert count("um...") == 1


def test_multiple_ums():
    assert count("um um") == 2
    assert count("um, um") == 2
    assert count("um. um!") == 2
    assert count("UM! Um? uM.") == 3
    assert count("um um um") == 3


def test_hyphens_and_underscores():
    assert count("um-um") == 2
    assert count("um_um") == 0
    assert count("um_um um") == 1


def test_false_positives():
    assert count("yummy") == 0
    assert count("album") == 0
    assert count("umbrella") == 0
    assert count("umhello") == 0
    assert count("hello umworld") == 0


def test_mixed_sentences():
    assert count("hello, um, world") == 1
    assert count("um, umhello world um") == 2
