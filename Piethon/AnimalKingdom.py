class Animal:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def eat(self):
        print(f"{self.name} is eating.")

    def sleep(self):
        print(f"{self.name} is sleeping.")

    def move(self):
        print(f"{self.name} is moving.")

class Mammal(Animal):
    def __init__(self, name, age, gender, milk_production):
        super().__init__(name, age, gender)
        self.milk_production = milk_production

    def eat_plants(self):
        print(f"{self.name} is eating plants.")

    def eat_meat(self):
        print(f"{self.name} is eating meat.")

class Bird(Animal):
    def __init__(self, name, age, gender, flight_speed):
        super().__init__(name, age, gender)
        self.flight_speed = flight_speed

    def fly(self):
        print(f"{self.name} is flying at {self.flight_speed}")

    def build_nest(self):
        print(f"{self.name} is building a nest.")

class Reptile(Animal):
    pass

class Fish(Animal):
    pass

# Creating instances of each animal type
elephant = Mammal("Bambi", 1, "Female", True)
eagle = Bird("Bald", 40, "Male", "65mph")

# Interacting with the animals
elephant.eat_plants()
eagle.fly()

for x in (elephant, eagle):
    print(x.name, x.age, x.gender)
    x.move()
