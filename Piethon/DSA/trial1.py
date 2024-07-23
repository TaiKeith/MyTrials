info = {}

with open("Trial.csv", "r") as file:
    for line in file:
        tokens = line.split(",")
        name = tokens[0]
        age = tokens[1]
        info[name] = age

print(info)
