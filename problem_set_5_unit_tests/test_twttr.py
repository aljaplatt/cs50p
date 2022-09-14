from twttr import shorten

def test_remove_vowels():
    assert shorten("Hello") == "Hll"
    assert shorten("hEllO") == "hll"
    assert shorten("BMW") == "BMW"