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


# ahora aprenderemos a lidear cuando falta informacion

data = Series(['one','two', np.nan, 'four'])

# desplegar informacion
data

# encontrar la informacion faltante
data.isnull()

# eliminar la informacion nula
data.dropna()

# en un DataFrame tenemos que ser mas cuidadosos
dframe = DataFrame([[1,2,3],[np.nan,5,6],[7,np.nan,9],[np.nan,np.nan,np.nan]])

# desplegar
dframe

clean_dframe = dframe.dropna()

# desplegar
clean_dframe

# cuando en una fila existe un valor NA, se elimina

# tambien podemos especificar que solo elimine las filas con todos sus valores nulos
dframe.dropna(how='all')

# o podemos especificar que elimine las columnas con infomracion nula
dframe.dropna(axis=1)

# esto tiene que eliminar todas las columnas ya que cada columna contiene un valor nulo
# tambien podemos condicionar los valores nulos

# crear una serie
dframe2 = DataFrame([[1,2,3,np.nan],[2,np.nan,5,6],[np.nan,7,np.nan,9],[1,np.nan,np.nan,np.nan]])

# desplegar
dframe2

# eliminar cualquier fila que tenga menos de 2 datos
dframe2.dropna(thresh=2)

# eliminar cualquier fila que tenga menos de 3 datos
dframe2.dropna(thresh=3)

# tambien podemos llegar todos los valores nulos
dframe2.fillna(1)