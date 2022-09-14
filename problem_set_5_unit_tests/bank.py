def main():
    greeting = input("Greeting: ").strip().lower()
    val = value(greeting)
    print(f"${val}")

def value(greeting):
    if greeting[0] == 'h':
        if greeting[:5] == 'hello':
            return 0
        else:
            return 20
    else:
        return 100

if __name__ == "__main__":
    main()