#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 17 16:17:25 2017

@author: jorgemauricio
"""

#%% import libraries
import pandas as pd
import os
import numpy as np

#%% Clear terminal
os.system('clear')

#%% load data from csv file
print('***** leer archivo csv')
data = pd.read_csv('../data/data_course_aguascalientes.csv')

#%% generar array para el ciclo for 
estaciones = np.array(data['name'])
estaciones = np.unique(estaciones)

#%% comenzar con el ciclo for
for i in estaciones:
	dataTemp = data.loc[data['name'] == i]
	print("***** Generando: {}".format(i))
	tempTitle = "../resultados/clasificacion/{}.csv".format(i)
	dataTemp.to_csv(tempTitle)

print("***** proceso terminado")
