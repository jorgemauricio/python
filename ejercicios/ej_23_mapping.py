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

# vamos a crear un dataframe con las ciudades con mayor elevación de USA
dframe = DataFrame({'city':['Alma','Brian Head','Fox Park'],
                    'altitude':[3158,3000,2762]})

# desplegar
dframe

# podemos agregar una columna para cada uno de los stados utilizando la funcion mapping
state_map={'Alma':'Colorado','Brian Head':'Utah','Fox Park':'Wyoming'}

# mapeando la información en nuestro dataframe
dframe['state'] = dframe['city'].map(state_map)

# desplegar el resultado
dframe