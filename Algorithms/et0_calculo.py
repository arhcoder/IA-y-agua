import math

def calculate_eto(t_max, t_min, wind_speed, humidity, solar_rad, elev, lat, doy):
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
    # Calculate the slope of the saturation vapor pressure curve
    delta = 4098 * (0.6108 * math.exp((17.27 * t_max) / (t_max + 237.3))) / ((t_max + 237.3) ** 2)

    # Calculate the atmospheric pressure
    pressure = 101.3 * ((293 - 0.0065 * elev) / 293) ** 5.26

    # Calculate the psychrometric constant
    gamma = 0.000665 * pressure

    # Calculate the extraterrestrial radiation
    dr = 1 + 0.033 * math.cos((2 * math.pi / 365) * doy)
    phi = math.radians(lat)
    ra = (24 * 60 / math.pi) * 0.0820 * dr * (
        math.acos(-math.tan(phi) * math.tan(0.4093 * math.sin((2 * math.pi / 365) * doy + 1.39))))

    # Calculate the net shortwave radiation
    albedo = 0.23
    rn = (1 - albedo) * solar_rad

    # Calculate the net longwave radiation
    es_max = 0.6108 * math.exp((17.27 * t_max) / (t_max + 237.3))
    es_min = 0.6108 * math.exp((17.27 * t_min) / (t_min + 237.3))
    ea = es_min * humidity / 100
    delta_temp = t_max - t_min
    sigma = 4.903e-9  # Stefan-Boltzmann constant in MJ/K4/m2/d
    r_nl = sigma * ((es_max + es_min) / 2) ** 4 * (0.34 - 0.14 * math.sqrt(ea)) * ((1.35 * rn / solar_rad) - 0.35)

    # Calculate the reference evapotranspiration
    eto = (0.408 * delta * (rn - r_nl) + gamma * 900 / (t_max + 273) * wind_speed * (es_max - ea)) / (
                delta + gamma * (1 + 0.34 * wind_speed))

    return eto


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