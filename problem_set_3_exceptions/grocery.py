
groceries = {}

while True:
    try:
        item = input().upper()
    except EOFError:
        print()
        break

    # if item is already in grocery, + 1 to its value
    if item in groceries:
        groceries[item] += 1
    else:
        # add it to the list in uppercase and initialise with 1
        groceries[item] = 1

for item in sorted(groceries.keys()):
    print(groceries[item], item)