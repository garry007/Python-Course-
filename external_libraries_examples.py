# Working with External Libraries in Python

# 1. requests (HTTP requests)
# To install: pip install requests
import requests
response = requests.get('https://api.github.com')
print('requests status code:', response.status_code)

# 2. pandas (data analysis)
# To install: pip install pandas
import pandas as pd
data = {'name': ['Alice', 'Bob'], 'age': [25, 30]}
df = pd.DataFrame(data)
print('pandas DataFrame:\n', df)

# 3. numpy (numerical computing)
# To install: pip install numpy
import numpy as np
arr = np.array([1, 2, 3, 4])
print('numpy array:', arr)
print('Mean:', np.mean(arr))

# 4. matplotlib (plotting)
# To install: pip install matplotlib
import matplotlib.pyplot as plt
plt.plot([1, 2, 3], [4, 5, 6])
plt.title('Simple Plot')
plt.xlabel('x')
plt.ylabel('y')
plt.show()
