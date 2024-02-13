# -*- coding: utf-8 -*-
"""
Created on Tue Feb 13 03:52:52 2024

@author: Javier
"""

# Importamos bibliotecas
import pandas as pd
import csv
from inline_sql import sql, sql_val

carpeta = ""

casos         = pd.read_csv(carpeta+"casos.csv")    
departamento  = pd.read_csv(carpeta+"departamento.csv")    
grupoetario   = pd.read_csv(carpeta+"grupoetario.csv")    
provincia     = pd.read_csv(carpeta+"provincia.csv")    
tipoevento    = pd.read_csv(carpeta+"tipoevento.csv")    
   
