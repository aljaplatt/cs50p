name_list = []

while True:
    try:
        name = input("Name: ")
        name_list.append(name)
    except EOFError:
        print()
        break

# print(str(name_list))
name_str = ''
for name in name_list:
    if name == name_list[-1] and len(name_list) > 1:
        name_str += f"and {name}"
    # elif name == name_list[-1] and len(name_list) == 2:
    #     name_str += f" and {name}"
    elif name == name_list[0] and len(name_list) == 1:
        name_str += f"Adieu, adieu, to {name}"
    elif name == name_list[0] and len(name_list) == 2:
        name_str += f"Adieu, adieu, to {name} "
    elif name == name_list[0]:
        name_str += f"Adieu, adieu, to {name}, "
    else:
        name_str += f"{name}, "

print(name_str)
