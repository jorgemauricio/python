#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 17 16:17:25 2017

@author: jorgemauricio
"""

# librerias
import numpy as np

# Funciones universales 
arr = np.arange(11)

# desplegar
arr

# raiz cuadrada
np.sqrt(arr)

# calcular el exponencial (e^)
np.exp(arr)

# Funciones binarias requieren dos arreglos

# arreglo aleatorio (distribucion normal)
A = np.random.randn(10)

# desplegar
A

# arreglo aleatorio (distribucion normal)
B = np.random.randn(10)

# desplegar
B

# anadir
np.add(A,B)

# Maximo y minimo de dos arreglos
np.maximum(A,B)

#