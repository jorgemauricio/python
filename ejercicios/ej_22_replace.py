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

# crear una serie
ser1 = Series([1,2,3,4,1,2,3,4])

# desplegar
ser1

# usando replace .replace(valor a ser remplazado, nuevo valor)
ser1.replace(1,np.nan)

# podemos incluir listas
ser1.replace([1,4],[100,400])

# y tambien dictionarios
ser1.replace({4:np.nan})