# Adds @property for house


class Student:
    def __init__(self, name, house):
        if not name:
            raise ValueError("Invalid name")
        self.name = name
        self.house = house

    def __str__(self):
        return f"{self.name} from {self.house}"
    
    #? a property is an attribute that has greater functionality to increase control  

    #* decorators are functions that modify the behaviour of other functions
    # getter
    # - name the function what you would name the variable
    @property
    def house(self):
        # adding the underscore prevents conflict between variable house and function house naming
        return self._house

    # ^ this allows you to use the decorator @house
    @house.setter
    def house(self, house):
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house")
        self._house = house


def main():
    student = get_student()
    print(student)


def get_student():
    name = input("Name: ")
    house = input("House: ")
    return Student(name, house)


if __name__ == "__main__":
    main()
