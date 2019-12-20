#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 17 16:17:25 2017

@author: jorgemauricio
"""

# librerias
import numpy as np

# crear arreglo
arr = np.arange(50).reshape((10,5))

# desplegar
arr

# transponer
arr.T

# Producto punto de dos matrices
np.dot(arr.T,arr)

# Para una matriz 3d
arr3d = np.arange(50).reshape((5,5,2))

# desplegar
arr3d

# transponer una matriz 3d
arr3d.transpose((1,0,2))
