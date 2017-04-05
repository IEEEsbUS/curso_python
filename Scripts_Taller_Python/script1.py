# -*- coding: utf-8 -*-
"""
Created on Thu Feb 02 16:31:10 2017

I Curso de Introducción a Python Orientado a la Resolución 
de Problemas de Optimización en Ingeniería

Script 1
@authors:  DanyGR MarioDM IgnacioGP
"""

#%%
# Aqui comienza el scrit que está vacio
 
print "Hola mundo"
#%%
 
# vamos a jugar un poco con listas
 
l1 = [1, 2, 3, 4]
 
print "Hemos definido la lista %s" % l1 # las listas se imprimen con %s
print "La longitud de la lista es %d" % len(l1) 
 
l1.append(5) # vetemos un nuevo valor en la lista
 
print "La lista queda ahora como %s" % l1
 
print "El ultimo valor de la lista es %d" % l1[len(l1)-1]
 
l2 = ['a', 'b', 'c'] # una lista de caracteres
 
print "Otra lista %s" % l2
 
#%%
# vamos a definir un diccionario
 
dir1 = {'Nombre': "Antonio", 'Edad':32}
 
print "Diccionario %s" % dir1
 
print dir1.values()
 
#%%
# un poco de cadenas...
 
cad1 = "Hay una leyenda que recorre el mundo entero ..."
print cad1
 
print "La longitud de la cadena es %d" % len(cad1) 
print "El numero de veces que aparece 'e' es  %d" % cad1.count('e')