# -*- coding: utf-8 -*-
"""
Created on Thu Aug 04 14:46:47 2016

I Curso de Introducción a Python Orientado a la Resolución 
de Problemas de Optimización en Ingeniería

Script7

Funciones y listas

@authors: DanyGR MarioDM IgnacioGP
"""
# modificar los valores de una lista y los pone a todo a cero
def modifica (a):
	for i in range(0, len(a)):
		a[i] = 0
	# OJO NO HEMOS UTILIZADO LA SENTENCIA RETURN	
	
lista = [1, 2, 3, 4]
print "Lista"
print lista

modifica(lista)

print "Lista despues de la funcion"
print lista

# Las listas son objetos enlazados

lista2= lista

print "Lista 2"
print lista2

lista[0] = 10

print "Lista2 cuando he modificado Lista"
print lista2

lista3 = lista[:] # esta es la forma para crea una nueva lista partiendo de lista pero sin estar enlazada
lista[0] = 0

print "Lista modificada de nuevo"
print lista

print "Lista 3"
print lista3

# esto no ocurre con el resto de tipos


