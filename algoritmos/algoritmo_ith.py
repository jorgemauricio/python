#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 17 16:17:25 2017

@author: jorgemauricio
"""

#%% import libraries
import pandas as pd
import os

#%% Clear terminal
os.system('clear')

#%% load data from csv file
print('***** leer archivo csv')
data = pd.read_csv('../data/data_course_aguascalientes.csv')

#%% Display head of file
data.head()

#%% How many rows the dataset
data['number'].count()

#%% Drop NA values from the rows
print('***** eliminar valores nulos')
data = data.dropna()

#%% How many rows the dataset after drop NA
data['number'].count()

#%% Create Fecha Format AAAA-MM
print('***** crear columna dateFormat')
data['dateFormat'] = data.apply(lambda x: '%d-%d' % (x['year'], x['month']), axis=1)

#%% Funcion para calcular el ITH
def calcularITH(ta, hr):
	"""
	Calculate ith from ta and hr
	return ith
	ith = 1.8 * ta + 32 - (0.55 - (0.55 * (hr/100.0))) * (1.8 * ta) - 26.0
	param: ta: temperatura ambiente
	param: hr: humedad relativa
	param: ith: indice termohigrometrico
	"""
	cal1 = 1.8 * ta
	cal2 = (0.55 - (0.55 * (hr/100.0)))
	cal3 = (1.8 * ta) - 26.0
	ith = cal1 + 32 - cal2 * cal3
	return ith

#%% crear columna tmed
data['tmed'] = (data['tmax'] + data['tmin']) / 2

#%% display head of file
data.head()

#%% calcular ith
data['ith'] = data.apply(lambda x: calcularITH(x['tmed'], x['humr']), axis=1)

#%% display head of file
data.head()

#%% Aggregation
aggregations = {
        'ith' : ['min', 'max', 'median', 'mean', 'std']
        }

#%% Apply aggregation
print('***** agrupar datos por columna dateFormat')
data.groupby('dateFormat').agg(aggregations)

#%% data head
data.head()

#%% Save to CSV
print('***** guardar archivo')
grouped = data.groupby(['lat', 'long','number','dateFormat']).agg(aggregations)
grouped.columns = ["_".join(x) for x in grouped.columns.ravel()]
grouped.to_csv('../resultados/baseAgrupadaPorAnioMesITH.csv')

#%% grouped data head()
grouped.head()
