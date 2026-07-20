# Define a class
class Dog:
    species = "Canine"   # Class attribute (shared by all dogs)

    def __init__(self, name, age):
        self.name = name   # Instance attribute
        self.age = age     # Instance attribute

    def bark(self):
        return f"{self.name} says Woof!"

# Create objects (instances of Dog)
dog1 = Dog("Buddy", 3)
dog2 = Dog("Lucy", 5)

print(dog1.bark())   # Buddy says Woof!
print("Dog1's species:", dog1.species)  # Dog1's species: Canine
print(dog2.bark())   # Lucy says Woof!
print("Dog2's species:", dog2.species)  # Dog2's species: Canine