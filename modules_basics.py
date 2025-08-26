# Modules Basics in Python

# Using a standard library module
import math
print("Square root of 25:", math.sqrt(25))

# Importing specific functions from a module
from random import randint
print("Random integer between 1 and 10:", randint(1, 10))

# Creating and using your own module:
# 1. Save a function in a file named mymodule.py:
#    def say_hello():
#        print("Hello from mymodule!")
# 2. In this file, you can import and use it:
# import mymodule
# mymodule.say_hello()

# Example: Defining and using a class in Python (like a module)

class Calculator:
    def __init__(self):
        self.history = []

    def add(self, a, b):
        result = a + b
        self.history.append(f"add({a}, {b}) = {result}")
        return result

    def multiply(self, a, b):
        result = a * b
        self.history.append(f"multiply({a}, {b}) = {result}")
        return result

    def get_history(self):
        return self.history

# Using the Calculator class
calc = Calculator()
print("Add 2 + 3:", calc.add(2, 3))
print("Multiply 4 * 5:", calc.multiply(4, 5))
print("Operation history:", calc.get_history())
