import pytest
from fuel import convert, gauge

# --- Tests for convert() ---


def test_convert_valid():
    assert convert("3/4") == 75
    assert convert("1/2") == 50
    assert convert("1/1") == 100
    assert convert("0/1") == 0


def test_convert_errors():
    with pytest.raises(ValueError):
        convert("cat/dog")
    with pytest.raises(ValueError):
        convert("2/1")
    with pytest.raises(ZeroDivisionError):
        convert("1/0")
    with pytest.raises(ValueError):
        convert("-1/3")
    with pytest.raises(ValueError):
        convert("3/-3")


# --- Tests for gauge() ---
def test_gauge_E():
    assert gauge(0) == "E"
    assert gauge(1) == "E"


def test_gauge_F():
    assert gauge(99) == "F"
    assert gauge(100) == "F"


def test_gauge_middle():
    assert gauge(50) == "50%"
    assert gauge(75) == "75%"
