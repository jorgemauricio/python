#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 17 16:17:25 2017

@author: jorgemauricio

- 	Define una función en la cual se acepten dos variables string, evalue cual
    de las dos funciones tiene el número mayor de caracteres y la imprima, si
    las dos palabras tienen un número igual de caracteres, se deben de imprimir
    las dos palabras
    Ej.
    hola
    adios

    Resultado:
    adios
"""

def printValue(s1,s2):
	len1 = len(s1)
	len2 = len(s2)
	if len1>len2:
		print (s1)
	elif len2>len1:
		print(s2)
	else:
		print(s1)
		print(s2)
