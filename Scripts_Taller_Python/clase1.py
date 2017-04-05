# -*- coding: utf-8 -*-
"""
Created on Mon Oct 10 11:52:09 2016

I Curso de Introducción a Python Orientado a la Resolución 
de Problemas de Optimización en Ingeniería

clase1:

Script basico de definicion de clases y su uso

@authors:DanyGR MarioDM IgnacioGP
"""

class Persona(object): #normalmente las clases se definene en mayúsucula
        """Definición de una clase persona""" #Docstring
        def __init__(self, altura, peso, edad):
            """Inicialización del objeto persona"""
            self.altura=altura #Ojo todas estas variables son públicas
            self.peso=peso
            self.edad=edad
            self.profesion="" #ésta la inicializaremos nosotros después.
            self.lista_tareas=[]
            self.privado=1 #este atributo es privado no se puede acceder a él desde fuera
            
        def suma_tarea (self, tarea): #incluimos una nueva tarea
            self.lista_tareas.append(tarea)
            self._metodo_privado(tarea)
            
        def elimino_tarea(self, tarea): #eliminamos una de las tareas
            self.lista_tareas.remove(tarea)
            
        def _metodo_privado(self, item):
            print "Incluyo item %s" %item
            
#Generamos un nuevo objeto y lo inicializamos con ciertos valores
Daniel=Persona(1.78, 74, 34)

print "Altura %f" %Daniel.altura
print "Altura %.2f" %Daniel.altura

#Profesión
Daniel.profesion="Ingeniero"

print "Profesion %s" %Daniel.profesion

#tareas

lis_tar=["compra semana", "paper", "preparar practicas"]

for tar in lis_tar:
    Daniel.suma_tarea(tar)
    
print "Tareas pendientes %s" %Daniel.lista_tareas


#Imprimimos el doctstring

print Daniel.__doc__
 