import csv
import math

# Leer el archivo CSV y cargar los datos en una lista
with open('../Data/data.csv', newline='') as archivo:
    datos = list(csv.reader(archivo))

# Recorrer la lista y actualizar los valores con "-"
for i, fila in enumerate(datos):
    for j, valor in enumerate(fila):
        if '-' in valor and valor.isnumeric():
            # Calcular el promedio entre los números antes y después del "-"
            anterior = float(fila[j-1])
            siguiente = float(fila[j+1])
            promedio = (anterior + siguiente) / 2
            # Actualizar el valor con el promedio calculado
            datos[i][j] = str(promedio)

# Guardar los datos actualizados en un nuevo archivo CSV
with open('archivo_actualizado.csv', 'w', newline='') as archivo:
    writer = csv.writer(archivo)
    writer.writerows(datos)