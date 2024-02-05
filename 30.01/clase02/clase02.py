# -*- coding: utf-8 -*-
# """
# Editor de Spyder

# Este es un archivo temporal.
# """

# =============================================================================
# f9 para correr linea por linea,
# shift + enter para correr linea indicada
# =============================================================================


# """Ejercicio"""
# """
# def traductor_geringoso(lista):
#     vocales =  ["a", "e", "i", "o", "u"]
#     diccionario = {}
#     palabra=""
#     for i in lista :
#         for j in i :
#             if j in vocales : 
#                 palabra = palabra + j + "p"+ j
#             else :
#                 palabra = palabra + j
#         diccionario[i] = palabra
#         palabra = ""
#     return diccionario     
# """

# """print(traductor_geringoso(["perro", "gato"])) """

# f = open('datame.txt', 'rt', encoding="utf-8")
# data = f.read()
# print("Mientras esta abierto el archivo\n"+data)
# f.close()
# print("Luego de cerrar archivo\n"+data)

# with open('datame.txt', 'rt', encoding="utf-8") as file: # otra forma de abrir archivos
#   data = file.read()
#   # 'data' es una cadena con todo el texto en el archivo
# data
# print(data)

# nombre_archivo = 'cronograma_sugerido.csv'
# with open(nombre_archivo, 'rt', encoding="utf-8") as file:
#     for line in file:
#         print(line)
#         datos_linea = line.split(',')
#         print(datos_linea)
#         print(datos_linea[1])


# import csv 
# nombre_archivo = 'cronograma_sugerido.csv'
# # registros devuelve un diccionario con el encabezado como claves, 
# # y los valores las entradas de cada fila
# def registros(nombre_archivo):
#     lista = []
#     with open(nombre_archivo, 'rt', encoding="utf-8") as f :
#         filas = csv.reader(f)
#         # print(filas) #Muestra: <_csv.reader object at 0x0000022E1175B280>
#         encabezado = next(filas)
#         print("Este es el encabezado\n"+str(encabezado)+'\n')
#         for fila in filas :
#             registro = dict(zip(encabezado, fila))  # armo el diccionario de cada fila
#             # print(registro)
#             lista.append(registro)   # lo agrego a la lista
#             # print(lista)
#     return lista 
# print(registros(nombre_archivo)) 


# """ Ejercicios ---------------------------------------------- """
# """
# import random 
# def generala_tirar():
#     lista = [1,2,3,4,5]
#     lista_aleatoria=[]
#     for i in range(1,6):
#         lista_aleatoria.append(random.choice(lista))
#     return lista_aleatoria
# print(generala_tirar())
# """


# #Imprime las lineas que incluye"estudiantes"
# def contieneEstudiante(nombre_archivo):
#     with open(nombre_archivo, 'rt', encoding="utf-8") as file :
#         lista_lineas = file.readlines() 
#         # print("Lista de lineas del archivo:\n"+str(lista_lineas))
#         for linea in lista_lineas :
#             if "estudiante" in linea :
#                 print(linea)
# contieneEstudiante('datame.txt') 



# def listadoMaterias(nombre_archivo): 
#     with open(nombre_archivo, 'rt', encoding="utf-8") as file : 
#         lista_materias = []
#         next(file)  #Aca me salteo el encabezado(primerafila)
#         for line in file: 
#             datos_linea = line.split(',') #Hago de c/linea una lista
#             print(datos_linea)
#           # print(datos_linea[1])
#             lista_materias.append(datos_linea[1])
#     return lista_materias
# listadoMaterias('cronograma_sugerido.csv')


# def cuantas_materias(n):
#     cantidad_materias = 0 
#     with open('cronograma_sugerido.csv', 'rt', encoding="utf-8") as file :
#         for line in file :
#             datos_linea = line.split(',')
#             if str(n) in datos_linea :
#                 cantidad_materias += 1
#     return cantidad_materias
# print("En el cuatrimestre deberá cursar",cuantas_materias(8),"materias")



# =============================================================================
# Funcion que devuelve una lista de diccionarios con la información de 
# las materias sugeridas para cursar el n-ésimo cuatrimestre.
# =============================================================================
import csv
def materias_cuatrimestre(nombre_archivo, n):
    lista = []
    lista_diccionarios = []
    with open(nombre_archivo, 'rt', encoding="utf-8") as f :
        filas = csv.reader(f)
        encabezado = next(filas)
        for fila in filas :
            registro = dict(zip(encabezado, fila))  # armo el diccionario de cada fila
            lista.append(registro)                  # lo agrego a la lista
        for i in lista :
            if i['Cuatrimestre'] == str(n) :
                lista_diccionarios.append(i) 
    return lista_diccionarios
materias_cuatrimestre("cronograma_sugerido.csv", 5)
                
    
            
# import numpy as np