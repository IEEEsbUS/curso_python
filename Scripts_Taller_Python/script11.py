# -*- coding: utf-8 -*-
"""

I Curso de Introducción a Python Orientado a la Resolución 
de Problemas de Optimización en Ingeniería

Script11

Módulos en Python

@authors: DanyGR MarioDM IgnacioGP
"""
#%%
import random
# aquí tengo que utilizar random como palabra clave para llamar a las
# funciones del módulo random. Todas las funciones están accesibles

lista = list()
for i in range(0,10):
    lista.append(random.random())
    
print lista

#%% Ahora utilizo la palabra clave ran para acceder a las funciones
# también están todas las funciones accesibles

import random as ran

lista = list()
for i in range(0,10):
    lista.append(ran.random())
    
print lista

#%% Ahora sólo vamos a importar solo la función uniform

from random import uniform
# uniform nos devuelve un valor aleatorio entre dos límites

lista = list()
for i in range(0,10):
    lista.append(uniform(0,10)) 
    
print lista

#%% Ahora importamos todas las funciones

from random import*

lista = list()
for i in range(0,10):
    lista.append(uniform(0,10)) 
    
print lista
