#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 17 16:17:25 2017

@author: jorgemauricio

Instrucciones

- Crear un programa que imprima el factorial de un numero determinado por el usuario
- Validar si el número es menor a 0
- Validar si el número es igual a 0

"""
num = int(input("Ingresa un numero: "))

factorial = 1

# check if the number is negative, positive or zero
if num < 0:
   print("Lo siento, factoriales no existen para numeros negativos")
elif num == 0:
   print("El factorial de 0 es 1")
else:
   for i in range(1,num + 1):
       factorial = factorial*i
   print("El factorial de {} es {}".format(num, factorial))
