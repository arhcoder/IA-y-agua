'''from aquacrop.PenmanMonteith import PenmanMonteith
from datetime import datetime

def calcular_et0(t_med, t_min, t_max, viento, humedad, elevacion, latitud, dia_yeard):
    # Convertir latitud a radianes
    lat_rad = latitud * (3.1416/180.0)
    
    # Calcular la hora del amanecer y del atardecer
    phi = lat_rad
    delta = 0.4093 * sin(2 * 3.1416 * dia_yeard / 365 - 1.39)
    omega = acos(-tan(phi) * tan(delta))
    hora_local = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    hora_utc = datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')
    atardecer_utc = (datetime.utcnow() + timedelta(hours=(12 - omega * 180 / 3.1416 / 15))).strftime('%Y-%m-%d %H:%M:%S')
    amanecer_utc = (datetime.utcnow() + timedelta(hours=(-12 + omega * 180 / 3.1416 / 15))).strftime('%Y-%m-%d %H:%M:%S')
    
    # Definir los parámetros del modelo Penman-Monteith
    parametros = {
        "tmean": t_med,
        "tmin": t_min,
        "tmax": t_max,
        "wind": viento,
        "rhmean": humedad,
        "elevation": elevacion,
        "latitude": latitud,
        "solarradiation": None,
        "dayofyear": dia_yeard,
        "atmosphericpressure": None,
        "specificheatair": None,
        "conductance": None,
        "soilheatflux": None,
        "psychrometricconstant": None,
        "slopeofvaporpressurecurve": None,
        "airtemperature": None,
        "windspeed": None,
        "vaporpressure": None,
        "netradiation": None,
        "sunrise": amanecer_utc,
        "sunset": atardecer_utc,
        "timezone": None,
        "datenow": hora_local,
        "dateutc": hora_utc
    }
    
    # Calcular Et0
    et0 = PenmanMonteith(**parametros).calc_et0()
    
    return et0'''