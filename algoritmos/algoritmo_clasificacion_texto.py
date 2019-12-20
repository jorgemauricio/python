#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 17 16:17:25 2017

@author: jorgemauricio
"""
#%% librerias
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#%% read .txt files
f = open('../data/1.txt', 'r')

#%% crear una variable
file = f.read()

#%% texto a mayusculas
file = file.upper()

#%% eliminar interlineado
file = file.replace('\n',' ')

#%% eliminar comas
file = file.replace(',',' ')

#%% eliminar puntos
file = file.replace('.',' ')

#%% eliminar punto y comas
file = file.replace(';',' ')

#%% eliminar ?
file = file.replace('?',' ')

#%% eliminar ¿
file = file.replace('¿',' ')

#%% eliminar !
file = file.replace('!',' ')

#%% eliminar ¡
file = file.replace('¡',' ')

#%% eliminar doble espacio
file = file.replace('  ',' ')

#%% eliminar doble espacio
file = file.replace('   ',' ')

#%% texto a array
fileArray = file.split(' ')

#%% numero de palabras
print('***** Numero de palabras: {}'.format(len(fileArray)))

#%% init dictionary
dictionaryOfWords = dict()

#%% generar un diccionario de palabras
for i in fileArray:
	if i in dictionaryOfWords:
		dictionaryOfWords[i] = dictionaryOfWords[i] + 1
	else:
		dictionaryOfWords[i] = 1

#%% preposiciones
preposiciones = ['','AL','A', 'ANTE', 'BAJO', 'CABE', 'CON', 'CONTRA', 'DE', 'DESDE', 'DURANTE', 'EN','ENTRE', 'HACIA','HASTA','MEDIANTE','PARA','POR','SEGUN','SIN','SON','SOBRE','TRAS','Y','A','O','YA','LA','LOS','EL','ELLOS', 'HE', 'UN', 'LAS','LO','NO','DEL','ESTE', 'ESTA', 'ESTÁN', 'PERO', 'HA', 'MÁS', 'QUE', 'SE', 'ES','UNA', 'COMO','SU']

#%% borrar preposiciones
for i in preposiciones:
	if i in dictionaryOfWords:
		del dictionaryOfWords[i]

#%% dict to dataframe
data = pd.DataFrame()
data['Palabra'] = dictionaryOfWords.keys()
data['Frecuencia'] = dictionaryOfWords.values()

#%% sort data
data = data.sort_values(by='Frecuencia')

#%% generate x , y 
x = np.array(data['Palabra'])
y = np.array(data['Frecuencia'])

#%% 15 palabras mas mencionadas
x = x[-15:]
y = y[-15:]

xi = np.arange(0,len(x),1)

#%% plot words
plt.bar(xi, y, align='center')
plt.xticks(xi,x)

#%%
plt.show()
