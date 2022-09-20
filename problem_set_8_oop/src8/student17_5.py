class Student:
    def __init__(self, name, house) -> None:
        if not name:
            raise ValueError("Missing name")
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid House")
        self.name = name
        self.house = house

    # turns the student object into a printable string
    def __str__(self):
        return f"{self.name} from {self.house}"


def main():
    # call get_student and store return value in student variable
    student = get_student()
    print(student)


def get_student():
    name = input("Name: ")
    house = input("House: ")
    return Student(name, house)