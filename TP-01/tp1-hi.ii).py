# -*- coding: utf-8 -*-
"""
Created on Sat Feb 24 17:12:01 2024

@author: pc
"""

# Importo librearias
import pandas as pd
import numpy as np
from inline_sql import sql
import matplotlib.pyplot as plt
from matplotlib import ticker   
import seaborn as sns        



pbi_paises = pd.read_csv('API_NY.GDP.PCAP.CD_DS2_en_csv_v2_73.csv',skiprows=4)

codigo_paises = pd.read_csv('Metadata_Country_API_NY.GDP.PCAP.CD_DS2_en_csv_v2_73.csv')

metadata = pd.read_csv('Metadata_Indicator_API_NY.GDP.PCAP.CD_DS2_en_csv_v2_73.csv')

# cargo Dataframes del Ministerio

secciones_original = pd.read_csv('lista-secciones.csv')

sedes_original = pd.read_csv('lista-sedes.csv')

datos_sedes = pd.read_csv('lista-sedes-datos.csv')

# =============================================================================
# Creacion de DataFrames
# =============================================================================

redes_sociales = pd.DataFrame(columns=['id_sede','url'])

sedes = pd.DataFrame(columns=['id_sede','nom_sede','codigo_pais'])

secciones  = pd.DataFrame(columns=['id_sede','nom_seccion'])

paises  = pd.DataFrame(columns=['codigo_pais','nom_pais','id_region','PIB'])

regiones = pd.DataFrame(columns=['id_region','nom_region'])




mask = datos_sedes['redes_sociales'].notnull()

sedes_c_rs = datos_sedes[['sede_id']][mask] 




regiones['nom_region'] = sorted(datos_sedes['region_geografica'].unique())

regiones['id_region'] = np.array(range(1,len(regiones['nom_region'])+1))


sedes[['id_sede','nom_sede','codigo_pais']] = datos_sedes[['sede_id','sede_desc_castellano','pais_iso_3']]


paises['id_region'] = paises['id_region'].apply(lambda x: regiones[regiones.loc[:,'nom_region'] == x]['id_region'].values[0])

secciones[['id_sede','nom_seccion']] = secciones_original[['sede_id','sede_desc_castellano']]

secciones = sql^"""
                SELECT DISTINCT* 
                FROM secciones
                 """

GPD_2022 = pd.DataFrame(columns=['Country_name', 'Country_code', '2022'])

GPD_2022[['Country_name', 'Country_code', 'pbi']]= pbi_paises[['Country Name', 'Country Code', '2022']]

paises[['codigo_pais','nom_pais','id_region']] = datos_sedes[['pais_iso_3','pais_castellano','region_geografica']].drop_duplicates()

pbi2022 = sql^"""
               SELECT DISTINCT paises.codigo_pais, paises.nom_pais, pbi.pbi, regiones.id_region
               FROM paises
               LEFT OUTER JOIN GPD_2022 AS pbi
               ON paises.codigo_pais = pbi.Country_code
               LEFT OUTER JOIN datos_sedes
               ON datos_sedes.pais_iso_3 = paises.codigo_pais
               LEFT OUTER JOIN regiones
               ON regiones.nom_region = datos_sedes.region_geografica
               """
paises = pbi2022


redes_sociales = pd.DataFrame(columns=['id_sede','url'])


for i in range(datos_sedes.shape[0]):
    # accedo al valor de la columna redes_sociales en la posicion i
    urls =  datos_sedes.loc[i,'redes_sociales']
    
    if type(urls) == str:
        
        if urls != None:
            lista_urls = urls.split('  //  ')[:-1]
            
            df_url_sede = pd.DataFrame((zip(np.full(len(lista_urls), datos_sedes.loc[i,'sede_id']),lista_urls)),columns=['id_sede','url'])
            
            redes_sociales = pd.concat([redes_sociales,df_url_sede], axis=0,)
            
            
