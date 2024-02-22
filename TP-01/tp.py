# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal.
"""

import pandas as pd
import numpy as np 
from inline_sql import sql, sql_val

carpeta = ""


GPD_paises = pd.read_csv('API_NY.GDP.PCAP.CD_DS2_en_csv_v2_73.csv',skiprows=4)


secciones_original = pd.read_csv('lista-secciones.csv')

datos_sedes = pd.read_csv('lista-sedes-datos.csv')
 
len(datos_sedes['sede_id'].unique())

GPD_2022 = pd.DataFrame(columns=['Country_name', 'Country_code', '2022'])

GPD_2022[['Country_name', 'Country_code', 'pbi']]= GPD_paises[['Country Name', 'Country Code', '2022']]

# mask = GPD_paises ['2022'] .notnull()

# GPD_2022 = GPD_2022[mask]

len(secciones['sede_id'].unique())   # da 105
len(secciones['sede_desc_castellano'].unique())   # da 202



# =============================================================================
# CREACION DE DATAFRAMES
# 
# =============================================================================


redes_sociales = pd.DataFrame(columns=['id_sede','url'])

Sedes = pd.DataFrame(columns=['id_sede','nom_sede','codigo_territorio'])

secciones  = pd.DataFrame(columns=['id_sede','nom_seccion'])

Paises  = pd.DataFrame(columns=['codigo_pais','nom_territorio','id_region','PIB'])

Region = pd.DataFrame(columns=['id_region','nom_region'])


Paises[['codigo_pais','nom_territorio']] = datos_sedes[['pais_iso_3','pais_castellano']].drop_duplicates()


Region['nom_region'] = sorted(datos_sedes['region_geografica'].unique())

Region['id_region'] = np.array(range(1,len(Region['nom_region'])+1))

pbi2022 = sql^"""
               SELECT DISTINCT codigo_pais, nom_territorio, pbi.pbi, Region.id_region
               FROM Paises
               LEFT OUTER JOIN GPD_2022 AS pbi
               ON Paises.codigo_pais = pbi.Country_code
               LEFT OUTER JOIN datos_sedes
               ON datos_sedes.pais_iso_3 = codigo_pais
               LEFT OUTER JOIN Region 
               ON nom_region = datos_sedes.region_geografica              
               """

Paises = pbi2022

Sedes[['id_sede','nom_sede','codigo_territorio']] = datos_sedes[['sede_id','sede_desc_castellano','pais_iso_3']]
               
secciones[['id_sede','nom_seccion']] = secciones_original[['sede_id','sede_desc_castellano']]

secciones = sql^"""
                SELECT 
                FROM secciones
                """

sql^"""
    SELECT count(sede_id)
    FROM datos_sedes
    """
 
#Codigo para limpiar datos de columna sitio web    
for i in range(datos_sedes.shape[0]):

    urls =  datos_sedes.loc[i,'redes_sociales']

    if type(urls) == str:

        if urls != None:
            lista_urls = urls.split('  //  ')[:-1]
            df_url_sede = pd.DataFrame((zip(np.full(len(lista_urls), datos_sedes.loc[i,'sede_id']),lista_urls)),columns=['id_sede','url'])

            redes_sociales = pd.concat([redes_sociales,df_url_sede], axis=0)    
    
redes_sociales = sql^"""
                 SELECT DISTINCT *
                 FROM redes_sociales
                 """
    
# =============================================================================
#  h)     
# =============================================================================

