import csv

name = input("What is your name? ")
home = input("Where are you from? ")

with open("stu_dents.csv", "a") as file:
    writer = csv.writer(file)
    writer.writerow([name, home])
