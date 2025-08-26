# String Manipulation Examples

text = "  Hello, Python World!  "
print("Original:", repr(text))

# Strip whitespace
print("Stripped:", text.strip())

# Change case
print("Uppercase:", text.upper())
print("Lowercase:", text.lower())
print("Title case:", text.title())

# Replace
print("Replace 'Python' with 'Programming':", text.replace("Python", "Programming"))

# Split and join
words = text.strip().split()
print("Split into words:", words)
joined = "-".join(words)
print("Joined with hyphens:", joined)
