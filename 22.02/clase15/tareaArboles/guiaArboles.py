# -*- coding: utf-8 -*-
"""
Created on Fri Mar  1 13:42:48 2024

@author: Javier
"""

from sklearn import datasets
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np 




iris = datasets.load_iris()
iris_df = pd.DataFrame(iris['data'], columns=iris.feature_names)

# for column in iris_df.columns:
#     plt.figure(figsize=(8, 6))
#     plt.hist(iris_df[column], bins=20, edgecolor='black', alpha=0.7)
#     plt.xlabel(column)
#     plt.ylabel('Frecuencia')
#     plt.title(f'Histograma de {column}')
#     plt.show()

# =============================================================================
# Histogramas de los datos
# =============================================================================
for column in iris_df.columns:
    plt.figure(figsize=(8, 6))
    
    # Crear el histograma y obtener los valores
    n, bins, patches = plt.hist(iris_df[column], bins=20, edgecolor='black', alpha=0.7)
    
    # Agregar los valores de frecuencia encima de cada barra
    for value, bin, patch in zip(n, bins, patches):
        plt.text(bin + 0.5*(bins[1]-bins[0]), value, str(int(value)),
                 ha='center', va='bottom')
    
    plt.xlabel(column)
    plt.ylabel('Frecuencia')
    plt.title(f'Histograma de {column}')
    plt.show()
 
# =============================================================================
# Scatter Plot: Largo del sepalo vs Ancho del sepalo
# =============================================================================
plt.figure(figsize=(8, 6))
plt.scatter(iris_df['sepal length (cm)'], iris_df['sepal width (cm)'])
plt.xlabel('Largo del Sépalo')
plt.ylabel('Ancho del Sépalo')
plt.title('Scatter Plot: Largo del Sépalo vs. Ancho del Sépalo')
plt.show()




