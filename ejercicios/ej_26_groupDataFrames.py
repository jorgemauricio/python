#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 17 16:17:25 2017

@author: jorgemauricio
"""

# librerias
import numpy as np
import pandas as pd
from pandas import DataFrame, Series

# crear un dataframe
dframe = DataFrame({'k1':['X','X','Y','Y','Z'],
                    'k2':['alpha','beta','alpha','beta','alpha'],
                    'dataset1':np.random.randn(5),
                    'dataset2':np.random.randn(5)})

# desplegar
dframe

# tomamos la columan dataset1 y lo agrupamos con la llave k1
group1 = dframe['dataset1'].groupby(dframe['k1'])

# desplegar el objecto
group1

# ahora podemos realizar operaciones en este objeto
group1.mean()

# podemos utilizar los nombres de las columnas para generar las llaves de los grupos
dframe.groupby('k1').mean()

# o multiples columnas
dframe.groupby(['k1','k2']).mean()

# podemos saber el tamaño del grupo con el metodo .size()
dframe.groupby(['k1']).size()

# podemos iterar entre los grupos

# por ejemplo:
for name,group in dframe.groupby('k1'):
    print ("This is the %s group" %name)
    print (group)
    print ('\n')

# utilizando multiples llaves
for (k1,k2) , group in dframe.groupby(['k1','k2']):
    print ("Key1 = %s Key2 = %s" %(k1,k2))
    print (group)
    print ('\n')

# se puede generar un diccionario de la informacion
group_dict = dict(list(dframe.groupby('k1')))

# desplegar el grupo con una 'X'
group_dict['X']