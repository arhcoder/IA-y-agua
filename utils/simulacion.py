import numpy as np
import matplotlib.pyplot as plt

# Definir los Parámetros de Simulación
dt = 0.01  # Tiempo que pasa (en dias)
Tmax = 50  # Tiempo maximo de duracion de la simulacion (en dias)
T = np.arange(0, Tmax, dt)  # Tiempo en vector
N = len(T)  # Numero de dias pasados en la simulacion
G = np.zeros(N)  # Inicializar el vector de crecimiento de la planta
G[0] = 0.01  # Inicializa el crecimiento de la planta en 0.01 kg/ha (kilogramos por hectarea)


# Condiciones Ambientales
temp = np.ones(N) * 25  # C onstante de temperatura (en grados Celsius)
rain = np.ones(N) * 5  # Constante de lluvia (mm/dia)
light = np.ones(N) * 5000  # Constante de luz directa (en lux)

# Parametros de la planta en cuestion de crecimiento
k1 = 0.05  # Tasa de crecimiento Constante (kg/ha/dia)
k2 = 0.0001  # Tasa de mortalidad constante (kg/ha/dia)
k3 = 0.00005  # constante de inhibición del crecimiento (kg/ha/mm)

# Proceso de simulacion
for i in range(1, N):
    # Calcular la tasa de crecimiento del cultivo
    dGdt = k1 * G[i-1] - k2 * G[i-1] * rain[i-1] - k3 * G[i-1] * rain[i-1]
    
    # Actualizar el crecimiento de los cultivos
    G[i] = G[i-1] + dGdt * dt
    
    # Compruebe si hay un crecimiento negativo del cultivo
    if G[i] < 0:
        G[i] = 0

# Parcela de crecimiento del cultivo y la grafica de crecimiento
plt.plot(T, G)
plt.xlabel('Time (days)')
plt.ylabel('Crop growth (kg/ha)')
plt.show()