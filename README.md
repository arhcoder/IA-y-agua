<a href="https://github.com/arhcoder/IA-y-agua" target="_blank"><img align="left" alt="DenunciAGS" width="100px" src="https://github.com/arhcoder/IA-y-agua/blob/master/Images/WhatsApp%20Image%202023-04-10%20at%202.34.08%20PM.jpeg?raw=true"/></a>

# IA´y agua 💧🌿🏵️🌾
<br>

Aplicación que mediante **modelos matemáticos** permite dar información a los ganaderos, de **cuánta agua deberían usar** en sus cultivos dependiendo de las características de los mismos, de modo que se utilice el mínimo de agua, **sin
perder la calidad en la producción**

<br>

___

**Este proyecto fue parte del [TALENT HACKATHON 2023](https://hackathon.genius-arena.com/"), desarrollado en Guadalajara, México el 10, 11 , 12 y 13 de abril de 2023.**

<br>

## 🧠 Desarrolladores
* Alejandra Hernandez
* Alejandro Yael
* Alejandro Ramos
* Carlos Ignacio
* Cesar Donnet



<br>




# Descripción de los algoritmos principales del programa
## etc_necesidad_hidrica
Este programa es el corazón de nuestro proyecto, se encarga de calcular la necesidad hídrica de un cultivo basado en parámetros meteorológicos y características del cultivo. Toma como entrada la superficie del campo en metros cuadrados, el tipo de semilla, el estado actual del cultivo, el tipo de riego, la latitud y longitud del sitio, (Parámetros que recibe de otras funciones). Luego, utiliza un conjunto de coeficientes de cultivo referencial para encontrar el coeficiente de cultivo (kc) correspondiente al estado actual del cultivo junto con el tipo de semilla. Con el valor de kc y los parámetros meteorológicos, el programa utiliza la ecuación de evapotranspiración de referencia (ET0) para calcular la evapotranspiración del cultivo. 
Finalmente, devuelve la necesidad hídrica en mm/día para el cultivo especificado obtenida por la multiplicación del et0 por Kc y el área en metros cuadrados.
Que a su vez imprime la cantidad de agua utilizada (en litros) = valor de mm/día x superficie del área (en metros cuadrados) x factor de conversión (en litros/metro cuadrado/mm)
________________________
La cantidad de agua que se debe aplicar por planta y luego por toda la superficie de nuestro cultivo será definida por algunos cálculos que veremos a continuación. Resumiremos entonces en 2 pasos la determinación de cuánto y cuándo regar:

- ¿CUÁNTO REGAR?: Se refiere a la cantidad de agua que se debe aplicar al suelo para reponer el agua absorbida por la planta y la evaporada. Para ello hay que determinar la demanda hídrica del cultivo o evapotranspiración 

- ¿CUÁNDO REGAR?: Se refiere al momento en que debemos reponer el agua al suelo y que ha sido consumida por los cultivos entre dos riegos. La cantidad de agua a reponer depende esencialmente del cultivo y de la cantidad de agua que deseamos sacar del suelo, entendiendo que éste actúa como un estanque de almacenamiento. Esto definirá la frecuencia de riego y el tiempo de riego necesario para reponer el agua utilizada.

Es aquí donde entra el valor del ETC.
ETC se refiere a la Evapotranspiración de Cultivo, que es la cantidad de agua perdida por un cultivo debido a la evaporación y la transpiración de las plantas en un área específica durante un período de tiempo
La que podemos calcular a través de la siguiente expresión:
ETC=Et0 x Kc x A


Donde
	**Etc***:	 Es la evapotranspiración de cultivo y que es igual a la Demanda hídrica (mm/día).
	**Eto**:	 Es la evapotranspiración de referencia (mm/día).
	**Kc**:	 Es un factor que ajusta el valor a la condición de cultivo.
	**A**:	 Es el área en metros cuadrados del cultivo.
http://www.gea.uchile.cl/archivos/Como_determinar_cuando_y_cuanto_regar_Conadi.pdf


## et0_obtener_parametros

Este código utiliza una función llamada obtener_parametros_et0 que recibe como parámetros la latitud y longitud de una ubicación. La función utiliza la librería PyOWM para obtener información del clima y la librería Requests para obtener la elevación de la ubicación a través de la API de opentopodata.org.

La función luego utiliza la fecha actual para obtener el día del año, y finalmente devuelve un diccionario con los datos obtenidos, incluyendo la temperatura media, mínima y máxima, la velocidad y dirección del viento, la humedad, la elevación y el día del año.

## et0_evapotranspiracion
Este código define una función llamada "obtener_et0" que calcula la evapotranspiración de referencia (ETo) utilizando la ecuación de Penman-Monteith. Los parámetros que se necesitan para realizar el cálculo son rescatados de funciones anteriores como lo (Parámetros meteorológicos) La función devuelve el valor de ETo en milímetros por día. 
________________________
El método Penman-Monteith, sigue considerándose la mejor forma de estimar la ET0 en la mayoría de las regiones del planeta. De hecho, es ampliamente utilizado y recomendado por organizaciones internacionales como la FAO (Organización de las Naciones Unidas para la Alimentación y la Agricultura) como método estándar para calcular la ET0.
https://www.scirp.org/html/8-3000174_16853.htm

	Nuestra ecuación resulta de una ligera modificación en la ecuación original:
    ETo = 0.408* ∆ * (solarrad/25.0  )+* ((900/t_max⁡〖+273〗  )* windspeed* (delta + psy * (1 + 0.34 * windspeed)))+ γ * 0.34 * (1 - (humidity/10))*√elev  * ∆

En este caso lo valores utilizados son los siguientes: 
	**ETo**: evapotranspiración de referencia (mm/día).
	**delta**: pendiente de la curva de presión de vapor (kPa/°C).
	**solar_rad**: radiación solar (MJ/m2/día).
	**t_max**: temperatura máxima del aire (°C).
	**wind_speed**: velocidad del viento a una altura estándar (m/s).
	**psy**: constante psicrométrica (kPa/°C).
	**gamma**: constante psicrométrica (kPa/°C).
	**humidity**: humedad relativa (%).
	**elev**: altitud sobre el nivel del mar (m).
	
Luego de realizar varias pruebas de ejecución y comprobación de resultados, pudimos constatar que nuestra versión de la ecuación obtuvo un alto nivel de precisión en comparación con otros métodos. Este resultado resulta sumamente positivo, ya que nos brinda la confianza necesaria para utilizar nuestra ecuación en situaciones similares para predecir y estimar valores sin la necesidad de usar tantas variables. Sin embargo, es importante tener en cuenta que, como cualquier modelo o ecuación, nuestra propuesta tendrá limitaciones y posibles errores, por lo que recomendamos seguir realizando pruebas y mejoras en el futuro para garantizar su eficacia continua. 

## frecuencia_de_riego
Se encarga de calcular la frecuencia de riego necesaria para una zona geográfica determinada, utilizando parámetros climáticos y características del suelo. Usa los parámetros anteriormente obtenidos de valores como lo son: temperatura, humedad relativa, velocidad del viento y radiación solar para la ubicación geográfica especificada por su latitud y longitud. Luego, el programa solicita al usuario que introduzca valores para la temperatura, humedad relativa, velocidad del viento y profundidad de las raíces, y utiliza estos valores para calcular la tasa de evaporación y la pérdida de agua utilizando las fórmulas de Priestley-Taylor y Penman-Monteith, respectivamente. También calcula la humedad óptima utilizando la profundidad de las raíces y, finalmente, calcula la frecuencia de riego necesaria utilizando estas variables. El resultado se muestra en la consola.


Las funciones vap_pres y sat_vap_pres son dos funciones auxiliares utilizadas en el cálculo de la tasa de evaporación y la pérdida de agua, respectivamente. Ambas funciones trabajan con la presión de vapor de agua, que es la presión que ejerce el vapor de agua en una mezcla de aire y agua, El programa imprime el resultado de la frecuencia de riego necesaria para la ubicación geográfica especificada.
________________________
La fórmula nueva utilizada en esta función es la de Priestley-Taylor es utilizada en hidrología e hidrogeología para estimar la evapotranspiración de una superficie determinada.
La fórmula de Priestley-Taylor se basa en la idea de que la evapotranspiración es proporcional a la radiación solar recibida por la superficie, y se expresa como:
ET = α * RS
Donde ET es la evapotranspiración, RS es la radiación solar, y α es una constante empírica que depende de las condiciones climáticas y del tipo de vegetación presente en la superficie.

## Kc_coeficiente_semilla
Este código es una función llamada obtener_kc que toma dos argumentos: semilla y estatus_cultivo. La función busca el valor de una constante Kc en un archivo CSV que contiene una lista de coeficientes de cultivo referencial. El valor de Kc se utiliza en la fórmula para calcular la necesidad de agua de un cultivo.

La función primero abre el archivo CSV que contiene los coeficientes de cultivo referencial. Luego, busca la columna correspondiente al estatus del cultivo y la fila correspondiente al tipo de semilla. Si se encuentra el valor de Kc, la función devuelve el valor como un número de punto flotante. Si no se encuentra, devuelve False.

# Descripción del DataSet utilizado

## kc-coeficientes-de-cultivo-referencial
Los coeficientes de cultivos referencial (Kc) son valores adimensionales utilizados para calcular la demanda de agua de un cultivo en un área específica durante su ciclo de crecimiento. Estos valores se utilizan en conjunto con la ETC (evapotranspiración de cultivo) para calcular la ETc (evapotranspiración del cultivo real) y así determinar la cantidad de agua que debe suministrarse al cultivo.

En nuestro caso el dataset cuenta con las fases de inicio, desarrollo, medio, final y cosecha de 37 semillas distintas.

# Modelos de simulación
## simulacion_1
Este código simula el crecimiento de un cultivo en una parcela a lo largo del tiempo, utilizando un modelo matemático que tiene en cuenta diferentes variables ambientales y parámetros de crecimiento de la planta.

Primero, se definen los parámetros de simulación, como el tiempo que pasa entre cada punto de la simulación (dt), el tiempo total de duración de la simulación (Tmax), el tiempo en forma de un vector (T) y el número de días en la simulación (N). Luego, se inicializa un vector de crecimiento de la planta (G) con un valor inicial de 0.01 kg/ha.
A continuación, se definen las condiciones ambientales del modelo que permiten el inicio de un proceso de simulación lineal

## simulacion_2
Este código también simula el crecimiento de una planta usando regresión lineal, pero en lugar de solicitar datos climáticos al usuario, genera datos climáticos aleatorios para cada día utilizando la función random.uniform() de Python. Luego, utiliza la misma lógica para calcular la tasa de crecimiento de la planta en función de las condiciones climáticas. En este caso, el ciclo for se utiliza para iterar sobre los días de la simulación y la altura de la planta se actualiza en consecuencia. El número de días de simulación se establece mediante la variable days. En resumen, este código utiliza un enfoque de simulación basado en datos aleatorios para evaluar el crecimiento de una planta en diferentes condiciones climáticas y es una forma efectiva de entender cómo diferentes factores climáticos pueden afectar el crecimiento de la planta.

## simulacion_3
Este código utiliza un enfoque de simulación basado en regresión lineal para evaluar el crecimiento de una planta en función de las condiciones climáticas diarias. La simulación se realiza mediante un ciclo while que solicita datos de temperatura, precipitación y luz solar del usuario para cada día y utiliza una función para calcular la tasa de crecimiento de la planta. Luego, la altura de la planta se actualiza en consecuencia y se muestra en la consola junto con la tasa de crecimiento. Este enfoque de simulación es una forma efectiva de evaluar el crecimiento de una planta en diferentes condiciones climáticas y entender cómo diferentes factores influyen en el crecimiento de la planta

# Modelo de Inteligencia Artificial
Aunque los modelos de simulación que utilizan inteligencia artificial aún no están completamente desarrollados para estimar los valores óptimos para el cultivo, existen diversas técnicas de aprendizaje automático y análisis de datos que pueden aplicarse para mejorar su precisión y utilidad en la agricultura moderna. En este sentido, nuestro proyecto ha desarrollado un algoritmo válido que ha sido detallado en la documentación final, el cual puede ser utilizado para optimizar la producción de cultivos y aumentar la eficiencia de las operaciones agrícolas. Sin embargo, es importante seguir investigando y mejorando estos modelos para que sean más precisos y fiables en la predicción del rendimiento.
