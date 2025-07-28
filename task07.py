import requests

url = 'https://randomuser.me/api/'

payload = {
    'results': 5
}

response = requests.get(url , params=payload)

results = response.json()['results']
for i, user in enumerate(results, start=1):
    image_url = user['picture']['large']
    
    r = requests.get(image_url)
    with open(f'images/user{i}.jpg', 'wb') as f:
        f.write(r.content)