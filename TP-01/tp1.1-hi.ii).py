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
from matplotlib import ticker, rcParams
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
ejercicio1= sql^"""
SELECT *
FROM ejercicio1
WHERE Pbi_per_Capita_2022_U$S IS NOT NULL
"""

# Conclusion de lo observado: En principio, se observan resultados muy disparejos si se
# intentan relacionar los datos de sedes, secciones y pbi.
# Sin embargo, pareciera ser que la mayoria de los paises de la tabla 
# que mas PBI poseen son aquellos que poseen secciones en promedio mayores o iguales a 2.5 


# ii) La solucion final a este ejercicio 
# es la tabla de consulta "ejercicio2" 


# ra = sql^"""SELECT DISTINCT r.nom_region AS 'Región geográfica', 
#                 count(*) AS 'Países Con Sedes Argentinas', 
#                 ROUND(AVG(p.pbi)) As 'Promedio PBI per Cápita 2022 (Millones U$S)'
# from sedes as s
# inner join paises as p 
# on s.codigo_pais = p.codigo_pais
# inner join regiones as r 
# on p.id_region = r.id_region
# GROUP by r.nom_region
# order by AVG(p.pbi) DESC """



# regiones_sedes_arg= sql^"""
# SELECT regiones.nom_region AS Region_geografica, COUNT(ejercicio1.sedes) AS Paises_Con_Sedes_Argentinas
# FROM ejercicio1 
# LEFT OUTER JOIN paises 
# ON paises.nom_pais = ejercicio1.Pais
# LEFT OUTER JOIN regiones
# ON regiones.id_region = paises.id_region 
# WHERE ejercicio1.sedes >0
# GROUP BY regiones.nom_region
# """

promedio_pbi = sql^"""
SELECT regiones.nom_region AS Region_geografica, ejercicio1.*
FROM ejercicio1
LEFT OUTER JOIN paises
ON ejercicio1.Pais = paises.nom_pais
LEFT OUTER JOIN regiones
ON regiones.id_region = paises.id_region
"""
ejercicio2 = sql^"""
SELECT promedio_pbi.Region_geografica, 
COUNT(*) AS Paises_Con_Sedes_Argentinas,
ROUND(AVG(promedio_pbi.Pbi_per_Capita_2022_U$S),2) AS Promedio_Pbi_per_Capita_2022_U$S
FROM promedio_pbi
GROUP BY promedio_pbi.Region_geografica
ORDER BY promedio_Pbi_per_Capita_2022_U$S DESC
"""


# Conclusion de lo observado: Las 2 regiones con menos sedes argentinas, 
# en este caso Oceania y America del Norte, y las 2 regiones con mas sedes argentinas, 
# en este caso Europa Occidental y Asia, son aquellos que mas PBI tienen.
# En nuestra region geografica de America, solo America del Norte posee en promedio un PBI alto
# Observamos tambien que el continente africano posee en promedio un PBI muy bajo 
# con respecto al resto del promedio de las demas regiones



#ejercicio III)
"""
IMPORTANTE: Para este ejercicio uso dataframe "reporte" generado en el ejercicio 4. 

"""
# ejercicio IV


reporte = sql^ """
          SELECT id_sede AS sede_id  , url
          FROM redes_sociales
          WHERE url LIKE 'http%' OR url LIKE 'www%' OR url LIKE 'twitter%' OR url LIKE 'Twitter%'
                                OR url LIKE 'facebook%' OR url LIKE 'Facebook%' OR url LIKE 'instagram%'
                                OR url LIKE 'Instagram%' OR url LIKE 'linkedin%'    
"""
reporte = sql^ """
          SELECT sede_id ,
          CASE 
              WHEN url LIKE '%twitter%' OR url LIKE '%Twitter%' THEN 'Twitter'
              WHEN url LIKE '%instagram%' OR url LIKE '%Instagram%' THEN 'Instagram'
              WHEN url LIKE '%facebook%' OR url LIKE '%Facebook%' THEN 'Facebook'
              WHEN url LIKE '%linkedin%' OR url LIKE '%Linkedin%' THEN 'Linkedin'
              WHEN url LIKE '%flickr%' OR url LIKE '%Flickr%' THEN 'Flickr'
              WHEN url LIKE '%youtube%' OR url LIKE '%Youtube%' THEN 'Youtube'
              ELSE ''
              END AS Red_social , url
              FROM reporte 
                """
