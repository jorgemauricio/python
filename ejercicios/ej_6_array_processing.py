#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 17 16:17:25 2017

@author: jorgemauricio
"""

# librerias
import numpy as np

import matplotlib.pyplot as plt
%matplotlib inline

# valores para un lado de la malla
points = np.arange(-5,5,0.01)

# crear malla
dx,dy=np.meshgrid(points,points)

# desplear un lado de la malla
dx

# evaluar una funcion
z = (np.sin(dx) + np.sin(dy))

# desplegar resultdo de z
z

# desplegar el arreglo de 2d
plt.imshow(z)

# desplegar la barra de colores
plt.colorbar()

# colocar un titulo a la grafica
plt.title("GraficaP sin(x)+sin(y)")

#%% desplegar gráfico
plt.show()

# numpy.where
answer2 = np.where(condition,A,B)

# desplegar
answer2

# usar np.where en un arreglo 2d
from numpy.random import randn
arr = randn(5,5)

# desplegar arr
arr

# donde el arreglo es menor a 0, colocar un 0, si no dejar el valor
np.where(arr < 0,0,arr)

# Other Statistical Processing
arr = np.array([[1,2,3],[4,5,6],[7,8,9]])

# desplegar
arr

# suma
arr.sum()

# sumatoria de una sola columna
arr.sum(0)

# media
arr.mean()

# desviacion estandar
arr.std()

# Varianza
arr.var()

# arreglos con valores condicionales
bool_arr = np.array([True,False,True])

# para cualquier valor verdadero
bool_arr.any()

# para todos los valores verdaderos
bool_arr.all()

# Ordenar

#  arreglo aleatorio
arr = randn(5)

# desplegar
arr

# ordenar
arr.sort()

# desplegar
arr

# valores unicos
countries = np.array(['France', 'Germany', 'USA', 'Russia','USA','Mexico','Germany'])

np.unique(countries)