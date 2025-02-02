# -*- coding: utf-8 -*-
"""
Materia     : Laboratorio de datos - FCEyN - UBA
Clase       : Clase Regresion Lineal
Detalle     : Modelo de Regresion Lineal Simple - Cuarteto de Anscombe
Autores     : Maria Soledad Fernandez y Pablo Turjanski
Modificacion: 2023-10-23
"""

# Importamos bibliotecas
import pandas as pd
import numpy as np
from sklearn import linear_model
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
# Cargamos los datos
# data_anscombe va a contener los 4 conjuntos de datos
# Tener en cuenta esto al momento de procesarlos
data_anscombe = sns.load_dataset("anscombe")

# Sets de datos
datasets = ["I", "II", "III", "IV"]

# Imprimimos el header de la tabla
print("dataset \tinter. \tpend. \tR2")
print("-------------------------------")
# Procesamos cada set de datos
for dataset in datasets:
    # ----------------------------------
    # ----------------------------------
    #       Modelo Lineal Simple (rls)
    # ----------------------------------
    # ----------------------------------
    ########################
    ## Generacion del modelo
    ########################
    data_train = sql^ "SELECT x, y FROM data_anscombe WHERE dataset='" + dataset + "'   "
    # Declaramos las variables
    
    # Declaramos el tipo de modelo

    # Entrenamos el modelo

    # Mostramos los coeficientes y el R2
    print(dataset, "\t \t", end="")           # dataset (I, II, III o IV)
    print("{:.3f}".format(0.0)  , " \t", end="") # Intercept
    print("{:.3f}".format(0.0)  , " \t", end="") # Pendiente
    print("{:.3f}".format(0.0)  , " \t", end="") # R2
    print()
    
    ###############################################
    ## Visualizacion del modelo vs valores de TRAIN
    ###############################################
    # Graficamos una dispersion de puntos de y en funcion x
    plt.figure()
    #  Completar
    plt.show()
