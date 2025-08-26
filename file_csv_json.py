# Working with CSV and JSON in Python
import csv
import json

# Writing to a CSV file
rows = [
    ["name", "age"],
    ["Alice", 25],
    ["Bob", 30]
]
with open("people.csv", "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(rows)

# Reading from a CSV file
with open("people.csv", "r") as csvfile:
    reader = csv.reader(csvfile)
    print("CSV content:")
    for row in reader:
        print(row)

# Writing to a JSON file
data = {"name": "Alice", "age": 25, "city": "New York"}
with open("person.json", "w") as jsonfile:
    json.dump(data, jsonfile)

# Reading from a JSON file
with open("person.json", "r") as jsonfile:
    loaded = json.load(jsonfile)
    print("JSON content:")
    print(loaded)
