print("Hello, Python!")

x = 10  # integer
y = 3.14  # float
name = "Alice"  # string
is_active = True  # boolean
print(x, y, name, is_active)

user_input = input("Enter something: ")
print("You entered:", user_input)




# 7. Lists
fruits = ["apple", "banana", "cherry"]
print(fruits)
print(fruits[0])  # first element
fruits.append("orange")
print(fruits)




import math
print(math.sqrt(16))

squares = [x**2 for x in range(5)]
print(squares)

with open("sample.txt", "w") as f:
    f.write("HelloHelloHelloHelloHello, file!")
with open("sample.txt", "r") as f:
    content = f.read()
    print(content)
