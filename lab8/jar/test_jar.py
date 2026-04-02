import pytest
from jar import Jar


def test_init():
    jar = Jar()
    assert jar.capacity == 12
    assert jar.size == 0

    jar = Jar(5)
    assert jar.capacity == 5


def test_invalid_init():
    # We use 'with' to define the scope where the error should happen
    with pytest.raises(ValueError):
        Jar(-1)
    with pytest.raises(ValueError):
        Jar("apple")


def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar(5)
    jar.deposit(3)
    assert jar.size == 3

    # This should trigger our "Too many cookies" ValueError
    with pytest.raises(ValueError):
        jar.deposit(3)

    # This should trigger our "Non-negative" ValueError
    with pytest.raises(ValueError):
        jar.deposit(-1)


def test_withdraw():
    jar = Jar(5)
    jar.deposit(5)
    jar.withdraw(2)
    assert jar.size == 3

    # This should trigger our "Not enough cookies" ValueError
    with pytest.raises(ValueError):
        jar.withdraw(4)

    # This should trigger our "Non-negative" ValueError
    with pytest.raises(ValueError):
        jar.withdraw(-1)
