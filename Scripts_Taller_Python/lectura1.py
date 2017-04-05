# -*- coding: utf-8 -*-
"""
Created on Wed Mar 01 16:26:00 2017

I Curso de Introducción a Python Orientado a la Resolución 
de Problemas de Optimización en Ingeniería

Lectura1:

Ejemplo de lectura de un archivo de texto. 

@authors: DanyGR MarioDM IgnacioGP
"""

# Leemos el fichero linea a linea

fichero = open("song.txt", 'r')

for i, line in enumerate(fichero):
    print line
    numero_lineas = i
 
print "numero de lineas del fichero:", numero_lineas 

#%% Vamos a complicar un poco mas el asunto

for line in fichero:
    palabras = line.split(" ") # separamos las lineas en palabras
    for palabra in palabras:
        print palabra # imprimimos palabra a palabra



