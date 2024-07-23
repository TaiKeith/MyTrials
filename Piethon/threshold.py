students = {
        "Alice": 85,
        "Bob": 92,
        "Charlie": 75,
        "Diana": 95,
        "Eve": 88
        }
threshold = 85
passed_students = {name: grade for name, grade in students.items() if grade >= threshold}
print(passed_students)
