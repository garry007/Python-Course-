# Program 1: Add two numbers
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
sum = num1 + num2
print(f"Sum: {sum}")

# Program 2: Check even or odd
number = int(input("Enter a number to check even or odd: "))
if number % 2 == 0:
    print("Even number")
else:
    print("Odd number")

# Program 3: Print a list of numbers
numbers = [1, 2, 3, 4, 5]
print("List of numbers:", numbers)

# Program 4: Simple for loop
for i in range(5):
    print(f"Loop iteration: {i}")

# Program 5: String manipulation
name = input("Enter your name: ")
print(f"Hello, {name.upper()}! Your name has {len(name)} letters.")
