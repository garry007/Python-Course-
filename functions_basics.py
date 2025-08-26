# Function Basics in Python

def greet(name):
    print(f"Hello, {name}!")

greet("Alice")

def add(a, b):
    return a + b

result = add(5, 7)
print("Sum:", result)

# Function with default argument
def power(base, exponent=2):
    return base ** exponent

print("Power (default exponent):", power(3))
print("Power (custom exponent):", power(3, 3))

# Complex function: Calculate statistics for a list of numbers
def calculate_stats(numbers):
    if not numbers:
        return None
    total = sum(numbers)
    count = len(numbers)
    mean = total / count
    minimum = min(numbers)
    maximum = max(numbers)
    # Calculate median
    sorted_nums = sorted(numbers)
    mid = count // 2
    if count % 2 == 0:
        median = (sorted_nums[mid - 1] + sorted_nums[mid]) / 2
    else:
        median = sorted_nums[mid]
    return {
        'sum': total,
        'count': count,
        'mean': mean,
        'min': minimum,
        'max': maximum,
        'median': median
    }

# Example usage
nums = [3, 7, 2, 9, 4]
stats = calculate_stats(nums)
print("Statistics:", stats)

# Advanced function: Filter, transform, and summarize data

def process_numbers(numbers, threshold=5):
    """
    Filters numbers greater than threshold, squares them,
    and returns a summary with the processed list and their average.
    """
    # Filter numbers greater than threshold
    filtered = list(filter(lambda x: x > threshold, numbers))
    # Square each filtered number
    squared = [x**2 for x in filtered]
    # Calculate average if list is not empty
    avg = sum(squared) / len(squared) if squared else 0
    return {
        'original': numbers,
        'filtered': filtered,
        'squared': squared,
        'average': avg
    }

# Example usage
nums2 = [1, 4, 6, 8, 3, 10]
result = process_numbers(nums2, threshold=5)
print("Advanced processing:", result)
