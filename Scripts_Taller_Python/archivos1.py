# -*- coding: utf-8 -*-
"""
Created on Wed Mar 01 16:26:00 2017

I Curso de Introducción a Python Orientado a la Resolución 
de Problemas de Optimización en Ingeniería

Archivos 1:
    
Script de introducción al módulo os

@authors: DanyGR MarioDM IgnacioGP
"""

import os
    
print "directorio actual", os.getcwd()

dir_actual = os.getcwd()

print "lista de archivos", os.listdir(dir_actual)


lista_archivos = os.listdir(".")

print "IMPRIMIMOS SOLOS LOS .txt"
for archivo in lista_archivos:
    if archivo.endswith('.txt'):
        print archivo

# ejercicio cambiar el código para que haga lo mismo con los .py
# la potencialidad que tiene esto es que podemos analizar datos de distintos
# archivos. Hay muchos programas que nos generan distintos archivos de resultados


#%% método walk
import os
for root, dirs, files in os.walk(".", topdown=False):
    for name in files:
        print(os.path.join(root, name)) # os.path.join sirve para concatenar los path
    for name in dirs:
        print(os.path.join(root, name))
        
# ejercicio crear subdirectorios y comprobar el resultado de la celda