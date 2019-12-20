#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 17 16:17:25 2017

@author: jorgemauricio
"""

# librerias
import numpy as np
from pandas import Series,DataFrame
import pandas as pd

# Crear una serie (arreglo de datos con etiquetas)
obj = Series([3,6,9,12])

# desplegar
obj

# desplegar los valores
obj.values

# desplegar el indice
obj.index

# Crear una serie con indice 

# WW2 damnificados
ww2_cas = Series([8700000,4300000,3000000,2100000,400000],index=['USSR','Germany','China','Japan','USA'])

# desplegar
ww2_cas

# se pueden utilizar los valores de indices para seleccionar un valor de la serie
ww2_cas['USA']

# podemos utilizar funciones de arreglos

# checar quienes tubieron más de 4 millones de damnificados
ww2_cas[ww2_cas>4000000]

# una serie se puede usar como un dictionario

# checar si USSR se encuentra en la serie
'USSR' in ww2_cas

# convertir una serie en un diccionario de python
ww2_dict = ww2_cas.to_dict()

# desplegar
ww2_dict

# regresar un diccionario a una serie
WW2_Series = Series(ww2_dict)

# desplegar
WW2_Series

# pasando a diccionario los indices tendran las llaves del diccionario en orden
countries = ['China','Germany','Japan','USA','USSR','Argentina']


# redefinir una serie
obj2 = Series(ww2_dict,index=countries)

# desplegar
obj2

# se puede utilizar isnull y notnull para encontrar huecos de informacion
pd.isnull(obj2)

#obj2.isnull() 

# al igual para el opuesto
pd.notnull(obj2)

#obj2.notnull()

# desplegar la serie de WW2 nuevamente
WW2_Series

# checar las serie con el valor de Argentina
obj2

# Now we can add and pandas automatically aligns data by index
WW2_Series + obj2

# podemos nombrar una serie
obj2.name = "World War 2 Casualties"

# desplegar
obj2

# tambien se puede nombrar los indices
obj2.index.name = 'Countries'

# desplegar
obj2