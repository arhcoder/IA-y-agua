# Import Meteostat library and dependencies
from datetime import datetime
import matplotlib.pyplot as plt
from meteostat import Stations, Daily, Point


# Set time period
start = datetime(2023, 4, 4)
end = datetime(2023, 4, 4)

Aguascalientes = Point(49.2497, -123.1193, 70)

# Get daily data
data = Daily('10637', start, end)
data = data.fetch()

'''
# Plot line chart including average, minimum and maximum temperature
data.plot(y=['tavg', 'tmin', 'tmax'])
plt.show()
'''

print(data)
#print(data["tavg"])