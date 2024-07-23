"""
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    def move(self):
        print("Drive!")

class Boat:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    def move(self):
        print("Sail!")

class Plane:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    def move(self):
        print("Fly!")

mycar = Car("AUDI", "RS7")
myboat = Boat("Ibiza", "Touring 20")
myplane  = Plane("Boeing", "747")

for x in (mycar, myboat, myplane):
    x.move()
"""

"""Inheritance Class Polymorphism"""

class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    def move(self):
        print("Move!")

class Car(Vehicle):
    def move(self):
        print("Drive!")

class Boat(Vehicle):
    def move(self):
        print("Sail!")

class Plane(Vehicle):
    def move(self):
        print("Fly!")

mycar = Car("AUDI", "RS7")
myboat = Boat("Ibiza", "Touring 20")
myplane = Plane("Boeing", "747")

for x in (mycar, myboat, myplane):
    print(x.brand, x.model)
    x.move()
