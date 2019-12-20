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

# indices como objetos
my_ser = Series([1,2,3,4],index=['A','B','C','D'])

# Obtener los indices
my_index = my_ser.index

# desplegar
my_index

# obtener valores mediante rangosCan grab index ranges
my_index[2:]

# si tratamos de cambiar un index, que pasa?
my_index[0] = 'Z'

# Marca Error. Los indices no son mutables