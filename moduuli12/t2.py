import requests as re

API_key = input('Anna API avain: ')
kaupunki = input('Anna paikkakunta: ')


geocode_str = f'http://api.openweathermap.org/geo/1.0/direct?q={kaupunki},FIN&appid={API_key}'

vastaus = re.get(geocode_str)

jsoni = vastaus.json()[0]
lat = jsoni['lat']
lon = jsoni['lon']
weather_str = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&units=metric&lang=fi&appid={API_key}'

saa = re.get(weather_str)

saajsoni = saa.json()
desc = saajsoni['weather'][0]['description']
tempdict = saajsoni['main']
temp = tempdict['temp']
feels_like = tempdict['feels_like']

print(f'Sää paikkakunnalla: {kaupunki}', f'Kuvaus: {desc}', f'Lämpötila: {temp} c, tuntuu kuin: {feels_like} c', sep='\n')