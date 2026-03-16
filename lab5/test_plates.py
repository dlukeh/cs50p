from plates import is_valid


def test_length():
    assert is_valid("AA") is True
    assert is_valid("ABCDEF") is True
    assert is_valid("A") is False
    assert is_valid("ABCDEFG") is False


def test_start_condition():
    assert is_valid("AA") is True
    assert is_valid("A1") is False
    assert is_valid("1A") is False
    assert is_valid("11") is False


def test_number_placement():
    assert is_valid("AAA222") is True
    assert is_valid("AAA22A") is False
    assert is_valid("AA22AA") is False


def test_zero_rules():
    assert is_valid("CS50") is True
    assert is_valid("CS05") is False
    assert is_valid("CS500") is True
    assert is_valid("AAA01") is False


def test_punctuation():
    assert is_valid("PI3.14") is False
    assert is_valid("AA!") is False
    assert is_valid("AA 50") is False
