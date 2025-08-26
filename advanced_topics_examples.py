# Advanced Python Topics Examples

# Generators and Iterators
def count_up_to(n):
    count = 1
    while count <= n:
        yield count
        count += 1

print("Generator output:", list(count_up_to(5)))

# Decorators
def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("Before function call")
        result = func(*args, **kwargs)
        print("After function call")
        return result
    return wrapper

@my_decorator
def say_hello(name):
    print(f"Hello, {name}!")

say_hello("Python")

# Lambda functions
nums = [1, 2, 3, 4]
squares = list(map(lambda x: x**2, nums))
print("Squares with lambda:", squares)

# Context managers (with statement)
with open("temp.txt", "w") as f:
    f.write("Temporary file content.")
with open("temp.txt", "r") as f:
    print("File content with context manager:", f.read())
