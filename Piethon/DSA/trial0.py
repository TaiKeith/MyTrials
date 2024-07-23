import csv

i = 0
while i < 3:
    name = input("Name: ")
    age = int(input("Age: "))

    with open("Trial.csv", "a") as file:
        writer = csv.DictWriter(file, fieldnames=["Name", "Age"])
        writer.writerow({"Name": name, "Age": age})
    i += 1
