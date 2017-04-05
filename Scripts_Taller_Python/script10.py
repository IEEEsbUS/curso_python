# -*- coding: utf-8 -*-
"""
I Curso de Introducción a Python Orientado a la Resolución 
de Problemas de Optimización en Ingeniería

Script 10


@author:  DanyGR MarioDM IgnacioGP
"""

# vamos a ver la diferencia entre variables globales y locales en python

d = 5

def funcion1(a, b):
	global d
	c = a + b
	d = c
	return c

# la variable d no es accesible fuera de la funcion

print "valor de d antes de la funcion %d" %d
resultado = funcion1(5, 9)
print resultado
print "valor de d despues de la funcion es %d" % d

# 1 ejecutar el script con global d comentado
# 2 descomentar la linea de codigo 17
# 3 comentar la linea de codigo 14
