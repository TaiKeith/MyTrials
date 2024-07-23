name = input("What's your name?\n")

file = open("names.txt", "a")
file.write(f"{name}\n")
file.close

"""
name = input("What's your name? ")

with open("names.txt", "a") as file:
    file.write(f"{name}\n")
"""
