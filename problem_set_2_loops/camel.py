# variable_name = list(input("Please input a variable name: "))


# print(list(variable_name))
# print(variable_name)

# for letter in variable_name:
#     if letter == letter.upper():
#         print(letter)

# print(variable_name)

# letter_list = variable_name.split('')
# print(letter_list)

#* 1
# letter = [x for x in variable_name]
# print(letter)

# #* 2

# letters = [*variable_name]
# print(letters)

# #* 3

# lst = []

# for letter in variable_name:
#     lst.append(letter)

# print(lst)

# variable_name = list(input("Please input a variable name: "))
# print(variable_name)


# for letter, value in enumerate(variable_name):
#     if letter == str(letter.upper()):
#         print(letter, value)




camelCase = input("camelCase: ")

snake_case = ""

# loops the length of the string held in camelCase
# and prints char 
# for i in range(len(camelCase)):
#     print(camelCase[i])

for i in range(len(camelCase)):
    if camelCase[i].isupper():
        snake_case = snake_case + "_" + camelCase[i].lower()
    else:
        snake_case += camelCase[i]

print("snake_case: ", snake_case)

'''
i am using that logic to get the content stored in the snake_case variable, otherwise I will be overwriting the previous content every time that line evaluates.
so for example if snake_case = 'hello", if I want to add "world" to this variable I will need to write this snake_case = snake_case + "world" or snake_case += "world", and now snake_case = "helloworld".
but if I write snake_case = "world", I will overwrite the past content and snake_case will now be = "world".
i would really recommend to try putting ur line of code instead of mine and see the difference.
'''

variable_name = input("Please input a variable name: ")

snake_case = ""

for letter in range(len(variable_name)):
    if variable_name[letter].isupper():
        snake_case = snake_case + "_" + variable_name[letter].lower()
    else:
        snake_case += variable_name[letter]

print("snake_case: ", snake_case)