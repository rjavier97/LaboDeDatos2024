# -*- coding: utf-8 -*-
"""
Created on Tue Feb  6 03:17:41 2024

@author: Javier
"""

empleado01 = [[20222333, 45, 2, 20000],
              [33456234, 40, 0, 25000],
              [45432345, 41, 1, 10000]]


# Ejercicio1---------------------------------------------
def superanSalarioActividad01(empleado01, umbral)->list:
    nuevaMatriz = []
    for fila in empleado01 :
        if fila[3] > umbral :
            nuevaMatriz.append(fila)
    return nuevaMatriz 
# superanSalarioActividad01(empleado01, 15000) 


# Ejercicio2---------------------------------------------
empleado02 = empleado01.copy()
empleado02.append([43967304, 37, 0, 12000])
empleado02.append([42236276, 36, 0, 18000])

# superanSalarioActividad01(empleado02, 15000)

# Si, sigue funcionando 

# Ejercicio3---------------------------------------------
empleado03 = [[20222333, 20000, 45, 2],
              [33456234, 25000, 40, 0],
              [45432345, 10000, 41, 1],
              [43967304, 12000, 37, 0],
              [42236276, 18000, 36, 0]]

# superanSalarioActividad01(empleado03, 15000)

# No, ya no funciona.  Devuelve: []

def superanSalarioActividad03(empleado03, umbral)->list:
    empleado03original= []
    lista = []
    for i in empleado03 :
        lista.append(i[0])
        lista.append(i[2])
        lista.append(i[3])
        lista.append(i[1])
        empleado03original.append(lista)
    nuevaMatriz = []  
    print(empleado03original)
    for fila in empleado03original :
        if fila[3] > umbral :     
            nuevaMatriz.append(fila)
    return nuevaMatriz 
superanSalarioActividad03(empleado03, 15000)

            
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    