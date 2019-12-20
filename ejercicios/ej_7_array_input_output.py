#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 17 16:17:25 2017

@author: jorgemauricio
"""

# librerias
import numpy as np

# crear arreglo
arr = np.arange(5)

# guardar el arreglo en formato binario (extension .npy)
np.save('my_array',arr)

# cambiar arr
arr1 = np.arange(10)

# desplegar
arr

# cargar el arreglo original
np.load('my_array.npy')

# guardar multiples arreglos en un archivo zip
np.savez('two_arrays.npz',x=arr,y=arr1)

# cargar multiples arreglos
archive_array = np.load('two_arrays.npz')

# desplegar
archive_array['x']

# remover arreglos de la memoria
rm my_array.npy

rm two_arrays.npz

# guardar y cargar archivos de texto
arr = np.array([[1,2,3],[4,5,6]])

np.savetxt('my_test_text.txt',arr,delimiter=',')

arr = np.loadtxt('my_test_text.txt',delimiter = ',')

arr
