#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 17 16:17:25 2017

@author: jorgemauricio
"""

# librerias
import numpy as np

# crear arreglo
arr = np.arange(0,11)

# desplegar
arr

# obtener el valor en un indice determinado
arr[8]

# valores de un rango
arr[1:5]

# valores de un rango 
arr[0:5]

# asignar valores a un rango
arr[0:5]=100

# desplegar
arr

# resetear arreglo
arr = np.arange(0,11)

# desplegar
arr

# partir arreglos
slice_of_arr = arr[0:6]

# desplegar parte del arreglo 
slice_of_arr

# cambiar valores en la parte del arreglo
slice_of_arr[:]=99

# desplegar parte del arreglo
slice_of_arr

# Los cambios ocurren en el arreglo original
arr

# la informacion es copiada, se despliega el arreglo original para evitar problemas de memoria

# To get a copy, need to be explicit
arr_copy = arr.copy()

arr_copy

# indexar un arreglo 2D
arr_2d = np.array(([5,10,15],[20,25,30],[35,40,45]))

# desplegar
arr_2d

# indexacion de columna
arr_2d[1]


# formato arr_2d[row][col] o arr_2d[row,col]

# obtener un valor individual
arr_2d[1][0]

# obtener un valor individual
arr_2d[1,0]

# Cortar un arreglo 2d

# Forma (2,2) desde la esquina superiror derecha
arr_2d[:2,1:]

# Forma de la fila inferior
arr_2d[2]

# Forma de la fila inferior
arr_2d[2,:]

# Indexacion compleja

# crear matriz
arr2d = np.zeros((10,10))

# longitud del arreglo
arr_length = arr2d.shape[1]

# determinar valores
for i in range(arr_length):
    arr2d[i] = i
    
# desplegar
arr2d