redes_sociales.reset_index(inplace=True,drop=True)
      

    
# =============================================================================
#  h)     
# =============================================================================
# i) Para resolver este punto, se eliminaron 3 filas de la tabla de secciones_original
# ya que habia sedes que tenian 2 secciones con el mismo nombre y lo que sucedia era que
# esas secciones tenian distinto jefe, entonces las contaba como 2. 
# Nosotros decidimos que eso solo cuente como uno. En este caso la modificacion a nivel tabla 
# seria la eliminacion de apenas 3 filas de las 516 que lleva la tabla secciones.
# La modificacion se llevo a cabo en la creacion del DataFrame de secciones (linea 295)
# Luego de creada la tabla, se le aplico un Select Distinct* y se lo igualo a secciones. 


cantidad_sedes = sql^"""
SELECT paises.nom_pais, count(*) AS sedes
FROM paises
LEFT OUTER JOIN sedes
ON paises.codigo_pais = sedes.codigo_pais
GROUP BY paises.nom_pais
 """

paises_sedes_secciones = sql^"""
SELECT paises.nom_pais, paises.codigo_pais, 
sedes.id_sede, secciones.nom_seccion
FROM paises
LEFT OUTER JOIN sedes 
ON paises.codigo_pais = sedes.codigo_pais
LEFT OUTER JOIN secciones
ON sedes.id_sede = secciones.id_sede
"""

cantidad_secciones = sql^"""
SELECT paises_sed_sec.nom_pais, paises_sed_sec.codigo_pais, 
paises_sed_sec.id_sede,
SUM(CASE WHEN paises_sed_sec.nom_seccion IS NULL THEN 0 ELSE 1 END ) as cantidad_secciones
FROM paises_sedes_secciones AS paises_sed_sec
GROUP BY paises_sed_sec.nom_pais, paises_sed_sec.codigo_pais, 
paises_sed_sec.id_sede
"""

promedio_seccionesxsede = sql^"""
SELECT cantidad_secciones.nom_pais, 
cantidad_secciones.codigo_pais, 
ROUND(AVG(cantidad_secciones.cantidad_secciones), 1) as secciones_promedio
FROM cantidad_secciones
GROUP BY cantidad_secciones.nom_pais, cantidad_secciones.codigo_pais
"""

ejercicio1 = sql^"""
SELECT paises.nom_pais AS Pais, cantidad_sedes.sedes,
promedio_seccionesxsede.secciones_promedio,
paises.pbi AS Pbi_per_Capita_2022_U$S
FROM paises
LEFT OUTER JOIN cantidad_sedes 
ON cantidad_sedes.nom_pais = paises.nom_pais
LEFT OUTER JOIN promedio_seccionesxsede
ON promedio_seccionesxsede.nom_pais = paises.nom_pais
ORDER BY cantidad_sedes.sedes DESC, paises.nom_pais 
"""

# Conclusion de lo observado: En principio, se observan resultados muy disparejos si se
# intentan relacionar los datos de sedes, secciones y pbi.
# Sin embargo, pareciera ser que la mayoria de los paises de la tabla 
# que mas PBI poseen son aquellos que poseen secciones en promedio mayores o iguales a 2.5 


# ii) La solucion final a este ejercicio 
# es la tabla de consulta "ejercicio2" 


regiones_sedes_arg = sql^"""
SELECT regiones.nom_region AS Region_geografica,
COUNT(*) AS Paises_Con_Sedes_Argentinas
FROM paises
LEFT OUTER JOIN regiones 
ON regiones.id_region = paises.id_region
LEFT OUTER JOIN ejercicio1 
ON ejercicio1.Pais = paises.nom_pais
GROUP BY Region_geografica, ejercicio1.sedes
HAVING ejercicio1.sedes >0
"""
regiones_sedes_arg = sql^"""
SELECT Region_geografica,
SUM(Paises_Con_Sedes_Argentinas) AS Paises_Con_Sedes_Argentinas
FROM regiones_sedes_arg
GROUP BY Region_geografica
"""

