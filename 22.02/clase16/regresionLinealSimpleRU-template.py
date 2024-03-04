# -*- coding: utf-8 -*-
"""
Materia     : Laboratorio de datos - FCEyN - UBA
Clase       : Clase Regresion Lineal
Detalle     : Modelo de Regresion Lineal Simple
Autores     : Maria Soledad Fernandez y Pablo Turjanski
Modificacion: 2023-10-13
"""

# Importamos bibliotecas
import pandas as pd
import numpy as np
from sklearn import linear_model
from sklearn.metrics import r2_score
import matplotlib.pyplot as plt
import seaborn as sns
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
    plt.plot(x_vals, y_vals, color="red")

#%%

####################################################################
########  MAIN
####################################################################
# Cargamos el archivo 
carpeta = ''
data_train = pd.read_csv(carpeta+"datos_roundup.txt", sep=" ", encoding='utf-8')
data_trainSQL = sql^"""SELECT * from data_train"""

promedioX = data_train["RU"].mean() # promedio de los valores de RU
promedioY = data_train["ID"].mean() # promedio de los valores de ID

listaX = data_train['RU'].astype(float).tolist() # lista con los valores de RU
listaY = data_train['ID'].astype(float).tolist() # lista con los valores de ID
# listapromX = [0,25,50,87.5,130,175,221.43,287.5,366.6,455,572.7]
# listapromY = [104,105,107.43,109.825,92.43,96,114.6, 117.765,120.3,123.6,127.94]

b1 = 0
for i in range (0,11):
    numerador = (listaX[i]-promedioX)*(listaY[i]-promedioY)
    denominador = (listaX[i] - promedioX) **2
    b1 = b1 + (numerador/denominador)

b0 = (promedioY) - (b1*promedioX)   
    
    


# ----------------------------------
# ----------------------------------
#       Modelo Lineal Simple (rls)
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

# Observamos los valores obtenidos (pendiente e intercept)


###############################################
## Visualizacion del modelo vs valores de TRAIN
###############################################
# Graficamos una dispersion de puntos de ID en funcion de la Dosis de RU


#####################################
## Prediccion
#####################################
# Cargamos el archivo (no posee valores para ID)
carpeta = '~/Downloads/'
data_a_predecir = pd.read_csv(carpeta+"datos_a_predecir.txt", sep=" ", encoding='utf-8')

# Realizamos la prediccion de ID utilizando el modelo y
# la asignamos a la columna ID


# Graficamos una dispersion de puntos de ID en funcion de la Dosis de RU
# Graficamos tanto los puntos de entrenamiento del modelo como los predichos


#####################################
## Evaluacion del modelo contra TRAIN
#####################################
#  R2






