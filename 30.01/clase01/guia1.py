#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 30 13:51:50 2024

@author: Estudiante
"""
# Ejercicios en clase ----------------------------------------------------
def tachar_pares(lista)->list:
    res=[]
    for i in lista:
        if i % 2 == 0:
            res.append("x")
        else : 
            res.append(i)
    return res
# print(tachar_pares([3,2,7]))

# Guia de ejercicios -----------------------------------------------------
# # Ejercicio 1 ------------------------------
def billeteObelisco():
    dias = 1
    altura = 0.00011
    while altura < 67.5 :
        dias += 1
        altura = 0.00011 * (2**(dias+1))
    return dias
print("Ejercicio1: billeteObelisco() es:",billeteObelisco())

# # Ejercicio 2 ------------------------------
def rebotes():
    inicial = 100
    for i in range (1,11):
        inicial = round(inicial*0.6 , 4)
        print(str(i)+" "+ str(inicial))
print("Ejercicio2: rebotes()")       
rebotes()

# # Ejercicio 3 ------------------------------
def palabraNeutra(palabra):
    palabra = list(palabra)
    if palabra[-1] == "o" :
        palabra[-1] = "e"
    elif len(palabra)>1 and palabra[-2] == "o" :
        palabra[-2] = "e"
    palabra = "".join(palabra)
    return palabra
# print(palabraNeutra("perro"))
# print("Ejercicio3: palabraNeutra('perro') es:",palabraNeutra('perro'))


def traductorNeutro(frase)->str:
    listaPalabras = frase.split(" ")
    for i in range(0,len(listaPalabras)):
        listaPalabras[i] = palabraNeutra(listaPalabras[i])
    frase = " ".join(listaPalabras)
    return frase
print("Ejercicio3: traductorNeutro('todos somos programadores') es:",traductorNeutro('todos somos programadores'))

# # Ejercicio 4 ------------------------------
def es_par(n)->bool:
    res = False
    if n % 2 == 0:
        res = True
    return res 
print("Ejercicio4: es_par(7) es:",es_par(7))

# # Ejercicio 5 ------------------------------
def dos_pertenece(lista)->bool:
    res = False
    for num in lista:
        if num == 2 :
            res = True
    return res 
print("Ejercicio5: dos_pertenece([1,2,3,4]) es:", dos_pertenece([1,2,3,4]))

# # Ejercicio 6 ------------------------------
def pertenece(lista, elemento)->bool:
    res = False
    for i in lista :
        if i == elemento :
            res = True
    return res
print("Ejercicio6: pertenece([1,2,3,4], 2) es:", pertenece([1,2,3,4],2))

# # Ejercicio 7 ------------------------------
def mas_larga(lista1, lista2)->list:
    res = lista1
    if len(lista2)>len(lista1):
        res = lista2
    return res 
print("Ejercicio7: mas_larga([1,2,3,4],[1,2,3,4,5]) es:", mas_larga([1,2,3,4],[1,2,3,4,5]))

# # Ejercicio 8 ------------------------------
def cant_e(lista)->int:
    res = 0
    for caracter in lista:
        if caracter == "e":
            res += 1
    return res
print("Ejercicio8: cant_e(['a', 'b', 'c', 'e', 'e']) es:",cant_e(['a', 'b', 'c', 'e', 'e']))

# # Ejercicio 9 ------------------------------
def sumar_unos(lista)->list:
    for i in range(len(lista)):
        lista[i] = lista[i] + 1
    return lista 
print("Ejercicio9: sumar_unos([1,2,3,4,5]) es:",sumar_unos([1,2,3,4,5]))

# # Ejercicio 10 ------------------------------
def mezclar(cadena1, cadena2)->str:
    res = ""
    if len(cadena1) <= len(cadena2):
        for i in range(len(cadena1)): #Caso cadena1 mas chico o igual que cadena2
            res = res + cadena1[i] + cadena2[i]
            if i == len(cadena1)-1 and len(cadena1)<len(cadena2):
                for j in range(i+1,len(cadena2)):
                    res = res + cadena2[j]
    else : 
        for i in range(len(cadena2)) :  #Caso cadena1 mas grande que cadena2
            res = res + cadena1[i] + cadena2[i]
            if i == len(cadena2)-1 :
                for j in range(i+1, len(cadena1)):
                    res = res + cadena1[j]
    return res 
print("Ejercicio10: mezclar('Pepe','Josefa') es:",mezclar('Pepe','Josefa'))


        


