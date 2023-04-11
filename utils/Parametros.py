#!/usr/bin/env python3

import pyowm
import requests

owm = pyowm.OWM('b9abefa7296fdaabc3e0dd9cd5d1765c')

lat = 20.6736
lon = -103.344
date = '2023-04-10'

mgr = owm.weather_manager()
observation = mgr.weather_at_coords(lat, lon)
w = observation.weather
temperature = w.temperature('celsius')
humidity = w.humidity
wind = w.wind()

# Get the elevation data from opentopodata.org
url = f'https://api.opentopodata.org/v1/eudem25m?locations={lat},{lon}'
response = requests.get(url)
elevation = response.json()['results'][0]['elevation']

print('Temperatura:')
print('    Media: ', temperature['temp'])
print('    Minima: ', temperature['temp_min'])
print('    Maxima: ', temperature['temp_max'])

print('Viento:')
print('    Velocidad: ', wind['speed'])
print('    Direccion: ', wind['deg'])

print('Humedad: ', humidity)

print('Elevacion: ', elevation)

print('Latitud: ', lat)

print('Día del año: ', int(date[5:7])*30 + int(date[8:10]))
