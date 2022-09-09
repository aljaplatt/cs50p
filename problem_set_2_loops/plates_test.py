#* “All vanity plates must start with at least two letters.”
#? maximum of 6 characters (letters or numbers) and a minimum of 2 characters.”
#* “Numbers must come at the end. For example, AAA222 ok, AAA22A no. The first number used cannot be a ‘0’.”
#? “No periods, spaces, or punctuation marks are allowed.”

def main():
    plate = input("Plate: ")
    if check_len(plate):
        print("valid length")
        if check_isalnum(plate):
            print("valid char")
            if check_first_two_char(plate):
                print('Starts with letters')
                if check_char_order(plate):
                    print('orderrrrr')
    else:
        print('Invalid')


def check_len(plate):
    print(len(plate))
    if 6 >= len(plate) >= 2:
        return True

def check_isalnum(plate):
    if plate.isalnum():
        return True

def check_first_two_char(plate):
    print(plate[:2])
    if plate[:2].isalpha():
        return True

# def check_char_order(plate):
#     if plate[2] != '0':
#         check_str = plate[2:]
#         if char_str[0].isnumeric():


        # print(plate[2:])
        # if plate[2].isnumeric() and plate[-1]

# main()


def main():
    plate = input("Plate: ")
    if not plate.isalnum() or (len(plate) < 2 or len(plate) > 6):
        print("Invalid")
        return False

    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if   s.isalpha() or s[:2].isalpha() and s[-2:].isnumeric() and s[-2:][0] != "0":
        return True
    else:
        return False
main()