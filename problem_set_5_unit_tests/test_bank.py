from bank import value


def test_hello():
    assert value("hello") == 0

def test_starts_h():
    assert value("hi") == 20

def test_not_h():
    assert value("python") == 100

def test_case():
    assert value("Hython") == 20

