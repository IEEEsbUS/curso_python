# -*- coding: utf-8 -*-
"""
Created on Thu Aug 04 14:46:47 2016

I Curso de Introducción a Python Orientado a la Resolución 
de Problemas de Optimización en Ingeniería

Script6
Segundo script con funciones

@authors: DanyGR MarioDM IgnacioGP
"""

# definimos la funcion suma
def suma (a, b):
	resultado = a + b
	return resultado

# sumamos dos numeros
num1 = 10
num2 = 15

res = suma(num1, num2)
print res

# sumamos dos cadenas

cadena1 = "hola"
cadena2 = " mundo!"

res = suma(cadena1, cadena2)
print res

# sumamos dos listas

lista1 = [1, 2, 3]
lista2 = [4, 5, 6]

res = suma(lista1, lista2) # ojo que estamos concantenando!!!
print res

