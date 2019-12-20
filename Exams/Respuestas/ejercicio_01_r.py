#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 17 16:17:25 2017

@author: jorgemauricio

Instrucciones
	1. Solicita al usuario las variables x y y, las cuales posteriormente utilizaras
	para comparar en un método si son: ==, > o <
	2. Se debe de imprimir los resultados dentro del método
"""

x = int(input("valor de x: "))
y = int(input("valor de y: "))

if x == y:
    print("x y y tienen el mismo valor")
elif x > y:
    print("x es mayor a y")
else:
    print("y es mayor a x")
