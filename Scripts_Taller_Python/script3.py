# -*- coding: utf-8 -*-
"""
Created on Thu Feb 02 16:31:10 2017

I Curso de Introducción a Python Orientado a la Resolución 
de Problemas de Optimización en Ingeniería

Script 3
@authors:  DanyGR MarioDM IgnacioGP
"""


# Los bucles For en Python son un poco diferentes a otros lenguajes de
# programación. Los bucles For recorre iterables tales como listas o cadenas

lista1 = [1, 2, 3, 4]
for i in lista1:
    print i
print "\n"
cadena1 = "hola mundo"
for i in cadena1:
    print i
    
#%% Otro ejemplo

for i in range(0,10):
    print i

#%% podemos dar un paso 

for i in range(0,10,2):
    print i

#%% incluso el paso puede ser negativo entonces iremos para atrás

for i in range(0,-10,-2):
    print i

#%% aqui no ponemos el valor de inicio

for i in range(10):
    print i

#%% incluso si no queremos hacer nada con la variable auxiliar
#podemos utilizar _

for _ in range(10):
    print "hola"
    
#%% podemos hacerlo todo el bucle en una sola linea!!!!!! --> List comprenhension
    
[x * x for x in range(10)] # ojo! solo es válido si el resultado es una lista

#%% Este ejemplo va dar un error de sintaxis

[print x for x in range(10)] # el resultado de esto no es una lista
    
#%%
# Ejemplo que modifica el contenido de una lista

lista2 = [0, 0, 0, 0]

for i in range(0, len(lista2)):
    lista2[i] = 1

print lista2

#%%
# vamos a complicar un poco el asunto, vamos a imprimir las parejas
#key.value de un diccionario

dir1 = {'Nombre': "Antonio", 'Edad':32}

for i in dir1.items():
    print i[0], i[1]
    