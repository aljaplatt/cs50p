# Moves get_student into Student class


class Student:
    def __init__(self, name, house):
        self.name = name
        self.house = house

    def __str__(self):
        return f"{self.name} from {self.house}"

    # class method - I can call this method without instantiating a student object first - do not need an existing student.
    @classmethod
    def get(cls):
        name = input("Name: ")
        house = input("House: ")
        # create an object of the current class - whatever cls is - in this case Student
        return cls(name, house)

# ====================================================
# Above is all student functionality abstracted/ encapsulated into a class 
# ====================================================

def main():
    # 
    student = Student.get()
    print(student)


if __name__ == "__main__":
    main()
