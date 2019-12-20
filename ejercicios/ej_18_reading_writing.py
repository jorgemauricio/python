#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 17 16:17:25 2017

@author: jorgemauricio
"""

# librerias
import numpy as np
from pandas import Series,DataFrame
import pandas as pd

# se pueden abrir archivos csv como dataframes
dframe = pd.read_csv('data/ej_18_data.csv')

# desplegar
dframe

# tambien se puede utilizr read_table para leer una tabla con una ',' como delimitante
dframe = pd.read_table('data/ej_18_data.csv',sep=',')

# desplegar
dframe

# si no queremos que el titulo sea la primer fila
dframe = pd.read_csv('data/ej_18_data.csv',header=None)

# desplegar
dframe

# tambien podemos delimitar el numero de filas a leer
pd.read_csv('data/ej_18_data.csv',header=None,nrows=2)

# desplegar
dframe

# escribimos el dataframe en un archivo de texto
dframe.to_csv('data/mytextdata_out.csv')

# veras el archivo en donde se ejecuta python

# tambien se pueden utilizar otros metodos

# podemos importar el modulo sys
import sys 

# usando sys.stdout se puede ver lo que se va a guardar sin necesidad de escribir el archivo
dframe.to_csv(sys.stdout,sep='_')

# un ejemplo para entender el delimitante
dframe.to_csv(sys.stdout,sep='?')

# podemos elegir solo las columnas que deseamos
dframe.to_csv(sys.stdout,columns=[0,1,2])