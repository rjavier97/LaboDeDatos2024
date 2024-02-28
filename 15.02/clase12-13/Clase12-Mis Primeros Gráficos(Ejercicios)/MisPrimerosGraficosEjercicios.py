# -*- coding: utf-8 -*-
"""
Created on Wed Feb 28 00:43:26 2024

@author: Javier
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt # Para graficar series multiples
from   matplotlib import ticker   # Para agregar separador de miles
import seaborn as sns           # Para graficar histograma

# =============================================================================
# 
# =============================================================================
ventasPorRegion = pd.read_csv("ventasPorRegion.csv")


fig, ax = plt.subplots()

ax.pie(data=ventasPorRegion,
       x='Porcentaje',
       labels='Region',
       autopct='%1.2f%%',
       shadow = True,
       counterclock = True, 
       explode = (0,0,0.1,0)
       )
# =============================================================================
# 
# =============================================================================
precioBiodiesel = pd.read_csv("precioBiodiesel.csv")

fig, ax = plt.subplots()

ax.plot('Periodo', 'Precio', data=precioBiodiesel)

# =============================================================================
# 
# =============================================================================
telefonos = pd.read_csv("telefonosInteligentes.csv")

fig, ax = plt.subplots()

ax = telefonos.plot(
        x='RangoEtario',
        y=['Telefono_Inteligente','Telefono_NoInteligente','SinTelefono'],
        kind='bar',
        label=['Telefono Inteligente','Telefono NoInteligente','Sin Telefono'], 
        )

ax.set_title('Telefonia segun rango etario')
ax.set_xlabel('Rango etario')    
ax.set_ylabel('Cantidad de Personas')
ax.set_ylim(0,70) 

              
              
              
              
              









