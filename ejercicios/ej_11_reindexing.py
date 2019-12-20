#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 17 16:17:25 2017

@author: jorgemauricio
"""

# librerias
import numpy as np
from pandas import Series, DataFrame
import pandas as pd
from numpy.random import randn

# crear una nueva serie
ser1 = Series([1,2,3,4],index=['A','B','C','D'])

# desplegar
ser1

# llamar reindex para acomodar los indices
ser2 = ser1.reindex(['A','B','C','D','E','F'])

# desplegar
ser2

# agregar nuevos valores a los indices
ser2.reindex(['A','B','C','D','E','F','G'],fill_value=0)

# usando un metodo particular para llenar los valores
ser3 = Series(['USA','Mexico','Canada'],index=[0,5,10])

# desplegar
ser3

# se puede usar un llenado para interpolar los valores entre indices
ser3.reindex(range(15),method='ffill')

# Reindexing renglones, columnas o ambos

# crear un dataframe con valores aleatorios
dframe = DataFrame(randn(25).reshape((5,5)),index=['A','B','D','E','F'],columns=['col1','col2','col3','col4','col5'])

# desplegar
dframe

# olvidamos colocar C
dframe2 = dframe.reindex(['A','B','C','D','E','F'])

# tambien se puede reindezar columnas
new_columns = ['col1','col2','col3','col4','col5','col6']

dframe2.reindex(columns=new_columns)