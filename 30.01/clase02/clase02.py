# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal.
"""

"""f9 para correr linea por linea,
shift + enter para correr linea indicada"""

"""Ejercicio"""
"""
def traductor_geringoso(lista):
    vocales =  ["a", "e", "i", "o", "u"]
    diccionario = {}
    palabra=""
    for i in lista :
        for j in i :
            if j in vocales : 
                palabra = palabra + j + "p"+ j
            else :
                palabra = palabra + j
        diccionario[i] = palabra
        palabra = ""
    return diccionario     
"""

"""print(traductor_geringoso(["perro", "gato"])) """

"""f = open('datame.txt', 'rt')
data = f.read()
print(data)
f.close()"""


"""
nombre_archivo = 'cronograma_sugerido.csv'
with open(nombre_archivo, 'rt') as file :import csv 
def registros(nombre_archivo):
    lista = []
    with open(nombre_archivo, 'rt') as f :
        filas = csv.reader(f)
        encabezado = next(filas)
        for fila in filas :
            registro = dict(zip(encabezado, fila))  # armo el diccionario de cada fila
            lista.append(registro)                  # lo agrego a la lista
    return lista 

print(registros('cronograma_sugerido.csv'))
    lista = []
    for line in file: 
        datos_linea = line.split(',')
        print(datos_linea[1])
        lista.append(datos_linea[1])
    print(lista)
"""    

"""
import csv 
def registros(nombre_archivo):
    lista = []
    with open(nombre_archivo, 'rt') as f :
        filas = csv.reader(f)
        encabezado = next(filas)
        for fila in filas :
            registro = dict(zip(encabezado, fila))  # armo el diccionario de cada fila
            lista.append(registro)                  # lo agrego a la lista
    return lista 
print(registros('cronograma_sugerido.csv'))
"""

""" Ejercicios ---------------------------------------------- """
"""
import random 
def generala_tirar():
    lista = [1,2,3,4,5]
    lista_aleatoria=[]
    for i in range(1,6):
        lista_aleatoria.append(random.choice(lista))
    return lista_aleatoria
print(generala_tirar())
"""

"""
def contieneEstudiante(nombre_archivo):
    with open(nombre_archivo, 'rt') as file :
        lista_lineas = file.readlines() 
        for linea in lista_lineas :
            if "estudiante" in linea :
                print(linea)
contieneEstudiante('datame.txt')
"""

"""
def listadoMaterias(nombre_archivo): 
    with open(nombre_archivo, 'rt') as file : 
        lista_materias = []
        for line in file: 
            datos_linea = line.split(',')
            print(datos_linea)
          # print(datos_linea[1])
            lista_materias.append(datos_linea[1])
        return lista_materias
print(listadoMaterias('cronograma_sugerido.csv'))
"""

"""
def cuantas_materias(n):
    cantidad_materias = 0 
    with open('cronograma_sugerido.csv', 'rt') as file :
        for line in file :
            datos_linea = line.split(',')
            if str(n) in datos_linea :
                cantidad_materias += 1
        return cantidad_materias
print(cuantas_materias(6)) 
"""

def materias_cuatrimestre(nombre_archivo, n):
    lista = []
    lista_diccionarios = []
    with open(nombre_archivo, 'rt') as f :
        filas = csv.reader(f)
        encabezado = next(filas)
        for fila in filas :
            registro = dict(zip(encabezado, fila))  # armo el diccionario de cada fila
            lista.append(registro)                  # lo agrego a la lista
        for i in lista :
            if i['Cuatrimestre'] == str(n) :
                lista_diccionarios.append(i) 
        return lista_diccionarios
                
    
            
    
    
    
    

    
     


        
        
    

    
    
        

        
            
            
        
   


