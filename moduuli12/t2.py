import requests as re

API_key = ''
kaupunki = input('Anna paikkakunta: ')


geocode_str = f'http://api.openweathermap.org/geo/1.0/direct?q={kaupunki}FIN&appid={API_key}'