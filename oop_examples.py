# Object-Oriented Programming (OOP) Examples in Python

# 1. Classes and Objects
class Animal:
    def __init__(self, name):
        self.name = name  # Attribute
    def speak(self):
        print(f"{self.name} makes a sound.")

# Creating an object
animal = Animal("Generic Animal")
animal.speak()

# 2. Attributes and Methods
class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed  # Additional attribute
    def speak(self):
        print(f"{self.name} barks. Breed: {self.breed}")

dog = Dog("Buddy", "Golden Retriever")
dog.speak()
print("Dog's name:", dog.name)
print("Dog's breed:", dog.breed)

# 3. Inheritance and Polymorphism
class Cat(Animal):
    def speak(self):
        print(f"{self.name} meows.")

animals = [Dog("Max", "Beagle"), Cat("Whiskers"), Animal("Creature")]
for a in animals:
    a.speak()  # Polymorphism: each class has its own speak()
