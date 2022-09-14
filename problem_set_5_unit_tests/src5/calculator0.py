# Demonstrates defining a function with a return value


def main():
    x = int(input("What's x? "))
    print("x squared is", square(x))


def square(n):
    return n * n


#  if were importing square from another file - you wouldn't want to trigger the main function in this module
if __name__ == "__main__":
    main()

#! cannot handles floats
