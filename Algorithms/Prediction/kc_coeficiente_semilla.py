import csv

def obtener_kc(semilla: str, estatus_cultivo: str):

    '''
        Recibe:

            * [semilla] (string): Texto en minúsculas que describe
              el nombre de la semilla del que se quiere extraer
              el coeficiente de cultivo referencial; necesario en
              la fórmula del cálculo de la necesidad hídrica.
              La lista de semillas para las que se tiene el
              coeficiente; se encuentra en el archivo:
              "/Data/kc-coeficientes-de-cultivo-referencial.csv";
              Ejemplo: "alfalfa";
            
            * [estatus_cultivo] (string): Estátus del cultivo; en texto y minúscualas;
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
        
            Retorna:

            * El valor de la constante Kc como float; si se encuentra;
            * FALSE si no encuentra el valor;
    '''

    with open('../../Data/kc-coeficientes-de-cultivo-referencial.csv', newline='') as archivo:
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
    
    # Si logró encontrar el Kc para el tipo de cultivo:
    if flag_semilla and flag_estatus:
        kc = float(datos[fila][columna])
        return kc
    else:
        return False