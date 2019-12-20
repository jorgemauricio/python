#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 17 16:17:25 2017

@author: jorgemauricio
"""

# librerias
import numpy as np
from pandas import Series, DataFrame
import pandas as pd

# DataFrames

# vamos a obtener un poco de informacion, que tal de la NFL?
import webbrowser
website = 'http://en.wikipedia.org/wiki/NFL_win-loss_records'
webbrowser.open(website)

# copiar y leer la informacion
nfl_frame = pd.read_clipboard()

# desplegar
nfl_frame

# podemos tomar los nombres de las columnas con el comando .columns
nfl_frame.columns

# para ver solo informacion de ciertas columnas
DataFrame(nfl_frame,columns=['Team','First Season','Total Games'])

# si mandamos llamar una columna que no existe
DataFrame(nfl_frame,columns=['Team','First Season','Total Games','Stadium'])

# podemos llamar columnas independientemente
nfl_frame.Team

# para columnas con multiples palabras
nfl_frame['Total Games']

# podemos mandar llamar filas mediante indices
nfl_frame.ix[3]

# nfl_frame.loc[3]

# podemos asignar el valor a toda una columna
nfl_frame['Stadium']="Levi's Stadium" # hay que tener mucho cuidado con los '

# desplegar
nfl_frame

#Putting numbers for stadiums
nfl_frame["Stadium"] = np.arange(5)

# desplegar
nfl_frame

# mandar llamar las columnas
nfl_frame.columns

# agrregar una serie al DataFrame
stadiums = Series(["Levi's Stadium","AT&T Stadium"],index=[4,0])

# agregamos los valores al DataFrame
nfl_frame['Stadium']=stadiums

# desplegar
nfl_frame

# borrar columnas
del nfl_frame['Stadium']

# desplegar
nfl_frame

# los DataFrames se pueden construir de diversas maneras, una de ellas es por medio de diccionarios
data = {'City':['SF','LA','NYC'],
        'Population':[837000,3880000,8400000]}

city_frame = DataFrame(data)

# desplegar
city_frame

