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

#crear un array
years = [1990,1991,1992,2008,2012,2015,1987,1969,2013,2008,1999]

# podemos separar estos años en decadas
decade_bins = [1960,1970,1980,1990,2000,2010,2020]

# utilizamos la funcion cut, para crear un objeto de categoria
decade_cat = pd.cut(years,decade_bins)

# desplegar
decade_cat

# podemos ver las caterorias usando .categories
decade_cat.categories

# para ver cuantos valores existen en cada categoria
pd.value_counts(decade_cat)