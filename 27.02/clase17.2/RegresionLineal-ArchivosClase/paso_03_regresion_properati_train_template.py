# -*- coding: utf-8 -*-
"""
Materia     : Laboratorio de datos - FCEyN - UBA
Clase       : Clase Regresion Lineal
Detalle     : Modelos de Regresion Lineal
                - Cargamos los datos de test y train de properati
                - Proponemos distintos modelos y los evaluamos
Autores     : Manuela Cerdeiro y Pablo Turjanski
Modificacion: 2023-10-13
"""

# Importamos bibliotecas
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn import linear_model
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.preprocessing import PolynomialFeatures
from inline_sql import sql, sql_val

#%%
####################################################################
########  DEFINICION DE FUNCIONES AUXILIARES
####################################################################

# Dibuja una recta. Toma como parametros pendiente e intercept
def plotRectaRegresion(slope, intercept):
    """Plot a line from slope and intercept"""
    axes = plt.gca()
    x_vals = np.array(axes.get_xlim())
    y_vals = intercept + slope * x_vals
    plt.plot(x_vals, y_vals, '--', color="darkgreen")

#%%
####################################################################
########  MAIN
####################################################################
# Cargamos el archivo ya limpio
carpeta = '~/Downloads/Clase-17-scriptsDefinitivos/archivosRegresionLineal/solucion/'
data_train = pd.read_csv(carpeta+'data_alq_caba_train.csv', index_col = 'id', encoding='utf-8')


#%%
# ----------------------------------
# ----------------------------------
#       Modelo Lineal Simple 1
# ----------------------------------
# ----------------------------------
# Primer propuesta: Modelo Lineal Simple (rls) tomando a:
#  X1 = surface_total (variable predictora)
#  Y  = price         (variable a predecir)
########################
## Generacion del modelo
########################
# Declaramos las variables

# Declaramos el tipo de modelo

# Entrenamos el modelo

# Observamos los valores obtenidos (pendiente e intercept)
print("Coefficients")
print("------------")
print("   intercept: ", 0.0)
print("   pendiente: ", 0.0)


#####################################
## Evaluacion del modelo contra TRAIN
#####################################
#  R2
# Calculamos el R2. Recordar que 1 es en el caso de una prediccion perfecta
# ... Para calcular R2 usamos los residuos de predecir los datos 

print("R^2 (train): %.2f" % 0.0)
# Otra manera de calcular R2, es con la funcion score


# MSE (mean squared error, o en castellano error cuadratico medio)
print("MSE (train): %.2f" % 0.0)


###############################################
## Visualizacion del modelo vs valores de TRAIN
###############################################
# Graficamos una dispersion de puntos de precio en funcion de la superficie total


# Eliminamos las variables auxiliares que ya no utilizamos


#%%
# ----------------------------------
# ----------------------------------
#       Modelo Lineal Simple 2
# ----------------------------------
# ----------------------------------
# Segunda propuesta: Modelo Lineal Simple (rls) tomando a:
#  X1 = surface_covered (variable predictora)
#  Y  = price           (variable a predecir)
########################
## Generacion del modelo
########################
# Declaramos las variables

# Declaramos el tipo de modelo

# Entrenamos el modelo

# Observamos los valores obtenidos (pendiente e intercept)
print("Coefficients")
print("------------")
print("   intercept: ", 0.0)
print("   pendiente: ", 0.0)


######################################
## Evaluacion del modelo contrar TRAIN
######################################
#  R2
# Calculamos el R2. Recordar que 1 es en el caso de una prediccion perfecta
# ... Para calcular R2 usamos los residuos de predecir los datos de test

print("R^2 (train): %.2f" % 0.0)
# Otra manera de calcular R2, es con la funcion score


# MSE (mean squared error, o en castellano error cuadratico medio)
print("MSE (train): %.2f" % 0.0)

###############################################
## Visualizacion del modelo vs valores de TRAIN
###############################################
# Graficamos una dispersion de puntos de precio en funcion de la superficie total


# Eliminamos las variables auxiliares que ya no utilizamos


