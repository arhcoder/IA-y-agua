'''

    PUNTO DE EJECUCIÓN QUE ENGLOBA TODO EL SISTEMA DE PREDICCIÓN

'''

from etc_necesidad_hidrica import calcular_necesidad_hidrica

print("\nCÁLCULO DE NECESIDAD HÍDRICA\n")

area = float(input(" * Área en mts² del cultivo: "))

semilla = input(" \n* Semilla;\n  ajo, alfalfa, almendro, arandano 1año, arandano 2año, arandano 3año, " \
    "\n  arroz, arveja fresca, cebolla seca, cebolla verde, ciruelo, coliflor" \
    "\n  duraznero, esparragos, frambuesa, kiwi, maiz dulce, maiz grano" \
    "\n  mani, manzano, maravilla, nectarino, nogal, olivo, palto, papa" \
    "\n  peral, pimentón, poroto seco, poroto vade, pradera, remolacha" \
    "\n  sandía, tabaco, tomate, togo, vid):\n")

estatus = input("\n * Estatus;\n  \"Inicial\": Etapa de germinación y emergencia de las plántulas, con alta demanda de agua." \
    "\n  \"Desarrollo\": Etapa de crecimiento de hojas y tallos, con menor demanda de agua que la etapa inicial." \
    "\n  \"Medios\": Etapa de desarrollo máximo con alta demanda constante de agua para mantener la salud del cultivo." \
    "\n  \"Finales\": Etapa de maduración y producción de frutos o semillas, con disminución en la demanda de agua." \
    "\n  \"Cosecha\": Etapa donde se recolectan los frutos o semillas, con baja demanda hídrica ya que el ciclo de vida del cultivo ha llegado a su fin.\n")

tipo_riego = input("\n * Tipo de riego;\n  [1]: Riego por gravedad." \
    "\n  [2]: Riego por asperción." \
    "\n  [3]: Riego localizado." \
    "\n  [4]: Riego subterráneo.\n")

print("\n  * Localización: Guadalajara")
ok = input("\nOkay?")

print("\nProcesando cálculo de óptimo de agua...")
response = calcular_necesidad_hidrica(mts_campo=area,
                                      semilla=semilla.lower(),
                                      estatus_cultivo=estatus.lower(),
                                      tipo_riego=1,
                                      latitud=20.6736,
                                      longitud=-103.344)

print(f"{response}")