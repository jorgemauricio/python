#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 17 16:17:25 2017

@author: jorgemauricio
"""

# librerias
import pandas as pd
from pandas import Series, DataFrame
import numpy as np

# crear dos dataframes
df_left = DataFrame({'key': ['X','Y','Z','X','Y'],
                  'data': range(5)})
df_right = DataFrame({'group_data': [10, 20]}, index=['X', 'Y'])

# desplegar
df_left

# desplegar
df_right

# utilizar el comando merge, utilizando la llame del dataframe de la izquierda y el indice del dataframe de la derecha
pd.merge(df_left,df_right,left_on='key',right_index=True)

# tambien podemos utilizar la union utilizando el atributo outer
pd.merge(df_left,df_right,left_on='key',right_index=True,how='outer')

# Avanzado

# utilizando indices jerarquicos
df_left_hr = DataFrame({'key1': ['SF','SF','SF','LA','LA'],
                   'key2': [10, 20, 30, 20, 30],
                   'data_set': np.arange(5.)})
df_right_hr = DataFrame(np.arange(10).reshape((5, 2)),
                   index=[['LA','LA','SF','SF','SF'],
                          [20, 10, 10, 10, 20]],
                   columns=['col_1', 'col_2'])


# desplegar
df_left_hr

# desplegar indices jerarquicos
df_right_hr

# utilizamos el metodo merge del dataframe de la izquierda con sus llaves y los indices del dataframe de la derechaNow we can merge the left by using keys and the right by its index
pd.merge(df_left_hr,df_right_hr,left_on=['key1','key2'],right_index=True)

# utilizamos la funcion outer
pd.merge(df_left_hr,df_right_hr,left_on=['key1','key2'],right_index=True,how='outer')