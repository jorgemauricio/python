#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 17 16:17:25 2017

@author: jorgemauricio

Instrucciones

	1. Ordenar la siguiente lista de valores por medio de ciclos y/o validaciones
	arreglo = [54,26,93,17,77,31,44,55,20]
    Resultado
	arreglo = [54,26,93,17,77,31,44,55,20]
    arreglo = [17, 20, 26, 31, 44, 54, 55, 77, 93]
"""

a = [54,26,93,17,77,31,44,55,20]

def bubbleSort(a):
    for passnum in range(len(alist)-1,0,-1):
        for i in range(passnum):
            if alist[i]>alist[i+1]:
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp

alist = [54,26,93,17,77,31,44,55,20]
bubbleSort(alist)
print(alist)
