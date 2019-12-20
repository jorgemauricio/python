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

# crear un dataframe
dframe1 = DataFrame({'key':['X','Z','Y','Z','X','X'],'data_set_1': np.arange(6)})

# desplegar
dframe1

# crear un segundo dataframe
dframe2 = DataFrame({'key':['Q','Y','Z'],'data_set_2':[1,2,3]})

# desplegar
dframe2

# ya que contamos con dos dataframes podemos usar el metodo merge
# el metodo automaticamente determinara la forma en que se unen los dataframes
pd.merge(dframe1,dframe2)

# no se integran los valores de X

# podemos espedificar que columna utilizar para el merge
pd.merge(dframe1,dframe2,on='key')

# podemos seleccionar la llame de un dataframe determinadom en este caso el del lado izquierdo (dframe1)
pd.merge(dframe1,dframe2,on='key',how='left')

# seleccionando el dataframe de la derecha (dframe2)
pd.merge(dframe1,dframe2,on='key',how='right')

# seleccionando el metodo "outer" genera la union de las dos llaves
pd.merge(dframe1,dframe2,on='key',how='outer')

# los siguientes dataframes contienen mas de una llave
dframe3 = DataFrame({'key': ['X', 'X', 'X', 'Y', 'Z', 'Z'],
                 'data_set_3': range(6)})
dframe4 = DataFrame({'key': ['Y', 'Y', 'X', 'X', 'Z'],
                 'data_set_4': range(5)})

# desplegar el merge
pd.merge(dframe3, dframe4)

# podemos realizar el metodo merge usando varias llaves
# dataframe de la izquierda
df_left = DataFrame({'key1': ['SF', 'SF', 'LA'],
                  'key2': ['one', 'two', 'one'],
                  'left_data': [10,20,30]})

# dataframe de la derecha
df_right = DataFrame({'key1': ['SF', 'SF', 'LA', 'LA'],
                   'key2': ['one', 'one', 'one', 'two'],
                   'right_data': [40,50,60,70]})

# metodo merge
pd.merge(df_left, df_right, on=['key1', 'key2'], how='outer')

# cabe mencionar que los dos dataframes tienen solapamiento en sus llaves (key1 and key2).
# pandas automaticamente añade sufijos
pd.merge(df_left,df_right,on='key1')

# podemos especificar cual queremos que sea el sufijo a utilizar
pd.merge(df_left,df_right, on='key1',suffixes=('_lefty','_righty'))