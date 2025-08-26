# List Comprehensions Examples

# Basic list comprehension
squares = [x**2 for x in range(1, 6)]
print("Squares:", squares)

# List comprehension with condition
even_squares = [x**2 for x in range(1, 11) if x % 2 == 0]
print("Even squares:", even_squares)

# Nested list comprehension
matrix = [[1, 2, 3], [4, 5, 6]]
flattened = [num for row in matrix for num in row]
print("Flattened matrix:", flattened)
