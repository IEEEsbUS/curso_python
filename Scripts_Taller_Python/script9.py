# -*- coding: utf-8 -*-
"""

I Curso de Introducción a Python Orientado a la Resolución 
de Problemas de Optimización en Ingeniería

Script9

Funciones lambda

@author:  DanyGR MarioDM IgnacioGP
"""
#%%
y= lambda x: x+2 # asignamos la funcion a una variable

z = y(5)

print z

h = y(9)

print h

#%%

# ejercicio propuesto, crear una funcion lambda que calcule el cuadrado de un numero

# podemos hacer funciones lambda con dos variables
y = lambda x, y: x + y

t = y(5,4)

print t
