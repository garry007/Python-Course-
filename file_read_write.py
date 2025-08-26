# Reading and Writing Files in Python

# Writing to a file
with open("example.txt", "w") as f:
    f.write("Hello, file!\n")
    f.write("This is a new line.\n")

# Reading from a file
with open("example.txt", "r") as f:
    content = f.read()
    print("File content:")
    print(content)
