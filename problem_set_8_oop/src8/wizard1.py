# Demonstrates inheritance [maybe don't add `if` error-checking]


class Wizard:
    def __init__(self, name, patronus):
        if not name:
            raise ValueError("Missing name")
        self.name = name
        self.patronus = patronus

    ...


class Student(Wizard):
    def __init__(self, name, house, patronus):
        super().__init__(name, patronus)
        self.house = house

    ...


class Professor(Wizard):
    def __init__(self, name, subject, patronus):
        super().__init__(name, patronus)
        self.subject = subject

    ...


wizard = Wizard("Albus")
student = Student("Harry", "Gryffindor")
professor = Professor("Severus", "Defence Against the Dark Arts")
...
