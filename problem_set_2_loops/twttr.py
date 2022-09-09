user_string = input("Input: ")

VOWELS = ("a", 'e', 'i', 'o', 'u')

new_string = ''

for letter in user_string:
    if letter.lower() not in VOWELS:
        new_string += letter

print(new_string)