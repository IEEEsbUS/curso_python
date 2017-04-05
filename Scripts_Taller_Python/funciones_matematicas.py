# -*- coding: utf-8 -*-
"""
Created on Mon Aug 08 01:03:47 2016

I Curso de Introducción a Python Orientado a la Resolución 
de Problemas de Optimización en Ingeniería

Funciones_matematicas: Módulo de ejemplo de funciones matemáticas

@authors: DanyGR MarioDM IgnacioGP
"""

def funcion_suma(a,b):
    suma = a + b
    return suma

def funcion_resta(a,b):
    resta = a - b
    return resta

def funcion_multiplicacion(a,b):
    multiplicacion = a * b
    return multiplicacion

def funcion_division(a,b):
    if b != 0:
        return float(a)/float(b)
    else:
        print "división por cero"

