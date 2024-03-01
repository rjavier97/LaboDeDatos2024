#!/usr/bin/env python
# coding: utf-8

# ## Podemos predecir quienes sobrevivieron en el Titanic? 
# 
# Tenemos un dataset muy famoso con datos de los pasajeros del titanic. El mismo está disponible en: 
# 
# https://www.kaggle.com/c/titanic/data 

# In[1]:


import utilsTitanic as utils
from IPython.display import display
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from   matplotlib import ticker   # Para agregar separador de miles
from inline_sql import sql, sql_val
import seaborn as sns


# ### Cargamos los datos

# In[2]:


df_titanic, X, y = utils.cargar_datos('titanic_training.csv') # X tiene todas las columnas del dataframe menos la que queremos predecir,
                                        # Y tiene la columna que indica si sobrevivieron
df_titanicSQL = sql^"""SELECT * FROM df_titanic"""

supervivientes = sql^"""
SELECT Sex, SUM(Survived) AS sobrevivientes
FROM df_titanic
GROUP BY Sex  """

fallecieron = sql^""" SELECT df.Sex, Count(df.Survived) AS fallecieron
FROM df_titanic as df 
WHERE df.Survived = 0 
GROUP BY df.Sex
"""
resumenTitanic = sql^"""
SELECT supervivientes.*, fallecieron.fallecieron
FROM supervivientes 
INNER JOIN fallecieron 
ON supervivientes.Sex = fallecieron.Sex
"""                        
                        
df_titanic.head()

# Agrupar y contar la cantidad de sobrevivientes y fallecidos por sexo
resultados = df_titanic.groupby(['Sex', 'Survived']).size().unstack()

# Crear el gráfico de barras
ax = resultados.plot(kind='bar', stacked=True, color=['red', 'green'], alpha=0.7)

# Personalizar el gráfico
ax.set_title('Sobrevivientes y Fallecidos por Sexo')
ax.set_xlabel('Sexo')
ax.set_ylabel('Cantidad')
ax.set_ylim(0,105)
ax.set_yticks(range(0,105,10))
ax.legend(['Fallecido', 'Sobreviviente'], loc='upper right')
plt.show()
# ### Exploren estos datos!! Ideas: histogramas, pairplots, etc 

# In[3]:


##Exploren 


# ## Competencia: Armen sus Reglas !!

# In[3]:


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


# #### Usemos nuestro clasificador sobre los datos 

# In[6]:


y_predict = clasificador_naive(X)
y_predict
score(y_predict, y)


# In[9]:


X_comp = utils.cargar_datos_competencia("titanic_competencia.csv")
y_pred_comp = clasificador_naive(X_comp)
y_pred_comp


# ## Ahora armemos un clasificador usando árboles de decisión

# In[7]:


# Algo de procesamiento de los datos
X = utils.encode_sex_column(X)


# ## Decision Tree
# Para saber más: <https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeClassifier.html>

# In[9]:


# planta tu árbol aquí
from sklearn.tree import DecisionTreeClassifier,plot_tree, export_graphviz
from sklearn import tree  
# para ver el arbol ejecutar "from sklearn import tree" y ejecutar en otra linea "tree.plot_tree(arbol)

arbol = DecisionTreeClassifier(criterion="entropy",
max_depth= 4)
arbol.fit(X, y) #Entrenamiento
prediction = arbol.predict(X) #Generamos las predicciones
# Generamos el grafo del árbol
plt.figure(figsize=(20,10))
plot_tree(arbol, filled=True, feature_names=X.columns, class_names=["Not Survived", "Survived"], rounded=True)
plt.show()
# import graphviz
# dot_data = export_graphviz(arbol, out_file=None, feature_names= X.columns,
# class_names= ["Not Survived", "Survived"],
# filled=True, rounded=True,
# special_characters=True)
# graph = graphviz.Source(dot_data) #Armamos el grafo
# graph.view()
# graph.render("titanic", format= "png") #Guardar la imágen
# tree.plot_tree(graph)


# #### Generamos el gráfico de nuestro árbol
# Para saber más <https://scikit-learn.org/stable/modules/generated/sklearn.tree.export_graphviz.html#sklearn.tree.export_graphviz>

# In[10]:


# plot arbol


# ### ¿Cuál es el mejor corte? 

# In[8]:


utils.plot_hist_sex_survived(df_titanic)


# In[9]:


utils.plot_hist_age_survived(df_titanic)


# ## ¿Todos los árboles son iguales?
# 
# veamos dos ejemplos

# In[13]:


## Armar un árbol de altura 2


# In[14]:


## Armar un arbol con altura indefinida


# ## Veamos la performance de estos árboles sobre un conjunto de test

# In[10]:


#Cargamos los datos de tests
X_test, y_test = utils.cargar_datos_test('test_titanic.csv')


# In[ ]:


# Veamos el score del arbol de altura 2 sobre los datos de entrenamiento y los datos de tests


# In[ ]:


# Veamos el score del arbol de altura inf sobre los datos de entrenamiento y los datos de tests

