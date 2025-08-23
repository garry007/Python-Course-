print("Hello, Python!")

x = 10  # integer
y = 3.14  # float
name = "Alice"  # string
is_active = True  # boolean
print(x, y, name, is_active)

user_input = input("Enter something: ")
print("You entered:", user_input)

a = 5
b = 2
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Integer Division:", a // b)
print("Modulus:", a % b)
print("Exponent:", a ** b)

num = int(input("Enter a number: "))
if num > 0:
    print("Positive")
elif num == 0:
    print("Zero")
else:
    print("Negative")

for i in range(5):
    print("For loop iteration:", i)

count = 0
while count < 3:
    print("While loop count:", count)
    count += 1

fruits = ["apple", "banana", "cherry"]
print(fruits)
print(fruits[0])  # first element
fruits.append("orange")
print(fruits)

point = (2, 3)
print(point)

person = {"name": "Bob", "age": 25}
print(person)
print(person["name"])

def greet(name):
    print(f"Hello, {name}!")

greet("World")

text = "python crash course"
print(text.upper())
print(text.title())
print(text.replace("crash", "quick"))

'''
This is a
multi-line comment
'''

try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")

import math
print(math.sqrt(16))

squares = [x**2 for x in range(5)]
print(squares)

with open("sample.txt", "w") as f:
    f.write("Hello, file!")
with open("sample.txt", "r") as f:
    content = f.read()
    print(content)
