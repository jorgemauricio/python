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
data = pd.read_csv('../data/data_course_prec.csv')

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

#%% column precipitacion to vReal
data['vReal'] = data['rain']

#%% Create Rainy days column
print('***** crear columna de dias con lluvia')
data['rainyDays'] = [1 if x > 0.0 else 0 for x in data['vReal']]

#%% Create No rainy days column
print('***** crear columna de dias sin lluvia')
data['noRainy'] = [1 if x == 0.0 else 0 for x in data['vReal']]

#%% grouped classification 0 - 5
print('***** clasificacion de 0 a 5')
data['0_5'] = [1 if x > 0.0 and x <= 5.0 else 0 for x in data['vReal']]

#%% grouped classification 5 - 10
print('***** clasificacion de 5 a 10')
data['5_10'] = [1 if x > 5.0 and x <= 10.0 else 0 for x in data['vReal']]

#%% grouped classification 10 - 15
print('***** clasificacion de 10 a 15')
data['10_15'] = [1 if x > 10.0 and x <= 15.0 else 0 for x in data['vReal']]

#%% grouped classification 15 - 20
print('***** clasificacion de 15 a 20')
data['15_20'] = [1 if x > 15.0 and x <= 20.0 else 0 for x in data['vReal']]

#%% grouped classification > 20
print('***** clasificacion mayor a 20')
data['20_'] = [1 if x > 20.0 else 0 for x in data['vReal']]

#%% Aggregation
aggregations = {
        'vReal' : ['sum', 'min', 'max', 'median', 'mean', 'std'],
        'rainyDays' : ['sum'],
        'noRainy' : ['sum'],
        '0_5' : ['sum'],
        '5_10' : ['sum'],
        '10_15' : ['sum'],
        '15_20' : ['sum'],
        '20_' : ['sum']
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
grouped.to_csv('../resultados/baseAgrupadaPorAnioMes.csv')

#%% grouped data head()
grouped.head()
