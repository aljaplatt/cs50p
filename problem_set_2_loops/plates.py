
def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    split_str = s[:2]

    if 6 >= len(s) >= 2 and split_str.isalpha() and s.isalnum():
        for char in s:
            if char.isdigit():
                i = s.index(char)
                if s[i:].isdigit() and int(char) != 0:
                    return True
                else:
                    return False
        # for loop checks if a string containing digits is valid or not and that's it, so we also have to consider a string with no digits, and that's also a valid plate and the function should return true.
        return True


main()

#! not sure how it checks if first digit is 0 or if nums are in the middle??