promedio_pbi = sql^"""
SELECT regiones.nom_region AS Region_geografica, ejercicio1.*
FROM ejercicio1
LEFT OUTER JOIN paises
ON ejercicio1.Pais = paises.nom_pais
LEFT OUTER JOIN regiones
ON regiones.id_region = paises.id_region
"""
promedio_pbi = sql^"""
SELECT promedio_pbi.Region_geografica, 
ROUND(AVG(promedio_pbi.Pbi_per_Capita_2022_U$S),2) AS Pbi_per_Capita_2022_U$S
FROM promedio_pbi
WHERE promedio_pbi.sedes>0
GROUP BY Region_geografica
"""

ejercicio2 = sql^"""
SELECT regiones_sedes_arg.Region_geografica,
regiones_sedes_arg.Paises_Con_Sedes_Argentinas,
promedio_pbi.Pbi_per_Capita_2022_U$S
FROM regiones_sedes_arg
INNER JOIN promedio_pbi
ON promedio_pbi.Region_geografica = regiones_sedes_arg.Region_geografica
ORDER BY promedio_pbi.Pbi_per_Capita_2022_U$S DESC
"""

# Conclusion de lo observado: Las 2 regiones con menos sedes argentinas, 
# en este caso Oceania y America del Norte, y las 2 regiones con mas sedes argentinas, 
# en este caso Europa Occidental y Asia, son aquellos que mas PBI tienen.
# En nuestra region geografica de America, solo America del Norte posee en promedio un PBI alto
# Observamos tambien que el continente africano posee en promedio un PBI muy bajo 
# con respecto al resto del promedio de las demas regiones


# =============================================================================
# i) Mostrar, utilizando herramientas de visualizacion, la siguiente informacion: 
# 
# i) Mostrar cantidad de sedes por region geografica. 
#    Ordenados de manera decreciente por dicha cantidad.
# =============================================================================

# Dataframe de ejercicio2 modificado para que aparesca ordenado en el grafico
ejercicio2ord = ejercicio2.sort_values('Paises_Con_Sedes_Argentinas', ascending=False)

#  lista de 9 colores para las regiones
colores = ['blue', 'green', 'purple', 'purple', 'green', 'orange', 'orange', 'purple', 'gray']

# Crea el grafico de barras
bars = plt.bar(ejercicio2ord['Region_geografica'], 
               ejercicio2ord['Paises_Con_Sedes_Argentinas'], 
               color='black')

plt.bar(ejercicio2ord['Region_geografica'],
        ejercicio2ord['Paises_Con_Sedes_Argentinas'],
        color=colores)

#Linea punteada de cada valor en y 
plt.grid(axis='y', color='gray', linestyle='dashed') 

# Rotar los textos en el eje x para que sean legibles
plt.xticks(rotation=60, ha='right', fontsize=8)  # 'ha' es para alineación horizontal

# Aca se le agrega la cantidad arriba de cada bin
plt.bar_label(bars, fmt='%d', fontsize=9, label_type='edge', color='black', weight='bold')

# Agregar titulo y limites al eje y
plt.title('Cantidad de Sedes por Región')    
plt.ylim(0,26)
plt.gca().spines['right'].set_visible(False) # se borra linea derecha de margen
plt.gca().spines['top'].set_visible(False) # se borra linea debajo del titulo
plt.tick_params(axis='y', left=False) # se borra tick de valores del eje y


# =============================================================================
# Conclusion: 
# Como era de esperarse, nuestro continente americano es el que tiene
# mayor cantidad de sedes argentinas (28) en dichos paises que corresponden a America.
# Sin embargo, tenemos casi la misma cantidad de sedes argentinas en 
# el continente Europeo con 26.
# Al parecer se le da primero mayor relevancia diplomatica al sector de Europa Occidental 
# que a Europa Central y Oriental.
# El continente africano cuenta con muy pocas sedes argentinas, pero no tanto como
# Oceania que cuenta con solo 2 sedes argentinas. 
# Seria interesante que Argentina lograra mayor contacto con el continente de Oceania 
# =============================================================================

