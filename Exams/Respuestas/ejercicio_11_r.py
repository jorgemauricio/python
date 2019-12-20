#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 17 16:17:25 2017

@author: jorgemauricio

- 	Escribe un programa que calcule el valor neto de una cuenta de banco basado
	en las transacciones que se ingresan en la consola de comandos.
	Ej:
	D 200
	D 250
	P 300
	D 100
	P 200
	Donde:
	D = Deposito
	P = Pago
	Resultado
	50
"""

import sys
netAmount = 0
while True:
    s = input("")
    if not s:
        break
    values = s.split(" ")
    operation = values[0]
    amount = int(values[1])
    if operation=="D":
        netAmount+=amount
    elif operation=="P":
        netAmount-=amount
    else:
        pass
print("El total de tu cuenta es: {}".format(netAmount))
