# -*- coding: utf-8 -*-
"""
Created on Tue Aug 09 12:46:00 2016

I Curso de Introducción a Python Orientado a la Resolución 
de Problemas de Optimización en Ingeniería

Script 14: 

Módulo random para generar números aleatorios

@authors: DanyGR MarioDM IgnacioGP
"""

import random

# generar un número aleatorio del 0 al 1.0

print random.random() # cada vez que lo ejecuteamos genera un número distinto

#%% numero aleatorio entero entre dos números

print random.randint(20,30) # los límites son 20 y 30

#%% con un número flotante

print random.uniform(20, 30)

#%% números aleatorios basados en funciones de probabilidad

print random.normalvariate(10, 3) # media, desviación típica

