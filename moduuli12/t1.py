import requests as re

vastaus = re.get('https://api.chucknorris.io/jokes/random')
print(vastaus.json()['value'])
