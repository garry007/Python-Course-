import requests
import matplotlib.pyplot as plt

# Example public API for demonstration (replace with your own if needed)
url = 'https://jsonplaceholder.typicode.com/users'
response = requests.get(url)
users = response.json()

# Extract names and company names for plotting
names = [user['name'] for user in users]
companies = [user['company']['name'] for user in users]

plt.figure(figsize=(10, 6))
plt.barh(names, range(1, len(names)+1), color='skyblue')
plt.xlabel('User Index')
plt.title('User Names from Network Request')
plt.tight_layout()
plt.show()
