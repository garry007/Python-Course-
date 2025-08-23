# Functions and Modules Examples

# Function definition and usage
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")

def add(a, b):
    return a + b

result = add(3, 4)
print("Sum:", result)

# Module usage (importing and using a standard library module)
import math
print("Square root of 16:", math.sqrt(16))

# You can also create your own module by saving functions in a .py file and importing them.
# For example, if you have a file mymodule.py with a function foo(), you can use:
# import mymodule
# mymodule.foo()
