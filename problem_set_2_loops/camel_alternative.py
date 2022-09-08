camel_case = input("camelCase: ")

snake_case = ""

for letter in camel_case:
    # isupper returns true if uppercase.
    if letter.isupper():
        print(letter)
        snake_case = snake_case + "_" + letter.lower()
        print(snake_case)
    else:
        snake_case += letter
        print(snake_case)

print("snake_case: ", snake_case)

