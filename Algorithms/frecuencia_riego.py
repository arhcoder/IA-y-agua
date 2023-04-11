#!/usr/bin/env python3

from et0_parametros import obtener_parametros_et0

def Obtener_frec_riego(latitud,longitud):
    clima = obtener_parametros_et0(latitud, longitud)
    # Pedimos al usuario que introduzca los valores necesarios para el cálculo
    temperatura = float(input("Introduce la temperatura en grados Celsius: "))

    humedad_relativa = float(input("Introduce la humedad relativa en porcentaje (%): "))

    velocidad_viento = float(input("Introduce la velocidad del viento en km/h: "))
    profundidad_raices = float(input("Introduce la profundidad de las raíces en cm: "))

    # Calculamos la tasa de evaporación utilizando la fórmula de Priestley-Taylor
    tasa_evaporacion = 0.0023 * (temperatura + 17.8) * ((humedad_relativa/100)**0.5)

    # Calculamos la pérdida de agua utilizando la fórmula de Penman-Monteith
    pérdida_agua = 0.408 * (tasa_evaporacion) * ((17.27 * temperatura)/(temperatura + 237.3)) + (0.0028 * velocidad_viento * (humedad_relativa/100)) * ((tasa_evaporacion) * (sat_vap_pres(temperatura) - vap_pres(humedad_relativa)))

    # Calculamos la humedad óptima utilizando la profundidad de las raíces
    humedad_optima = 0.7 * (profundidad_raices/10)

    # Calculamos la frecuencia de riego necesaria
    frecuencia_riego = (humedad_optima / (tasa_evaporacion - pérdida_agua))

    # Mostramos el resultado al usuario
   # print("La frecuencia de riego necesaria es de:", round(frecuencia_riego, 2), "días")

    return frecuencia_riego


# Definimos una función para calcular la presión de vapor saturado y la presión de vapor
def sat_vap_pres(temperatura):
	return 0.6108 * (10 ** ((7.5 * temperatura) / (237.3 + temperatura)))

def vap_pres(humedad_relativa):
	return humedad_relativa / 100 * sat_vap_pres(temperatura)

print(Obtener_frec_riego(20.6736, -103.344))

