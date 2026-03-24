from numb3rs import validate


def test_valid():
    assert validate("1.2.3.4") == True
    assert validate("127.0.0.1") == True
    assert validate("255.255.255.255") == True
    assert validate("001.002.003.004") == True  # leading zeros allowed


def test_invalid_format():
    assert validate("1.2.3") == False
    assert validate("1.2") == False
    assert validate("1") == False
    assert validate("1.2.3.4.5") == False
    assert validate("1..3.4") == False
    assert validate("a.b.c.d") == False
    assert validate("") == False


def test_out_of_range():
    assert validate("256.1.1.1") == False
    assert validate("1.256.1.1") == False
    assert validate("1.1.256.1") == False
    assert validate("1.1.1.256") == False
    assert validate("275.3.6.28") == False
