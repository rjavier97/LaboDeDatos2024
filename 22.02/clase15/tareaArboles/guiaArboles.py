# -*- coding: utf-8 -*-
"""
Created on Fri Mar  1 13:42:48 2024

@author: Javier
"""
from sklearn.datasets import load_iris
from sklearn import datasets
import matplotlib.pyplot as plt
import numpy as np 
from IPython.display import display
import pandas as pd
from matplotlib import ticker   # Para agregar separador de miles
from inline_sql import sql, sql_val
import seaborn as sns
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split


# =============================================================================
# FUNCIONES AUXILIARES
# =============================================================================
def cargar_datos(file, filter = True):
    df = pd.read_csv(file, index_col=0)
    df = df.dropna()
    if filter:
        df = df.drop(columns = ["petal length (cm)", "petal width (cm)"])
    X = df.drop(columns = ["target"]) 
    y = df.target
    return df, X, y

def clasificador_naive_instance(x):
    ## Completen con sus reglas por ej
    r1= x.Sex == 'female' and x.Age >2
    r2= (x.Sex == 'male' and x.Age <= 17 )
    if r1 or r2 :
        return True
    else:
        return False


# In[4]:


def clasificador_naive(X):
    y_predict = []
    for x in X.itertuples(index=False): 
        y_predict.append(clasificador_naive_instance(x))
    return y_predict


# In[5]:


def score(y, y_pred):
    print("Le pego a " + str(np.sum(y==y_pred)) + " de " + str(len(y)))

# =============================================================================
# 
# =============================================================================
# =============================================================================
# 
# =============================================================================

# iris = datasets.load_iris()
# iris_df = pd.DataFrame(iris['data'], columns=iris.feature_names)
# Con el codigo de arriba, solo tendria el dataSet sin la columna de "target" (especie)

iris     = load_iris(as_frame = True)
dataIris = iris.frame # Iris en formato dataframe (5 variables, con tipo especie)
dataIris.to_csv('dataIris.csv', index=True)

df_dataIris, X, y = cargar_datos('dataIris.csv') # X tiene todas las columnas del dataframe menos la que queremos predecir,
                                        # Y tiene la columna que indica que especie es


# =============================================================================
# Histogramas de los datos (en este caso no sirve mucho este grafico)
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
plt.scatter(df_dataIris['sepal length (cm)'], df_dataIris['sepal width (cm)'])
plt.xlabel('Largo del Sépalo')
plt.ylabel('Ancho del Sépalo')
plt.title('Scatter Plot: Largo del Sépalo vs. Ancho del Sépalo')
plt.show()

# =============================================================================
# 
# =============================================================================
y_predict = clasificador_naive(X)
y_predict
score(y_predict, y)


X_comp = cargar_datos_competencia("titanic_competencia.csv")
y_pred_comp = clasificador_naive(X_comp)
y_pred_comp


# ## Ahora armemos un clasificador usando árboles de decisión


# ## Decision Tree


# In[9]:

# planta tu árbol aquí
from sklearn.tree import DecisionTreeClassifier,plot_tree, export_graphviz
from sklearn import tree  
# para ver el arbol ejecutar "from sklearn import tree" y ejecutar en otra linea "tree.plot_tree(arbol)

arbol = DecisionTreeClassifier(criterion="entropy",
                               max_depth= 3)

# Recordando... 
# X tiene todas las columnas del dataframe menos la que queremos predecir
# y tiene la columna que indica que especie es

arbol.fit(X, y) #Entrenamiento
prediction = arbol.predict(X) #Generamos las predicciones
prediction
arbol.score(X,y)
# Generamos el grafo del árbol
plt.figure(figsize=(20,10))
plot_tree(arbol, 
          filled=True,
          feature_names=X.columns, 
          class_names=["0", "1","2" ], 
          rounded=True)
plt.show()


