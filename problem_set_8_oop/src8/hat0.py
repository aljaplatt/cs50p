# Implements sort() with an instance method

import random


# class Hat:
#     def __init__(self):
#         self.houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]

#     def sort(self, name):
#         print(name, "is in", random.choice(self.houses))


# alex_hat = Hat()
# harry_hat = Hat()
# harry_hat.sort("Harry")
# alex_hat.sort("Alex")
class Hat:
    def __init__(self, name):
        self.houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]
        self.name = name

    def sort(self):
        print(self.name, "is in", random.choice(self.houses))


alex_hat = Hat("Alex")
harry_hat = Hat("Harry")
harry_hat.sort()
alex_hat.sort()
