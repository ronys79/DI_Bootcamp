import requests 

request_url = 'http://api.chucknorris.io/jokes/random'

response = requests.get(request_url)

# print(response.json())[]

if response.status_code == 200:
    