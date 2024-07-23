while True:
    try:
        x = int(input("What's x? "))
    except ValueError:
        print("That isn't an integer. Please input an integer")
    else:
        break

print(f"x is {x}")
