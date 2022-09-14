from plates import is_valid


def test_is_valid():
    assert is_valid("cs50") == True


def test_starts_with():
    assert is_valid("2A") == False
    assert is_valid("A2") == False
    assert is_valid("AA") == True


def test_length():
    assert is_valid("c") == False
    assert is_valid("cs50545445") == False

def test_all_num():
    assert is_valid("50545445") == False


def test_placement():
    assert is_valid("AAA222") == True
    assert is_valid("cs05") == False
    assert is_valid("cs50p") == False

def test_punctuation():
    assert is_valid("PI3.14") == False