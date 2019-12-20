#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 17 16:17:25 2017

@author: jorgemauricio

Instrucciones
	1. Elevar al cuadrado una lista dada por el usuario de 10 elementos,
    se debe de mostrar la lista original y la lista elevada al cuadrado.
    Ej.
    a = [1,2,3,4,5,6,7,8,9,10]
    R = [1,4,9,16,25,36,49,64,81,100]
"""

valores = []

print("Introduce un valor entero númerico \nSi deseas terminar con el proceso ingresa *no*")

while True:
	valor = input("Introduce un valor: ")
	if valor == "no":
		break
	else:
		valor = int(valor)
		valores.append(valor)

print("Valores originales: \n", valores)
print("Valores al cuadrado: ")
print([x**2 for x in valores])
