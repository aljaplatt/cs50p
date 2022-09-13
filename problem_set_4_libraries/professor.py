import random
import sys


def main():
    # level = get_level()
    questions = 10
    score = 0
    while questions:
        attempts = 3
        num1 = generate_integer(get_level())
        num2 = generate_integer(get_level())
        answer = num1 + num2

        while attempts:
            try:
                user_answer = int(input(f"{num1} + {num2} = "))
            except ValueError:
                print("EEE")
                if attempts == 1:
                    print(f"{num1} + {num2} = {answer}")
                    attempts -=1
                    break
                else:
                    attempts -=1
                    continue
            else:
                if user_answer != answer:
                    print("EEE")
                    if attempts == 1:
                        print(f"{num1} + {num2} = {answer}")
                        attempts -=1
                        break
                    else:
                        attempts -=1
                        continue
                else:
                    score += 1
                    break

        questions -= 1
        if not questions:
            print(f"Score: {score}")


def get_level():
    i = 3
    while i > 0:
        try:
            level = int(input("Level: "))
        except ValueError:
            print("Enter a number between 1-3")
            pass
        except EOFError as e:
            sys.exit(0)
        else:
            if level in [1,2,3]:
                return level
            else:
                print("Enter a number between 1-3")
                i -= 1
                continue


def generate_integer(level):
    try:
        if level in [1,2,3]:
            match level:
                case 1:
                    return random.randint(0,9)
            match level:
                case 2:
                    return random.randint(10,99)
            match level:
                case 3:
                    return random.randint(100,999)
    except ValueError:
        print("Invalid input")
        sys.exit(1)


if __name__ == "__main__":
    main()