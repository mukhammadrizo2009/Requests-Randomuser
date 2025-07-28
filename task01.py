import requests
import json

url = 'https://randomuser.me/api/'
response = requests.get(url)

data = response.json()

user = {
    "first_name": data['results'][0]['name']['first'],
    "last_name": data['results'][0]['name']['last'],
    "gender": data['results'][0]['gender'],
    "phone": data['results'][0]['phone'],
    "address": {
        "street_name": data['results'][0]['location']['street']['name'],
        "city": data['results'][0]['location']['city'],
        "country": data['results'][0]['location']['country'],
    }
}

with open("user.json" , 'w') as jsonfile:
    json.dump(user, jsonfile , indent=4)

