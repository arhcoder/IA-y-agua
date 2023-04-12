import math

def obtener_et0(t_max, t_min, wind_speed, humidity, solar_rad, elev):
    """
    Calculate the reference evapotranspiration (ETo) using the Penman-Monteith equation.
    Parameters:
    t_max (float): Maximum temperature in degrees Celsius
    t_min (float): Minimum temperature in degrees Celsius
    wind_speed (float): Wind speed at 2 meters above the ground in meters per second
    humidity (float): Average relative humidity as a percentage
    solar_rad (float): Total incoming solar radiation in megajoules per square meter per day
    elev (float): Elevation in meters
    lat (float): Latitude in degrees
    doy (int): Day of the year (1-365)
    Returns:
    float: Reference evapotranspiration (ETo) in millimeters per day
    """
  
    # Calcular la presion atmos del mar
    P = (101.3 * ((293 - 0.0065 * elev) / 293) ** 5.26)
    # print(P)


    delta = (4098 * (0.6108 * math.exp((17.27 * t_max) / (t_max + 237.3)) - 0.6108 * math.exp((17.27 * t_min) / (t_min + 237.3)))) / ((t_max - t_min) + 237.3) ** 2
    gamma = 0.665e-3 * P  # aquí se asume que la presión atmosférica es 101.3 kPa
    psy = 0.00163 * (P/ (0.622 * 2.45))# aquí se asume que la presión atmosférica es 101.3 kPa

    ETo = 0.408 * delta * (solar_rad / 25.0) + gamma * ((900 / (t_max + 273)) * wind_speed * (delta + psy * (1 + 0.34 * wind_speed)))+ gamma * 0.34 * (1 - (humidity / 100)) * math.sqrt(elev) * delta

    #print('ETo:', round((ETo*10), 2), 'mm/día')

    return ETo


# Test the function with some sample parameters
t_max = 35  # degrees Celsius
t_min = 20  # degrees Celsius
wind_speed = 2.5  # meters per second
humidity = 60  # percentage
solar_rad = 25  # megajoules per square meter per day
elev = 500
lat = 20
doy = 150

# eto = calculate_eto(t_max, t_min, wind_speed, humidity, solar_rad, elev, lat, doy)
# print("ETo: ", eto, "mm/day")