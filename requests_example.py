# Example usage of the requests library
import requests

response = requests.get('https://api.github.com')
print('Status Code:', response.status_code)
print('Response JSON:', response.json())