reporte = sql^ """
            SELECT pais_castellano AS Pais , r.sede_id AS Sede , Red_social , url AS URL
            FROM reporte AS r
            LEFT JOIN datos_sedes AS d
            ON r.sede_id = d.sede_id
                """
#Ordeno                
reporte = sql^ """  
            SELECT *
            FROM reporte
            ORDER BY Pais ASC , Sede ASC , Red_social ASC , URL ASC
                """




res = sql^"""
            SELECT Pais , Red_social , COUNT(Red_social) AS nro_redes
            FROM reporte
            GROUP BY Pais , Red_social
            """
tabla_h_III = sql^"""
        SELECT Pais , COUNT(Pais) AS nro_redes
        FROM res
        GROUP BY Pais
        ORDER BY Pais ASC , nro_redes ASC

        """




#ejercicio IV)
# 
# Genero un nuevo data frame llamado reporte el cual es igual a redes_sociales solo que no contiene las tuplas con urls de mala calidad
# Se consideraron urls de mala calidad aquellos que no empezaban con http , www o alguna red social seguida de un ".com".
# Ejemplo instagram.com. 
# 



# =============================================================================
# i) Mostrar, utilizando herramientas de visualizacion, la siguiente informacion: 
# 
# i) Mostrar cantidad de sedes por region geografica. 
#    Ordenados de manera decreciente por dicha cantidad.
# =============================================================================

sedesXregion = sql^"""
SELECT Region_geografica, SUM(sedes) as Cantidad_Sedes
FROM promedio_pbi
GROUP BY Region_geografica
"""

# Dataframe de ejercicio2 modificado para que aparesca ordenado en el grafico
sedesXregionOrd = sedesXregion.sort_values('Cantidad_Sedes', ascending=False)

#  lista de 9 colores para las regiones
colores = ['blue', 'green', 'purple', 'blue', 'blue', 'orange', 'green', 'orange', 'gray']

# Crea el grafico de barras
bars = plt.bar(sedesXregionOrd['Region_geografica'],
        sedesXregionOrd['Cantidad_Sedes'],
        color=colores)

#Linea punteada de cada valor en y 
plt.grid(axis='y', color='gray', linestyle='dashed') 

# Rotar los textos en el eje x para que sean legibles
plt.xticks(rotation=60, ha='right', fontsize=8)  # 'ha' es para alineación horizontal

# Aca se le agrega la cantidad arriba de cada bin
plt.bar_label(bars, fmt='%d', fontsize=9, label_type='edge', color='black', weight='bold')

# Agregar titulo y limites al eje y
plt.title('Cantidad de Sedes por Región')    
plt.ylim(0,50)
plt.gca().spines['left'].set_visible(False) # se borra linea derecha de margen
plt.gca().spines['top'].set_visible(False) # se borra linea debajo del titulo
plt.tick_params(axis='y', left=False) # se borra tick de valores del eje y
plt.gca().set_facecolor('#D7DBDD') # Agregar fondo de color al gráfico
plt.gcf().set_facecolor('#D7DBDD') # Agregar fondo de color al gráfico



# bars = plt.bar(ejercicio2ord['Region_geografica'], 
#                ejercicio2ord['Paises_Con_Sedes_Argentinas'], 
#                color='black')


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



#EJERCICIO i III
#Grafico PBI y numero de sedes argentinas por pais.

pbi_2022_sedes = sql^"""
                    SELECT pbi2022.nom_pais , pbi , sedes
                    FROM pbi2022
                    LEFT JOIN cantidad_sedes
                    ON pbi2022.nom_pais = cantidad_sedes.nom_pais
                    ORDER BY pbi ASC
                    """ 
                    
y = pbi_2022_sedes['pbi']
x = pbi_2022_sedes['sedes'] 
plt.xticks(range(0, 13, 1))
plt.yticks(range(0,110000,20000))
rcParams['font.family'] = 'sans-serif'
plt.title('Relacion PBI y numero de sedes argentinas por pais')  
           # Modifica el tipo de letra
rcParams['axes.spines.right'] = False            
rcParams['axes.spines.left']  = True            
rcParams['axes.spines.top']   = False  
plt.ylabel('PBI (usd)')
plt.xlabel('nroº de sedes')
plt.scatter(x,y,s=5 )





