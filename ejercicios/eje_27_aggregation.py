#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 17 16:17:25 2017

@author: jorgemauricio
"""

# librerias
import numpy as np
import pandas as pd
from pandas import Series,DataFrame

# Agregacion consiste en operaciones que resultan en un dato escalar (ej. mean(),sum(),count(), etc)

# utilizamos el archivo ej_27_data.csv del folder data, cabe mencionar que esta información esta separada por ';'
dframe_wine = pd.read_csv('data/ej_27_data.csv',sep=';')

# mostramos un pequeño avance de la informacion
dframe_wine.head()

# si queresmos conocer el contenido promedio de alcohol en el vino
dframe_wine['alcohol'].mean()

# Ese fue un ejemplo de agregacion, por que no crear uno propio
def max_to_min(arr):
    return arr.max() - arr.min()

# Agrupar los vinos por la columna "quality"
wino = dframe_wine.groupby('quality')

# desplegar
wino.describe()

# ahora podemos utilizar nuestra proopia funcion, toma el valor maximo de la columna y le resta el valor minimo
wino.agg(max_to_min)

# podemos pasar metodos mediante por medio de texto
wino.agg('mean')

# regresemos al dataframe original
dframe_wine.head()

# Let's adda  quality to alcohol content ratio
dframe_wine['qual/alc ratio'] = dframe_wine['quality']/dframe_wine['alcohol']

# Show
dframe_wine.head()