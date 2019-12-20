#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 17 16:17:25 2017

@author: jorgemauricio

Instrucciones

- Calcular el área de un triángulo

"""

a = float(input('Primer lado: '))
b = float(input('Segundo lado: '))
c = float(input('Tercer lado: '))

# calculate the semi-perimeter
s = (a + b + c) / 2

# calculate the area
area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
print('El área del triangulo es: {:.2f}'.format(area))
