variable_name = input("Please input a variable name: ")

snake_case = ""

for letter in range(len(variable_name)):
    if variable_name[letter].isupper():
        snake_case = snake_case + "_" + variable_name[letter].lower()
    else:
        snake_case += variable_name[letter]

print("snake_case: ", snake_case)