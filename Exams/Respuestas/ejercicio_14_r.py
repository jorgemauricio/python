#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 17 16:17:25 2017

@author: jorgemauricio

- 	Definir una clase llamada Circulo que pueda ser construida por el radio.
    La clase Circulo debe de contener un método que pueda calcular el área
"""

class Circulo:
    def __init__(self, r):
        self.radius = r

    def calcularArea(self):
        return self.radius**2*3.1416
