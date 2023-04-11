from et0_evapotranspiracion import calculate_eto
from et0_parametros import obtener_parametros_et0
import csv

def calcular_necesidad_hidrica(mts_campo: float, semilla: str, estatus_cultivo: str, tipo_riego: int, latitud: float, longitud: float):

    '''
        Calcula la necesidad hídrica de
    '''

    # Obtiene los parámetros meteorológicos para la evapotranspiración:
    # Código hecho por Charly obtenido de "Utils/Parametros.py":
    '''
        - t_med (float): temperatura media diaria (°C)
        - t_min (float): temperatura mínima diaria (°C)
        - t_max (float): temperatura máxima diaria (°C)
        - viento (float): velocidad media diaria del viento a 2 m de altura (m/s)
        - humedad (float): humedad relativa media diaria (%)
        - elevacion (float): elevación del sitio (m)
        - latitud (float): latitud del sitio (grados decimales)
        - dia_yeard (int): día del año (1-365)
    '''
    clima = obtener_parametros_et0(latitud, longitud)

    # Calcula el valor de la evapotranspiración (et0):
    et0 = calculate_eto(lat=latitud, t_min=clima["temp_min"], t_max=clima["temp_max"], wind_speed=clima["viento_vel"], humidity=clima["humedad"], elev=clima["elevacion"], doy=clima["dia_anio"], solar_rad=25)

    # Encuentra el coeficiente del valor a la condición del cultivo basado en el tipo de semilla:
    with open('../Data/kc-coeficientes-de-cultivo-referencial.csv', newline='') as archivo:
        datos = list(csv.reader(archivo))
    # print(datos)

    # Recorrer la matriz de coeficientes hasta encontrar la columna con el estátus del cultivo:
    flag_estatus = False
    for columna, estatus in enumerate(datos[0]):
        if str(estatus) == estatus_cultivo:
            flag_estatus = True
            break
    
    # Recorrer la matriz de coeficientes hasta encontrar la fila con el tipo de semilla:
    flag_semilla = False
    for fila, semilla_data in enumerate(datos):
        if str(semilla_data[0]) == semilla:
            flag_semilla = True
            break
    
    # Si logró encontrar el Kc para el tipo de cultivo; concluye el cálculo:
    if flag_semilla and flag_estatus:
        kc = float(datos[fila][columna])
        ETC = float(et0 * kc * mts_campo)
        return f"\nTu cultivo de {mts_campo}m² de {semilla} en estátus de {estatus_cultivo} requiere {ETC} mm/día 😎\n"
    else:
        return "No"

# Ejemplo de uso:
print(calcular_necesidad_hidrica(mts_campo=20, semilla="alfalfa", estatus_cultivo="cosecha", tipo_riego=1, latitud=20.6736, longitud=-103.344))