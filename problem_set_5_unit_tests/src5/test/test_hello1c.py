from hello1 import hello


def test_default():
    assert hello() == "hello, world"


def test_argument():
    assert hello("David") == "hello, David"


# __init__.py treat the test folder as a package

# pytest test