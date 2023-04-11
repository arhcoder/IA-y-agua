import math

def calcular_et0(t_med, t_min, t_max, viento, humedad, elevacion, latitud, dia_yeard):
    
    """Función que calcula la evapotranspiración de referencia (ET0) utilizando la ecuación de Penman-Monteith.

    Parámetros:
    - t_med (float): temperatura media diaria (°C)
    - t_min (float): temperatura mínima diaria (°C)
    - t_max (float): temperatura máxima diaria (°C)
    - viento (float): velocidad media diaria del viento a 2 m de altura (m/s)
    - humedad (float): humedad relativa media diaria (%)
    - elevacion (float): elevación del sitio (m)
    - latitud (float): latitud del sitio (grados decimales)
    - dia_yeard (int): día del año (1-365)

    Retorna:
    - ET0 (float): evapotranspiración de referencia (mm/día)
    """
    # Constantes
    RADIACION_SOLAR_CONSTANTE = 0.0820  # MJ/m2/min
    GRAVEDAD_ESPECIFICA_AIRE = 0.000665  # kg/m3
    CP = 1.013e-3  # MJ/kg/°C

    # Cálculo de la radiación solar extraterrestre
    dr = 1 + 0.033 * math.cos((2 * math.pi / 365) * dia_yeard)
    delta = 0.409 * math.sin((2 * math.pi / 365) * dia_yeard - 1.39)
    w_s = math.acos(-math.tan(latitud * math.pi / 180) * math.tan(delta))
    Ra = (24 * 60 / math.pi) * RADIACION_SOLAR_CONSTANTE * dr * (
            w_s * math.sin(latitud * math.pi / 180) * math.sin(delta)
            + math.cos(latitud * math.pi / 180) * math.cos(delta) * math.sin(w_s)
    )

    # Cálculo de la presión atmosférica
    p_atm = 101.3 * ((293 - 0.0065 * elevacion) / 293) ** 5.26

    # Cálculo de la pendiente de la curva de presión de vapor
    t_med_kelvin = t_med + 273.16
    es_max = 0.6108 * math.exp(17.27 * t_max / (t_max + 237.3))
    es_min = 0.6108 * math.exp(17.27 * t_min / (t_min + 237.3))
    es = (es_max + es_min) / 2
    delta_es = 4098 * es / t_med_kelvin ** 2
    pendiente = delta_es * CP / GRAVEDAD_ESPECIFICA_AIRE

    # Cálculo de la déficit de presión de vapor
    ea = es_min * humedad / 100
    delta_ea = 4098 * ea / t_med_kelvin ** 2
    deficit_presion_vapor = es - ea

        # Cálculo de la radiación neta diaria
    albedo = 0.23
    Rs = 0.75 * Ra
    Rns = (1 - albedo) * Rs

    # Cálculo de la radiación neta de onda larga
    sigma = 4.903e-9  # MJ/m2/K4
    Rnl = sigma * (t_max + 273.16) ** 4 * (
            0.34 - 0.14 * math.sqrt(ea)
    ) * (1.35 * Rs / Rn - 0.35)

    # Cálculo de la radiación neta
    Rn = Rns - Rnl

    # Cálculo de la resistencia aerodinámica a la transferencia de masa
    z = 2  # Altura del anemómetro
    d = 0.67 * z  # Altura del instrumento de medida
    zh = 0.13 * z
    zoh = 0.013 * z
    dT = t_max - t_min
    esat = 0.6108 * math.exp(17.27 * t_med / (t_med + 237.3))
    ea = esat * humedad / 100
    Rho_air = p_atm / (287.058 * t_med_kelvin)
    Cp_air = 1004.67 + 0.0008 * ea
    lv = 2.45  # Latent heat of vaporization (MJ/kg)
    gamma = 0.665e-3 * p_atm / Cp_air
    u2 = viento * (math.log((z - d) / zoh) / math.log((zh - d) / zoh))
    R_ah = (math.log((z - d) / zh) * math.log((zh - d) / zoh)) / (gamma * u2)

    # Cálculo de la evapotranspiración de referencia (ET0)
    ET0 = (0.408 * pendiente * Rn + gamma * (900 / (t_med + 273)) * u2 * deficit_presion_vapor) / (
            pendiente + gamma * (1 + 0.34 * u2 / R_ah)
    )

    return ET0