# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 13:34:46 2024

@author: pc
"""
import random
import math
import csv
import numpy as np
import pandas as pd


# # Ejercicio1--------------------------------------

def leer_parque(nombre_archivo, parque)->list:
    lista_diccionarios = []
    with open(nombre_archivo, 'rt', encoding="utf-8") as f:
        filas = csv.reader(f)
        encabezado = next(filas)
        for fila in filas :
            if parque in fila:
                lista_diccionarios.append(dict(zip(encabezado, fila)) )
    return lista_diccionarios 
# a = leer_parque("arbolado-en-espacios-verdes.csv", "GENERAL PAZ")  
# len(leer_parque("arbolado-en-espacios-verdes.csv", "GENERAL PAZ")) #Da 690 


# # Ejercicio2--------------------------------------
# Devuelve el conjunto de especies(columna: 'nombre_com') de c/arbol
def especies(lista_arboles)->set:
    conjunto_especies = set() # es un conjunto de elementos unicos
    for arbol in lista_arboles:
        conjunto_especies.add(arbol["nombre_com"])
    return conjunto_especies
# a = leer_parque("arbolado-en-espacios-verdes.csv", "GENERAL PAZ")
# especies(a)
# a es lista_arboles


# # Ejercicio3--------------------------------------
def contar_ejemplares(lista_arboles)->dict:
    conjunto_especies = especies(lista_arboles) # es un conjunto de elementos unicos
    listaValores = [0]*len(conjunto_especies)
    diccionario_ejemplares = dict(zip(conjunto_especies,listaValores.copy()))   
    for arbol in lista_arboles:
        diccionario_ejemplares[arbol["nombre_com"]]+=1
    return diccionario_ejemplares
# a = leer_parque("arbolado-en-espacios-verdes.csv", "GENERAL PAZ")
# contar_ejemplares(a)


# # Ejercicio4--------------------------------------
def obtener_alturas(lista_arboles, especie)->list:
    alturas_especie = []
    for arbol in lista_arboles :
        if arbol["nombre_com"] == especie :
            alturas_especie.append(float(arbol['altura_tot']))
    return alturas_especie 
# a = leer_parque("arbolado-en-espacios-verdes.csv", "GENERAL PAZ")
# obtener_alturas(a, "Jacarandá")

def altura_Max_y_Promedio():
    a = leer_parque("arbolado-en-espacios-verdes.csv", "GENERAL PAZ")
    alturasA = obtener_alturas(a, "Jacarandá")
    b = leer_parque("arbolado-en-espacios-verdes.csv", "ANDES, LOS")
    alturasB = obtener_alturas(b, "Jacarandá")
    c = leer_parque("arbolado-en-espacios-verdes.csv", "CENTENARIO")
    alturasC = obtener_alturas(c, "Jacarandá")
    print("Medida General Paz Los Andes Centenario")
    print("max", max(alturasA) ,max(alturasB), max(alturasC) )
    print("prom", round(sum(alturasA)/len(alturasA),2), round(sum(alturasB)/len(alturasB),2), round(sum(alturasC)/len(alturasC),2) )
# altura_Max_y_Promedio()


# # Ejercicio5--------------------------------------
def obtener_inclinaciones(lista_arboles, especie)->list:
    inclinaciones_especie = []
    for arbol in lista_arboles :
        if arbol["nombre_com"] == especie :
            inclinaciones_especie.append(int(arbol['inclinacio']))
    return inclinaciones_especie
# a = leer_parque("arbolado-en-espacios-verdes.csv", "GENERAL PAZ")
# obtener_inclinaciones(a, "Jacarandá")


# # Ejercici6--------------------------------------
def especimen_mas_inclinado(lista_arboles):
    conjunto_especies_lista = list(especies(lista_arboles))
    arbol_e_inclinacion = dict()
    especie_mas_inclinada = ""
    for i in conjunto_especies_lista :
        arbol_e_inclinacion[i] = max(obtener_inclinaciones(lista_arboles, i))
    mayor_inclinacion = max(list(arbol_e_inclinacion.values()) )
    for j in list(arbol_e_inclinacion.items()) :
        if j[1] == mayor_inclinacion :
            especie_mas_inclinada = j[0] 
    print("Especie con mayor inclinacion:",especie_mas_inclinada,"con",mayor_inclinacion)
# a = leer_parque("arbolado-en-espacios-verdes.csv", "GENERAL PAZ") 
# b = leer_parque("arbolado-en-espacios-verdes.csv", "CENTENARIO")           
# especimen_mas_inclinado(b)

        
# # Ejercici7--------------------------------------
def especie_promedio_mas_inclinada(lista_arboles):
    conjunto_especies_lista = list(especies(lista_arboles))
    arbol_e_inclinacionProm = dict()
    especieMayorPromedioInclinacion = ""
    for i in conjunto_especies_lista :
        suma_inclinaciones = sum(obtener_inclinaciones(lista_arboles, i))
        cantidad_inclinaciones = len(obtener_inclinaciones(lista_arboles, i))
        arbol_e_inclinacionProm[i] = suma_inclinaciones / cantidad_inclinaciones
    mayorPromedioInclinacion = max(list(arbol_e_inclinacionProm.values()) )
    for j in list(arbol_e_inclinacionProm.items()) :
        if j[1] == mayorPromedioInclinacion :
            especieMayorPromedioInclinacion = j[0]
    print("Especie con mayor inclinacion promedio es:",especieMayorPromedioInclinacion,"con",mayorPromedioInclinacion)
# a = leer_parque("arbolado-en-espacios-verdes.csv", "GENERAL PAZ") 
# b = leer_parque("arbolado-en-espacios-verdes.csv", "ANDES, LOS")           
# especie_promedio_mas_inclinada(b)

   




    

        
            
            
    

    
    
    