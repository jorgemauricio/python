#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 17 16:17:25 2017

@author: jorgemauricio
"""

# librerias
import numpy as np
import pandas as pd
from pandas import Series, DataFrame

# generamos un array aleatorio
np.random.seed(12345)

# creamos un dataframe del arreglo aleatorio
dframe = DataFrame(np.random.randn(1000,4))

# desplegamos las primeras 5 filas de la informacion
dframe.head()

# descripcion de la informacion
dframe.describe()

# seleccionamos la primer columna
col = dframe[0]

# validamos que valores son más grandes a 3
col[np.abs(col)>3]

# como realizar esta misma evaluacion en todas las columnas

# utilizamos el metodo "any"
dframe[(np.abs(dframe)>3).any(1)]