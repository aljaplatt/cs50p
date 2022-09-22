from seasons import minutes_lived

def main():
    test_success_case()
    test_invalid_date()


def test_success_case():
    assert minutes_lived("1983", "09", "03") == "Twenty million, five hundred forty thousand, one hundred sixty minutes"
    assert minutes_lived("1988", "09", "03") == "Seventeen million, nine hundred nine thousand, two hundred eighty minutes"

def test_invalid_date():
    assert minutes_lived("03", "09", "1988") == "Invalid Date"


if __name__ == "__main__":
    main()