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

# crear una matriz
arr1 = np.arange(9).reshape((3,3))

# desplegar
arr1

# concatenar en el eje 1
np.concatenate([arr1,arr1],axis=1)

# concatenar en el eje 0
np.concatenate([arr1,arr1],axis=0)

# ejemplo en pandas

# creamos dos series sin solapamiento
ser1 =  Series([0,1,2],index=['T','U','V'])
ser2 = Series([3,4],index=['X','Y'])

# concatenamos las series (default es axis=0)
pd.concat([ser1,ser2])

# concatenando la informacion en el axis 1 generamos un dataframe
pd.concat([ser1,ser2],axis=1)

# podemos espeficifar los ejes que se van a utilizar
pd.concat([ser1,ser2],axis=1,join_axes=[['U','V','Y']])

# crear dos dataFrames
dframe1 = DataFrame(np.random.randn(4,3), columns=['X', 'Y', 'Z'])
dframe2 = DataFrame(np.random.randn(3, 3), columns=['Y', 'Q', 'X'])

# concatenar los dataframes
pd.concat([dframe1,dframe2])

# si el indice no es importante podemos ignorar el valor con el atributo ignore_index
pd.concat([dframe1,dframe2],ignore_index=True)