#%%
# ----------------------------------
# ----------------------------------
#       Modelo Multilineal 1
# ----------------------------------
# ----------------------------------
# Tercera propuesta: Modelo Multilineal tomando a:
#  X1 = surface_covered    (variable predictora 1)
#  X2 = surface_notCovered (variable predictora 2)
#  Y  = price           (variable a predecir)
########################
## Generacion del modelo
########################
# Declaramos las variables

# Un chequeo que se podria realizar es si surface_not_covered>=0 en todos los casos

# Declaramos el tipo de modelo

# Entrenamos el modelo


# Observamos los valores obtenidos (pendiente e intercept)
print("Coefficients")
print("------------")
print("   intercept: ", 0.0)
print("   pendiente: ", 0.0)


#####################################
## Evaluacion del modelo contra TRAIN
#####################################
#  R2
# Calculamos el R2. Recordar que 1 es en el caso de una prediccion perfecta
# ... Para calcular R2 usamos los residuos de predecir los datos de test

print("R^2 (train): %.2f" % 0.0)
# Otra manera de calcular R2, es con la funcion score


# MSE (mean squared error, o en castellano error cuadratico medio)
print("MSE (train): %.2f" % 0.0)


#######################################################
## Visualizacion del modelo vs valores de entrenamiento
#######################################################
# Este tipo de modelos ya es mas dificil de visualizar

# Eliminamos las variables auxiliares que ya no utilizamos


#%% 
# ----------------------------------
# ----------------------------------
#       Modelo Multilineal 2
# ----------------------------------
# ----------------------------------
# Cuarta propuesta: Modelo Multilineal tomando a:
#  X1 = surface_covered    (variable predictora 1)
#  X2 = lat                (variable predictora 2)
#  X3 = lon                (variable predictora 2)
#  Y  = price           (variable a predecir)
########################
## Generacion del modelo
########################
# Antes de utilizar lat y lon veamos si tienen valores null
# Comenzamos con lat ...

# Generamos un nuevo dataframe de datos para este modelo tal que no 
# contenga na en lat

# Ahora verificamos en data_train_l si quedan registros con null en lon

# data_l ya no tiene null ni en lat ni en lon
# Declaramos las variables

# Declaramos el tipo de modelo

# Entrenamos el modelo


# Observamos los valores obtenidos (pendiente e intercept)
print("Coefficients")
print("------------")
print("   intercept: ", 0.0)
print("   pendiente: ", 0.0)


####################################
## Evaluacion del modelo contra TRAIN
#####################################  R2
# Calculamos el R2. Recordar que 1 es en el caso de una prediccion perfecta
# ... Para calcular R2 usamos los residuos de predecir los datos de test

print("R^2 (train): %.2f" % 0.0)
# Otra manera de calcular R2, es con la funcion score


# MSE (mean squared error, o en castellano error cuadratico medio)
print("MSE (train): %.2f" % 0.0)


#######################################################
## Visualizacion del modelo vs valores de entrenamiento
#######################################################
# Este tipo de modelos ya es mas dificil de visualizar

# Eliminamos las variables auxiliares que ya no utilizamos


#%% 
# ----------------------------------
# ----------------------------------
#       Modelo Polinomial 1
# ----------------------------------
# ----------------------------------
# Quinta propuesta: Modelo Polinomial tomando a:
#  X1    = surface_covered  (variable predictora)
#  Y     = price            (variable a predecir)
#  grado = 30
########################
## Generacion del modelo
########################
# Declaramos las variables


# Generamos las variables polinomicas (Xp = [X^0,X^1,...,X^30])

# Declaramos el tipo de modelo

# Entrenamos el modelo


# Observamos los valores obtenidos (pendiente e intercept)
print("Coefficients")
print("------------")
print("   intercept : ", 0.0)
print("   pendientes: ", 0.0)

#####################################
## Evaluacion del modelo contra TRAIN
#####################################
#  R2
# Calculamos el R2. Recordar que 1 es en el caso de una prediccion perfecta
# ... Para calcular R2 usamos los residuos de predecir los datos de test

print("R^2 (train): %.2f" % 0.0)
# Otra manera de calcular R2, es con la funcion score


# MSE (mean squared error, o en castellano error cuadratico medio)
print("MSE (train): %.2f" % 0.0)

# Eliminamos las variables auxiliares que ya no utilizamos


