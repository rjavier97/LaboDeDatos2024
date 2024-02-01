#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 30 13:51:50 2024

@author: Estudiante
"""
# Ejercicios en clase -------------------------------------------------------------------
def tachar_pares(lista)->list:
    res= []
    for i in lista :
        if i % 2 == 0 :
            res.append("x")
        else :
            res.append(i)
    return res
# """ print(tachar_pares([3,2,7])) """

# Guia de ejercicios ---------------------------------------------------------------------
# # Ejercicio 1 ------------------------------
def billeteObelisco():
    dias = 1
    altura = 0.00011
    while altura < 67.5 :
        dias += 1
        altura = 0.00011 * (2**(dias+1))
    return dias
print(billeteObelisco())

# # Ejercicio 2 ------------------------------
def rebotes():
    inicial = 100
    for i in range (1,11):
        inicial = round(inicial*0.6 , 4)
        print(str(i)+" "+ str(inicial))
        
"Ejercicio 3"



