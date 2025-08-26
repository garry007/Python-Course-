# Standard Libraries & Packages Examples

import math
import datetime
import os
import sys
import random

# math
print("math.sqrt(16):", math.sqrt(16))

# datetime
now = datetime.datetime.now()
print("Current date and time:", now)

# os
print("Current working directory:", os.getcwd())

# sys
print("Python version:", sys.version)

# random
print("Random number between 1 and 10:", random.randint(1, 10))

# Installing and using a package with pip (example: requests)
# To install: pip install requests
# import requests
# response = requests.get('https://api.github.com')
# print(response.status_code)
