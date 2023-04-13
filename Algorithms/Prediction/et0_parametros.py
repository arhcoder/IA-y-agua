#!/usr/bin/env python3

def obtener_parametros_et0(latitud: float, longitud: float):

    '''
        Recibe:
            - [latitud] (float) de una zona;
            - [longitud] (float) de una zona;
        
        Retorna:
            - "temp_med": float(temperature["temp"]),
            - "temp_min": float(temperature["temp_min"]),
            - "temp_max": float(temperature["temp_max"]),
            - "viento_vel": float(wind["speed"]),
            - "direction": float(wind["deg"]),
            - "humedad": float(humidity),
            - "elevacion": 150,
            - "dia_anio": int(day_of_year)
            En un formato de MAPA;

            Utiliza una API de datos meteorológicos:
            librería "pyowm";
    '''

    import pyowm
    import requests
    import datetime

    '''
        ! LLAVE EXPUESTA !
        ESTO ES SÓLO PARA EL DESARROLLO DEL PROTOTIPO;
        PARA LA VERSIÓN DE PRUDICCÓN SE REFACTORIZARÁ.
    '''
    owm = pyowm.OWM("b9abefa7296fdaabc3e0dd9cd5d1765c")

    # Ejemplo de Guadalajara #
    # latitud = 20.6736
    # longitud = -103.344

    mgr = owm.weather_manager()
    observation = mgr.weather_at_coords(latitud, longitud)
    w = observation.weather
    temperature = w.temperature("celsius")
    humidity = w.humidity
    wind = w.wind()

    # Get the elevation data from opentopodata.org
    url = f"https://api.opentopodata.org/v1/eudem25m?locations={latitud},{longitud}"
    response = requests.get(url)
    elevation = response.json()["results"][0]["elevation"]

    now = datetime.datetime.now()
    day_of_year = now.timetuple().tm_yday

    # print("Temperatura:")
    # print("    Media: ", temperature["temp"])
    # print("    Minima: ", temperature["temp_min"])
    # print("    Maxima: ", temperature["temp_max"])
    # print("Viento:")
    # print("    Velocidad: ", wind["speed"])
    # print("    Direccion: ", wind["deg"])
    # print("Humedad: ", humidity)
    # print("Elevacion: ", elevation)
    # print("Latitud: ", latitud)
    # print("Día del año: ", day_of_year)

    data = {
        "temp_med": float(temperature["temp"]),
        "temp_min": float(temperature["temp_min"]),
        "temp_max": float(temperature["temp_max"]),
        "viento_vel": float(wind["speed"]),
        "direction": float(wind["deg"]),
        "humedad": float(humidity),
        "elevacion": 150,
        "dia_anio": int(day_of_year)
    }

    return data

# Ejemplo de coordenadas de Jalisco:
# print(obtener_parametros_et0(20.6736, -103.344))