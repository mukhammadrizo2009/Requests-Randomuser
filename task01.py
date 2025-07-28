import requests
import json

url = 'https://randomuser.me/api/'
response = requests.get(url)

print(response)


