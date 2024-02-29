# -*- coding: utf-8 -*-
"""
Materia     : Laboratorio de datos - FCEyN - UBA
Clase       : Clase Clasificacion
Detalle     : Modelo KNN
Autores     : Manuela Cerdeiro y Pablo Turjanski
Modificacion: 2023-10-24
"""

# Importamos bibliotecas
from sklearn.datasets import load_iris
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split


#%%
####################################################################
########  MAIN
####################################################################
# Cargamos el archivo 
iris     = load_iris(as_frame = True)
dataIris = iris.frame # Iris en formato dataframe (5 variables)

# Para comprender la variable target armamos un diccionario con equivalencia
print(iris.target_names)
diccionario = dict(zip( [0,1,2], iris.target_names)) # Diccionario con equivalencia


#%%
# ----------------------------------
# ----------------------------------
#       Modelo KNN
# ----------------------------------
# ----------------------------------
#  X = RU (variable predictora) [Dosis de Roundup]
#  Y = ID (variable a predecir) [Damage Index]
########################
## Generacion del modelo
########################
# Declaramos las variables

# Declaramos el tipo de modelo

# Entrenamos el modelo

#################################################
## Evaluacion del modelo contra dataIris completo
#################################################
# Calculamos el R2. Recordar que 1 es en el caso de una prediccion perfecta



#%%
#################################################
## Generacion archivos TEST / TRAIN
#################################################
# Dividimos en test(30%) y train(70%)


##################################################################
## Repetimos todo, pero en funcion de TEST y TRAIN y variando el k
##################################################################
# Rango de valores por los que se va a mover k
valores_k = range(1, 10)


##################################################################
## Graficamos R2 en funcion de k (para train y test)
##################################################################


#%%
#############################################################
## Repetimos todo, realizando varios experimentos para cada k
#############################################################
# Rango de valores por los que se va a mover k

#  Cantidad de veces que vamos a repetir el experimento

# Matrices donde vamos a ir guardando los resultados

# Realizamos la combinacion de todos los modelos (Nrep x k)

# Promediamos los resultados de cada repeticion

##################################################################
## Graficamos R2 en funcion de k (para train y test)
##################################################################
