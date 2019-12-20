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

# crear una series
ser1 = Series(np.arange(3),index=['a','b','c'])

# desplegar
ser1

# elimiar un indice
ser1.drop('b')

# en un dataframe podemos eliminar el valor de un eje
dframe1 = DataFrame(np.arange(9).reshape((3,3)),index=['SF','LA','NY'],columns=['pop','size','year'])

# desplegar
dframe1

# eliminar una columna
dframe1.drop('LA')

# o una columna
# necesitamos declarar que el axis = 1
dframe1.drop('year',axis=1)