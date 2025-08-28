import json
import matplotlib.pyplot as plt

# Read data from people.json
with open('people.json', 'r') as f:
    people = json.load(f)

names = [person['name'] for person in people]
ages = [person['age'] for person in people]

plt.bar(names, ages, color='skyblue')
plt.title('Ages of People')
plt.xlabel('Name')
plt.ylabel('Age')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()
