import pyowm
import requests
import datetime

owm = pyowm.OWM('b9abefa7296fdaabc3e0dd9cd5d1765c')

lat = 20.6736
lon = -103.344

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

now = datetime.datetime.now()
day_of_year = now.timetuple().tm_yday

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

print('Día del año: ', day_of_year)