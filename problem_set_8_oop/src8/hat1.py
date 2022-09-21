# Implements sort() with a class method

import random


class Hat:

    houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]

    @classmethod
    def sort(cls, name):
        # print(name, "is in", random.choice(cls.houses))
        return random.choice(cls.houses)


# Hat.sort("Harry")
harry_house = Hat.sort("Harry")
print(harry_house)

#? Why/when choose instance method or class method?  

#* Do you need self, in this case we just need to use this class to perform an action - decide what house harry is in.

#* do not need multiple instance of a class. - here the hat class is perform functionality on data, we do not need to create specialised version for each pupil like in the previous example. 

#*  data or functionality container 

#? why not use a function? - larger files - more organisation needed 