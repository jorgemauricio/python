#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 17 16:17:25 2017

@author: jorgemauricio
"""

"""
	De los datos proporcionados por SCHP, se eligen algunas columnas para trabajar la información 
	y se exploran las relaciones entre los montos registrados por mes, año, mes-año y año-sector. 
	La intención es responder las siguientes preguntas sencillas:

	¿En que anio se registro un mayor monto?
	¿En que mes se tienen la media mas alta de monto?
	¿En que anio y mes se registran los mayores montos?
	¿En que anio y sector se registran los mayores montos?

	fuente: http://catalogo.datos.gob.mx/dataset/estadisticas-oportunas-de-finanzas-publicas

"""

#%%librerias
import matplotlib
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

#%% tipo de grafico
plt.rcParams['figure.figsize']=(20,7)

#%% cargar datos
data = pd.read_csv('../data/ingresos.csv')

#%% checar la informacion
data.head()

#%% numero de filas y columnas
data.shape

#%% descripcion general de las variables
data.info()

#%% tipo de dato
data.dtypes

#%% nombre de las columnas
data.columns

#%% seleccionamos las columnas mas importantes
dataP = data[['CICLO','MES','NOMBRE','TEMA','SECTOR','MONTO']]

#%% mostramos la informacion seleccionada
dataP.head()

#%% cual es el anio con mayor monto registrado
group1 = dataP.groupby('CICLO')

#%% cantidad de registros para cada anio
group1.size()

#%% sumatoria de registros para cada anio
group1.sum()

#%% cantidad de registros en cada mes
group2 = dataP.groupby('MES')

#%% cantidad de registros para cada mes
group2.size()

#%% media
group2.mean()

# la variable ciclo se despliega como una variable númerica
#%% para desplegar la media solo del monto
group2.mean()['MONTO']

"""
Si se desea saber cual es el mes con la media de montos mayor, basta elegir
el máximo de los valores de las medias al ordenarlas. En este caso corresponde al mes de Diciembre
"""
group2['MONTO'].mean().sort_values()[-1:]

#%% agrupamos la informacion por anio y mes para conocer como se comportan los montos
group3 = dataP.groupby(['CICLO', 'MES'])

#%% vemos el valor de la suma de los montos
group3.sum()

#%% para elegir los 5 registros con los montos mas alta, hacemos la siguiente seleccion al group3
group3.sum().sort_values(by='MONTO')[-5:]

#%% se puede revisar como se comporta por CICLO y SECTOR, elegimos los 15 registros con valor
#%% mas alto en la suma de su MONTO
group4 = dataP.groupby(['CICLO', 'SECTOR']).sum().sort_values(by='MONTO')[-15:].plot(kind='bar')

#%%g desplegar grafica
plt.show()

#%% mostrar cantidad, sumatoria, max y min en valores
group1['MONTO'].agg([np.size, sum, max, min])

#%% comparativo entre maximo y minimo
group1['MONTO'].agg([max, min]).plot(kind='bar')

#%% desplegar grafica
plt.show()

#%% se explora como se comporta la agrupacion por mes, mediante una grafica de barras
group2['MONTO'].agg([max, min, np.mean])

#%% los datos originales permiten explorar graficamente como se relacionan los valores de los montos
#%% con respecto a los meses
sns.barplot(data=dataP, x='MES', y='MONTO', palette='PRGn')

#%% desplegar grafica
plt.show()

#%% explorar los datos agrupados por anio-mes
group3['MONTO'].agg([max, min, np.mean]).plot(title='Comportamiento de la suma de los montos')

#%% desplegar grafica
plt.show()
