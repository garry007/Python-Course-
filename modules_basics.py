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
