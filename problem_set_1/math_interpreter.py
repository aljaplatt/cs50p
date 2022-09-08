# expression = input('Expression: ')
# digit_1 = float(expression[0])
# operator = expression[2]
# digit_2 = float(expression[4])

# if operator == '+':
#     print(digit_1 + digit_2)
# elif operator == '-':
#     print(digit_1 - digit_2)
# elif operator == '*':
#     print(digit_1 * digit_2)
# elif operator == '/':
#     print(digit_1 / digit_2)

x, y, z = input("Expression: ").split(" ")

# print(x, y, z)

if y == '+':
    print(float(x) + float(z))
elif y == '-':
    print(float(x) - float(z))
elif y == '*':
    print(float(x) * float(z))
elif y == '/':
    print(float(x) / float(z))