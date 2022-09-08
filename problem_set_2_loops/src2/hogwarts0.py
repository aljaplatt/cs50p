# Demonstrates indexing into a list

students = ["Hermione", "Harry", "Ron"]

# print(students[0])
# print(students[1])
# print(students[2])
# print(students[-1])

#* 1  
for index in range(len(students)):
    print(index) # 0,1,2

#* 2
for index in range(1, len(students) + 1):
    print(index) # 1,2,3

#* 3
for i in range(len(students)):
    print('STUDENTS[I]: ', students[i])

'''
Hermione
Harry
Ron
'''

#* 4
for i in range(len(students)):
    print('STUDENTS[I]: ', i + 1, students[i])

'''
1 Hermione
2 Harry
3 Ron
'''

#* 5
for student in students:
    print(student)

'''
Hermione
Harry
Ron
'''
