from bank import value


def test_hello():
    assert value("hello") == 0
    assert value("Hello") == 0
    assert value("HELLO there ") == 0


def test_h_but_not_hello():
    assert value("hi") == 20
    assert value("Hey") == 20
    assert value("Hola ") == 20


def test_otherwise():
    assert value("what's up?") == 100
    assert value("good morning") == 100
    assert value("123hello") == 100


def test_edge_cases():
    assert value("h") == 20
    assert value("hello!") == 0
    assert value("hELLO") == 0
    assert value("H") == 20
