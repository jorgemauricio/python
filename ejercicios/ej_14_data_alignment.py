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

# generar dos series, primer serie
ser1 = Series([0,1,2],index=['A','B','C'])

# desplegar
ser1

# segunda serie
ser2 = Series([3,4,5,6],index=['A','B','C','D'])

# desplegar 
ser2 

# que pasa cuando se agregan dos series
ser1 + ser2

# verificar que los valores NAN se añaden automaticamente

# ahora con DataFrames
dframe1 = DataFrame(np.arange(4).reshape(2,2),columns=list('AB'),index=['NYC','LA'])

# desplegar
dframe1

# segundo DataFrame
dframe2 = DataFrame(np.arange(9).reshape(3,3),columns=list('ADC'),index=['NYC','SF','LA'])

# desplegar
dframe2

# que pasa cuando los agregamos

dframe1 + dframe2


# que pasa si queremos remplazar los valores Nan
# usamos la funcion .add()
dframe1.add(dframe2,fill_value=0)

# ahora podemos ver que los valores estan completos, pero aun existen valores SF y B sin valores