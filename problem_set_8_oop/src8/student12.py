# Adds validation in __init__ using raise


class Student:
    def __init__(self, name, house):
        if not name:
            raise ValueError("Missing name")
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house")
        self.name = name
        self.house = house


def main():
    student = get_student()
    print(f"{student.name} from {student.house}")


def get_student():
    while True:
        name = input("Name: ")
        house = input("House: ")
        try:
            return Student(name, house)
        except ValueError:
            print("Invalid data")
            continue



if __name__ == "__main__":
    main()
