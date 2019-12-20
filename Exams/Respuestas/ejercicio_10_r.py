#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 17 16:17:25 2017

@author: jorgemauricio

- 	Escribe un programa que toma una frase ingresada por el usuario y contabilice el numero
	de letras y números que contiene la frase.
	Ej
	Hola mundo! 1234
	Números = 4
	Letras = 9
"""

s = input("Ingresa una frase: ")
d={"Numeros":0, "Letras":0}
for c in s:
    if c.isdigit():
        d["Numeros"]+=1
    elif c.isalpha():
        d["Letras"]+=1
    else:
        pass
print ("Números", d["Numeros"])
print ("Letras", d["Letras"])
