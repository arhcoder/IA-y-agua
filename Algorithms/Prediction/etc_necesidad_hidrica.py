#!/usr/bin/env python3

import cProfile
from et0_evapotranspiracion import obtener_et0
from et0_parametros import obtener_parametros_et0
from kc_coeficiente_semilla import obtener_kc
from frecuencia_riego import obtener_frecuencia_riego
import csv

def calcular_necesidad_hidrica(mts_campo: float, semilla: str, estatus_cultivo: str, tipo_riego: int, latitud: float, longitud: float):

    '''
        Calcula la necesidad hídrica de un terrno con los datos recibidos:

            - mts_campo (float): Metros cuadrados de superficie del terreno;

            - semilla (string): Texto en minúsculas que describe
              el nombre de la semilla del que se quiere extraer
              el coeficiente de cultivo referencial; necesario en
              la fórmula del cálculo de la necesidad hídrica.
              La lista de semillas para las que se tiene el
              coeficiente; se encuentra en el archivo:
              "../../Data/kc-coeficientes-de-cultivo-referencial.csv";
              Ejemplo: "alfalfa";

            - estatus_cultivo (string): Estátus del cultivo; en texto y minúscualas;
                - "Inicial": En esta etapa, el cultivo se encuentra en el periodo de germinación
                    y emergencia de las plántulas. Tiene una alta demanda de agua para mantener
                    la humedad del suelo y favorecer su crecimiento.
                - "Desarrollo": En esta etapa, el cultivo ya ha desarrollado su sistema de raíces
                    y comienza a producir hojas y tallos. La demanda de agua durante esta etapa es
                    menor que en la etapa inicial, pero aún es importante para sostener el
                crecimiento del cultivo.
                - "Medios": En esta etapa, el cultivo se encuentra en su fase de desarrollo máximo,
                    con un alto crecimiento de hojas, tallos y raíces. En esta etapa, el cultivo
                    necesita un suministro constante de agua para satisfacer su demanda de nutrientes
                    y mantener su salud.
                - "Finales": Durante esta etapa, el cultivo comienza a madurar y producir frutos o
                semillas. La demanda de agua durante esta etapa disminuye a medida que el cultivo
                reduce su crecimiento y comienza a concentrar su energía en la producción de la cosecha.
                - "Cosecha": En esta etapa se recolectan los frutos o semillas del cultivo. Durante
                esta etapa, la demanda hídrica del cultivo es baja, ya que su ciclo de vida ha llegado
                a su fin.


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
    et0 = obtener_et0(t_min=clima["temp_min"], t_max=clima["temp_max"], velocidad_viento=clima["viento_vel"], humedad=clima["humedad"], elevacion=clima["elevacion"], radia_solar=25)

    # Encuentra el coeficiente del valor a la condición del cultivo basado en el tipo de semilla:
    kc = obtener_kc(semilla, estatus_cultivo)
    
    # Si logró encontrar el Kc para el tipo de cultivo; concluye el cálculo:
    if kc:
        ETC = float(et0 * kc * mts_campo)
        frecuencia = obtener_frecuencia_riego(latitud, longitud)
        litros = ETC * 100
        return f"\nTu cultivo de {mts_campo}m² de {semilla} en estátus de {estatus_cultivo} requiere {round(ETC, 2)} mm/día 😎\nQue equivalen a {round(litros, 2)}lts cada {round(frecuencia, 2)} días 📅\n"
    else:
        return "El tipo de semilla o el estátus de cultivo son incorrectos :c"

# Ejemplo de uso:
print(calcular_necesidad_hidrica(mts_campo=20, semilla="alfalfa", estatus_cultivo="cosecha", tipo_riego=1, latitud=20.6736, longitud=-103.344))

cProfile.run("calcular_necesidad_hidrica(mts_campo=20, semilla='alfalfa', estatus_cultivo='cosecha', tipo_riego=1, latitud=20.6736, longitud=-103.4050)")


