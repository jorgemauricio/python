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

# crear una serie
ser1 = Series(np.arange(3),index=['A','B','C'])

# multiplicar todos los valores por 2
ser1 = 2*ser1

# desplegar
ser1 

# obtener un registro por el nombre del indice
ser1['B']

# o por el indice
ser1[1]

# tambien lo podemos obtener por el rango de indices
ser1[0:3]

# o tomar el valor del indice
ser1[['A','B','C']]

# o por logica
ser1[ser1>3]

# crear una seleccion en el DataFrame
dframe = DataFrame(np.arange(25).reshape((5,5)),index=['NYC','LA','SF','DC','Chi'],columns=['A','B','C','D','E'])

# desplegar
dframe

# seleccionar por el nombre de la columna
dframe['B']

# seleccionar multiples columnas
dframe[['B','E']]

# tambien se puede usar condiciones
dframe[dframe['C']>8]

# o .loc
dframe.loc['A']
