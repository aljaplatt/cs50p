greeting = input("Greeting: ").strip().lower()

print(greeting[:4])

if greeting[0] == 'h':
    if greeting[:5] == 'hello':
        print('$0')
    else:
        print("$20")
else:
    print("$100")