# Demonstrates indexing into a dict

students = {
    "Hermione": "Gryffindor",
    "Harry": "Gryffindor",
    "Ron": "Gryffindor",
    "Draco": "Slytherin",
}

print(students["Hermione"])
print(students["Harry"])
print(students["Ron"])
print(students["Draco"])

'''
Gryffindor
Gryffindor
Gryffindor
Slytherin
'''
#* for loop like this, will print out keys
for student in students: 
    print(student)

'''
Hermione
Harry
Ron
Draco
'''

#* to print both
for student in students: 
    # print(student, students[student])
    print(student, students[student], sep=", ")

'''
Hermione Gryffindor
Harry Gryffindor
Ron Gryffindor
Draco Slytherin
'''