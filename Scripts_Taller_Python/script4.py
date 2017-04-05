# -*- coding: utf-8 -*-
"""
Created on Tue Jul 26 22:46:42 2016

I Curso de Introducción a Python Orientado a la Resolución 
de Problemas de Optimización en Ingeniería

Script 4

Este script sirve de introducción a los bucles while en Python
y otros sentencias útiles para bucles en general

@author: DanyGR MarioDM IgnacioGP
"""
#%%
i = 0
while i < 4:
    print i
    i = i + 1 

#%%

for i in range(0,4):
    if i == 2:
        continue
    else:
        print i

#%%

for i in range(0,4):
    if i == 2:
        break
    else:
        print i

#%%

for letter in "Python": 
   if letter == 'h':
      pass
      print "sentencia pass"
   print "Letra actual :", letter # otra forma de imprimir en Python

print "Se acabo!"