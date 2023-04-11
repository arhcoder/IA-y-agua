''' from datetime import datetime, timedelta
from pyeto import fao, Location

def calcular_et0(t_med, t_min, t_max, viento, humedad, elevacion, latitud, dia_yeard):
    # Convertir la latitud de grados decimales a radianes
    latitud_rad = latitud * (3.14159 / 180.0)

    # Crear objeto datetime para el día del año
    fecha = datetime(2023, 1, 1) + timedelta(days=dia_yeard-1)

    # Crear objeto Location con la latitud y longitud del sitio
    ubicacion = Location(latitud, 0)

    # Calcular la duración del día en horas
    duracion_dia = fao.daylight_hours(fecha, ubicacion)

    # Calcular la presión atmosférica en kPa
    presion_atm = fao.atmospheric_pressure(elevacion)

    # Calcular la constante psicrométrica en kPa/°C
    const_psicrom = fao.psy_const(presion_atm)

    # Calcular la pendiente de la curva de saturación de vapor en kPa/°C
    pend_curva_vapor = fao.sat_vapour_slope(t_med)

    # Calcular la presión de saturación de vapor a la temperatura mínima y máxima en kPa
    pres_sat_min = fao.saturation_vapour_pressure(t_min)
    pres_sat_max = fao.saturation_vapour_pressure(t_max)

    # Calcular la presión de vapor actual en kPa
    pres_vapor = fao.actual_vapour_pressure(pres_sat_min, pres_sat_max, humedad)

    # Calcular la radiación neta en MJ/m²/día
    rad_neta = fao.net_radiation(dia_yeard, latitud, duracion_dia, t_min, t_max, viento)

    # Calcular la resistencia aerodinámica en s/m
    res_aero = fao.aerodynamic_resistance(viento)

    # Calcular la resistencia estomática en s/m
    res_estom = fao.stomatal_resistance()

    # Calcular la evapotranspiración de referencia en mm/día
    et0 = fao.penman_monteith(presion_atm, pend_curva_vapor, const_psicrom, rad_neta, t_med, viento, pres_vapor, res_aero, res_estom)

    return et0'''

'''
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
'''

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