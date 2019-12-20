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

# crear un data [1,2,np.nan],[np.nan,3,4]])
arr = np.array([[1,2,np.nan],[np.nan,3,4]])
dframe1 = DataFrame(arr,index=['A','B'],columns = ['One','Two','Three'])

# desplegar
dframe1

# metodo sum()
dframe1.sum()

# el metodo ignora valores NaN

# tambien se puede hacer sobre filas
dframe1.sum(axis=1)

# valores minimos y maximos
dframe1.min()

# tambien de los indices
dframe1.idxmin()

# se puede usar de igual manera con idxmax()

# desplegar
dframe1

# suma acumulativa
dframe1.cumsum()

# el metodo describe() permite obtener un resumen estadistico
dframe1.describe()

# tambien podemos obtener información de correlacion y covarianza

# checar la correlacion y covarianza de la bolsa de valores

# el modulo pandas puede obtener informacion de la web
from pandas_datareader import data, wb
import pandas_datareader as pdr

# establecer el tiempo para la fecha de entrada
import datetime

# obtener precios de cierre
prices = pdr.get_data_yahoo(['XOM','BP'], 
                               start=datetime.datetime(2010, 1, 1), 
                               end=datetime.datetime(2013, 1, 1))['Adj Close']
# desplegar un previo de la informacion
prices.head()

# obtener los valores de cambio

volume = pdr.get_data_yahoo(['XOM','BP'], 
                               start=datetime.datetime(2010, 1, 1), 
                               end=datetime.datetime(2013, 1, 1))['Volume']

#S desplegar un previo de la informacion
volume.head()

# obtener el valor de regreso
rets = prices.pct_change()

# obtener la correlacion 
corr = rets.corr

# checar los precios en base al tiempo
prices.plot()

import seaborn as sns
import matplotlib.pyplot as plt
%matplotlib inline

# como imaginabamos existe una fuerte correlacion
sns.heatmap(rets.corr())