# Error Handling Examples in Python

# Basic try-except
try:
    x = 10 / 0
except ZeroDivisionError as e:
    print("Caught an exception:", e)

# try-except-finally
try:
    f = open("nonexistent.txt", "r")
except FileNotFoundError:
    print("File not found!")
finally:
    print("This always runs, even if there was an error.")

# Raising your own exception
def divide(a, b):
    if b == 0:
        raise ValueError("b cannot be zero!")
    return a / b

try:
    result = divide(5, 0)
except ValueError as err:
    print("Custom exception caught:", err)
