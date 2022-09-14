def main():
    user_str = input("Input: ")
    print(shorten(user_str))


def shorten(word):
    VOWELS = ("a", 'e', 'i', 'o', 'u')

    new_string = ''
    for letter in word:
        if letter.lower() not in VOWELS:
            new_string += letter

    return new_string


if __name__ == "__main__":
    main()


# user_string = input("Input: ")

# VOWELS = ("a", 'e', 'i', 'o', 'u')

# new_string = ''

# for letter in user_string:
#     if letter.lower() not in VOWELS:
#         new_string += letter

# print(new_string)