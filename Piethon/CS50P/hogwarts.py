"""
students = ["Harry", "Hermione", "Ron"]

for i in range(len(students)):
    print(i + 1, students[i])

for student in students:
    print(student)
"""

students = {
        "Harry": "Gryffindor",
        "Hermione": "Gryffindor",
        "Ron": "Gryffindor",
        "Draco": "Slytherin",
        }

for student in students:
    print(student, students[student], sep=": ")
