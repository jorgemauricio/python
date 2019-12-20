#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 17 16:17:25 2017

@author: jorgemauricio
"""

# librerias
import numpy as np

# hacer una lista
arr1 = [1,2,3,4]

# crear el arreglo de numpy
myArr1 = np.array(arr1)

#Imprimir
myArr1

# hacer otra lista
arr2 = [11,22,33,44]

# hacer una lista de listas
myList = [arr1,arr2]

# hacer un arreglomultimimencional
myArr2 = np.array(myList)

# desplegar arreglo
myArr2

# obtener la dimension del arreglo
myArr2.shape

# desplegar el tipy de datos del arreglo 
myArr2.dtype

# hacer arreglos especiales 
# ceros
np.zeros(5)

# unos
np.ones((5,5))

# vacio
np.empty(5)
np.empty((3,4))

# arreglo de identidad
np.eye(5)

# Using a range
np.arange(5)
