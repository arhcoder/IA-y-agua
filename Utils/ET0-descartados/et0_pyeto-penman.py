import pyeto

def calcular_et0(t_med, t_min, t_max, viento, humedad, elevacion, latitud, dia_yeard):
    # Convertir de grados Celsius a Kelvin
    t_med += 273.15
    t_min += 273.15
    t_max += 273.15

    # Calcular la presión atmosférica
    presion_atm = pyeto.atm_pressure(elevacion)

    # Calcular la radiación solar en el topo de la atmósfera
    rad_solar_topo = pyeto.radiation.extraterrestrial_radiation(latitud, dia_yeard)

    # Calcular la radiación solar neta
    rad_solar_neta = pyeto.net_solar_radiation(t_min, t_max, rad_solar_topo, humedad)

    # Calcular la radiación infrarroja neta
    rad_infrarroja_neta = pyeto.net_infrared_radiation(t_min, t_max, t_med, rad_solar_topo, humedad)

    # Calcular la temperatura media del aire a partir de la temperatura mínima y máxima
    t_media = (t_min + t_max) / 2

    # Calcular la pendiente de la curva de presión de vapor
    pend_curva_pres_vapor = pyeto.slope_vapor_pressure_curve(t_media)

    # Calcular la presión de vapor media
    pres_vapor_media = pyeto.avp_from_humidity(t_media, humedad, presion_atm)

    # Calcular la presión de vapor saturado a la temperatura mínima y máxima
    pres_vapor_saturado_min = pyeto.saturation_vapor_pressure(t_min)
    pres_vapor_saturado_max = pyeto.saturation_vapor_pressure(t_max)

    # Calcular la presión de vapor de saturación a la temperatura media
    pres_vapor_saturado_media = (pres_vapor_saturado_min + pres_vapor_saturado_max) / 2

    # Calcular la resistencia aerodinámica
    resistencia_aero = pyeto.aerodynamic_resistance(viento)

    # Calcular la resistencia a la transferencia de vapor de agua
    resistencia_transfer_vapor = pyeto.humidity_deficit_resistance(pres_vapor_media, pres_vapor_saturado_media, t_media, resistencia_aero)

    # Calcular la evapotranspiración de referencia (Et0) utilizando el método de Penman-Monteith
    et0 = pyeto.penman_monteith(rad_solar_neta, rad_infrarroja_neta, t_med, viento, presion_atm, pend_curva_pres_vapor, pres_vapor_media, pres_vapor_saturado_media, resistencia_aero, resistencia_transfer_vapor)

    # Convertir de metros por segundo a kilómetros por día
    et0 = et0 * 86400 / 1000

    return et0

from pyeto import fao

def calcular_et0(t_med, t_min, t_max, viento, humedad, elevacion, latitud, dia_yeard):
    # calcular la radiación solar extraterrestre
    Ra = fao.spencer_intradc(latitud, dia_yeard)

    # calcular la duración diaria de la insolación
    n = pyeto.sunshine_hours(t_med, elevacion)

    # calcular la radiación solar
    a, b = fao.angstrom(0.25, 0.50, latitud, dia_yeard)
    N = pyeto.daylight_hours(latitud, dia_yeard)
    R = (a + b * (n / N)) * Ra

    # calcular la Evapotranspiración de referencia
    Et0 = pyeto.hargreaves(t_min, t_max, t_med, R, viento, humedad, elevacion)

    return Et0