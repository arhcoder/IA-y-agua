import math

def obtener_et0(t_max: float, t_min: float, velocidad_viento: float, humedad: float, radia_solar: float, elevacion: float):

    '''
        Recibe:
            - t_med (float): temperatura media diaria (°C)
            - t_min (float): temperatura mínima diaria (°C)
            - t_max (float): temperatura máxima diaria (°C)
            - velocidad_viento (float): velocidad media diaria del viento a 2 m de altura (m/s)
            - humedad (float): humedad relativa media diaria (%)
            - radia_solar: Recomendable usar por defecto 25
            - elevacion (float): elevación del sitio (m)
        
            Retorna:
                - Valor de evapotranspiración (Et0) en milímetros por día;
    '''
  
    # Calcular la presion atmosférica del mar:
    P = (101.3 * ((293 - 0.0065 * elevacion) / 293) ** 5.26)
    # print(P)


    delta = (4098 * (0.6108 * math.exp((17.27 * t_max) / (t_max + 237.3)) - 0.6108 * math.exp((17.27 * t_min) / (t_min + 237.3)))) / ((t_max - t_min) + 237.3) ** 2
    gamma = 0.665e-3 * P  # aquí se asume que la presión atmosférica es 101.3 kPa
    psy = 0.00163 * (P/ (0.622 * 2.45))# aquí se asume que la presión atmosférica es 101.3 kPa

    ETo = 0.408 * delta * (radia_solar / 25.0) + gamma * ((900 / (t_max + 273)) * velocidad_viento * (delta + psy * (1 + 0.34 * velocidad_viento)))+ gamma * 0.34 * (1 - (humedad / 100)) * math.sqrt(elevacion) * delta

    #print('ETo:', round((ETo*10), 2), 'mm/día')

    return ETo

# Ejemplo de uso:

t_max = 19.86
t_min = 19.41
velocidad_viento = 2.5
humedad = 60
radia_solar = 25
elevacion = 150
lat = 20.67
# doy = 150

# eto = obtener_et0(t_max, t_min, velocidad_viento, humedad, radia_solar, elevacion)
# print("ETo: ", eto, "mm/day")
