def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if 6 >= len(s) >= 2 and s[:2].isalpha() and s.isalnum():
        str_end = s[2:]
        for char in str_end:
            if char.isdigit():
                i = str_end.index(char)
                if i == 0 and char == '0':
                    # print('Not allowed')
                    return False
                if str_end[i:].isnumeric():
                    return True
                else:
                    return False
            else:
                return True

main()