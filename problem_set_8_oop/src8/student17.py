# Removes patronus for simplicy, circumvents error-checking by setting attribute


class Student:
    # invoked when the Student class is called in get student
    def __init__(self, name, house):
        #! the error checking below only occurs during initialisation. Can be circumvented later 
        if not name:
            raise ValueError("Invalid name")
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house")
        self.name = name
        self.house = house

    def __str__(self):
        return f"{self.name} from {self.house}"

# calls get_student 
def main():
    student = get_student()
    #! being able to overwrite or circumvent err checking in init method like below is not good.
    student.house = "Number Four, Privet Drive"
    print(student)

# get student prompts for input then 
def get_student():
    name = input("Name: ")
    house = input("House: ")
    # calls student constructor which automatically invokes the init method - creating the student object in main and printing the __str__ method return value
    return Student(name, house)


if __name__ == "__main__":
    main()
