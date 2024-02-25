# -*- coding: utf-8 -*-
"""
Creado: 16/02/2024
Materia: Laboratorio de Datos - FCEyN - UBA
@autores:  Pons Valentino, Porcel Carlos, Suarez Javier
"""
### Importo librearias
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#import seaborn as sns


### cargo los datos crudos
  
# cargo los dataframes de TWB

pbi_paises = pd.read_csv('./TablasOriginales/API_NY.GDP.PCAP.CD_DS2_en_csv_v2_73.csv',skiprows=4)

datos_paises = pd.read_csv('./TablasOriginales/Metadata_Country_API_NY.GDP.PCAP.CD_DS2_en_csv_v2_73.csv')

metadata = pd.read_csv('./TablasOriginales/Metadata_Indicator_API_NY.GDP.PCAP.CD_DS2_en_csv_v2_73.csv')

# cargo Dataframes del Ministerio

secciones_original = pd.read_csv('./TablasOriginales/lista-secciones.csv')

sedes_original = pd.read_csv('./TablasOriginales/lista-sedes.csv')

datos_sedes = pd.read_csv('./TablasOriginales/lista-sedes-datos.csv')
    
### Creo los esquemas necesarios para el proyecto 

# creo los esquemas en dataframe vacios

redes_sociales = pd.DataFrame(columns=['id_sede','url'])

sedes = pd.DataFrame(columns=['id_sede','nom_sede','codigo_pais'])

secciones  = pd.DataFrame(columns=['id_sede','nom_seccion'])

paises  = pd.DataFrame(columns=['codigo_pais','nom_pais','id_region','pbi'])

regiones = pd.DataFrame(columns=['id_region','nom_region'])



### importo los datos a los dataframe vacios

# Regiones
# importo:
#   nom_region del dataframe datos_paises
regiones['nom_region'] = datos_paises['Region'].sort_values().unique() # selecciones los valores, ordeno y luego dejo solo los valores unicos
#   genero un id_regino para cada region
regiones['id_region'] = np.array(range(1,len(regiones['nom_region'])+1))# el array es  [1,2,3,4,5,6,7,8] 

# Paises
# importo:
#   codigo_pais, nom_pais, id_region del dataframe datos_paises
paises[['codigo_pais','nom_pais','id_region']] = datos_paises[['Country Code','TableName','Region']]    
#   pib del dataframe pib_paises
paises['pbi'] = pd.merge(paises['codigo_pais'], pbi_paises[['Country Code','2022']],
                         left_on='codigo_pais', right_on='Country Code')['2022']# Hago un natural join con codigo_pais del dataframe paises
                                                                                # y Country Code de pbi_paises para accedes a el pbi en 2022,
                                                                                # esos valores los importo a la columna pbi

# pais[['codigo_pais','nom_territorio','id_region']] = datos_sedes[['pais_iso_3','pais_castellano','region_geografica']].drop_duplicates()
# Sedes
# importo:
#   id_sede,nom_sede,codigo_territorio del dataframe datos_sedes
sedes[['id_sede','nom_sede','codigo_territorio']] = datos_sedes[['sede_id','sede_desc_castellano','pais_iso_3']]

# Secciones
# importo:
#   id_sede, nom_seccion del dataframe secciones_original
secciones[['id_sede','nom_seccion']] = secciones_original[['sede_id','sede_desc_castellano']]

# Redes Sociales
#   importo id_sede, url del dataframe datos_sedes
redes_sociales[['id_sede','url']] = datos_sedes[['sede_id','redes_sociales']]



### Limpieza y estandarizacion    
# Regiones
#   elimino la ultima fila pues tiene valor nulo
regiones.dropna(inplace=True)

# Paises
#   elimino las regiones de mi dataframe paises
paises.dropna(inplace=True)#subset=[''])
#   cambio las regiones por su id
paises['id_region'] = paises['id_region'].apply(lambda x: regiones[regiones.loc[:,'nom_region'] == x]['id_region'].values[0])
#   reseto sus indices
paises.reset_index(inplace=True,drop=True)

# Redes Sociales:   
#   Crep un dataframe con los datos sin precesar
redes_sociales_s_procesar = redes_sociales.copy()
#   Vacion el dataframe   
redes_sociales = pd.DataFrame(columns=['id_sede','url'])

#   Elimino las sedes que no tienen redes sociales
redes_sociales_s_procesar.dropna(inplace=True)
#   Reseteo el indice
redes_sociales_s_procesar.reset_index(inplace=True,drop=True)
#   Vuelvo los valores de la columna url en atomicos
for i in range(redes_sociales_s_procesar.shape[0]):
    # accedo al valor de la columna redes_sociales por la posicion en i
    urls =  redes_sociales_s_procesar.loc[i,'url']   
    # creo una lista con las urls eliminando el ultimo elemento
    lista_urls = urls.split('  //  ')
    # si la lista tiene mas de un elemento significa que elutlimo elemento es un espacio, por lo cual lo quito
    if len(lista_urls) >=2:
        lista_urls = lista_urls[:-1]
    # creo una lista de igual longitud que lista_urls con todos sus valores igual a la sede que pertenece las urls
    lista_full_sede_id = np.full(len(lista_urls), redes_sociales_s_procesar.loc[i,'id_sede'])
    # creo una lista de tuplas (sede_id, urls)
    lista_tuplas_urls = zip(lista_full_sede_id,lista_urls)
    # genero un dataframe con las tuplas de lista_tuplas_urls
    df_url_sede = pd.DataFrame(lista_tuplas_urls,columns=['id_sede','url'])
    # concateno las las nuevas urls al dataframe de redes sociales
    redes_sociales = pd.concat([redes_sociales,df_url_sede], axis=0,ignore_index=True)          
#   reseteo el indice de redes_sociales
redes_sociales.reset_index(inplace=True,drop=True)

# Secciones
#   Elimino duplicados
secciones.drop_duplicates(inplace=True)



### Expoerto los dataframes
lista_esquemas = [regiones,paises,sedes,secciones,redes_sociales]
nombre_cvs  = ['regiones.csv','paises.csv','sedes.csv','secciones.csv','redes_sociales.csv']
for esquema,nombre in zip(lista_esquemas,nombre_cvs):
    esquema.to_csv('./TablasLimpias/'+nombre,index=False, encoding = 'utf-8')


##################

    
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

#ejercicio III)
"""
IMPORTANTE: Para este ejercicio uso dataframe "reporte" generado en el ejercicio 4
La idea es ir agregando al conjuntoRedes las redes del pais al que estoy iterando.(Se va iterar en data_redes).
Luego se agrega en el dataframe creado mas abajo "res" el nombre del pais y el tamaño del conjunto
siendo este el numero de redes sociales distintas que tienen.Cada vez que un nuevo pais se itera el conjunto vuelve a vaciarse.
"""
def tipos_redes_pais():
    datos_redes = reporte[['Pais','Redes Sociales']] #Tomo de reporte las columnas que me interesan
    res = pd.DataFrame(columns=['Pais' , 'nro de redes' ]) #creo el data frame que voy a completar
    conjuntoRedes = set()  
 
    for i in range(0,len(datos_redes)-1):
        
        if (datos_redes.loc[i , 'Pais'] != datos_redes.loc[i+1,'Pais']):
            conjuntoRedes.add(datos_redes.loc[i,'Redes Sociales'])
            nueva_fila = pd.DataFrame({'Pais' : datos_redes.loc[i,'Pais'] , 'nro de redes' : len(conjuntoRedes)} , index=[0])
            res = pd.concat([res,nueva_fila],axis = 0) 
            conjuntoRedes=set()
            
        else:
            conjuntoRedes.add(datos_redes.loc[i,'Redes Sociales'])
            
    ultimo = len(datos_redes)-1 #ultimo caso por separado
    
    if (datos_redes.loc[ultimo , 'Pais'] != datos_redes.loc[ultimo-1,'Pais']):
      nueva_fila = pd.DataFrame({'Pais' : datos_redes.loc[ultimo,'Pais'] , 'nro de redes' : 1} , index=[0])
      res = pd.concat([res,nueva_fila],axis = 0)       
      
    return res
res_ejercicio3 = tipos_redes_pais()

#ejercicio IV)
"""
Genero un nuevo data frame llamado reporte el cual es igual a redes_sociales solo que no contiene las tuplas con urls de mala calidad
Se consideraron urls de mala calidad aquellos que no empezaban con http , www o alguna red social seguida de un ".com".
Ejemplo instagram.com. 

"""
def dataFrame_reporteBase(redes_sociales): #crea una copia de redes_sociales llamada reporte el cual vamos a usar para el ejercicio
    res = redes_sociales 
    res = res[res['url'].str.startswith(('http', 'www' ,'twitter' ,'Twitter' ,'linkedin', 'Linkedin' ,
                                                     'facebook','Facebook' ,'instagram','Instagram' ))] #filtro por las condiciones aclaradas
    res = res.reset_index(drop=True) #restablezco indices para evitar errores
    
    res.insert(1,'Redes Sociales' , pd.NA)#agrego columna Redes sociales
    return res

reporteBase = dataFrame_reporteBase(redes_sociales)

def busqueda_red_social(reporteBase): #Esta funcion agrega a reporte una columna la cual notifica que red social utiliza una sede especifica
    lista_de_redes = ['twitter' ,'facebook','instagram','linkedin','flickr','youtube']
    redSocial = None
    reporte = reporteBase
    for i in range(0,len(reporteBase)):
        url = reporte.loc[i,'url']
        for red in lista_de_redes:
            if red in url:
                redSocial = red
                break
        reporte.at[i,'Redes Sociales'] = redSocial 
        
    return reporte


def reporte_final(reporteBase):#agrega la columna Pais en las sedes correspondientes y ordena ascendentemente en el orden especificado
    res = busqueda_red_social(reporteBase)
    res = res.rename(columns={'id_sede': 'sede_id'})#Cambio el nombre de la columna para que datos_sedes y res tengan el mismo nombre en esa columna
    res = pd.merge(res, datos_sedes, on='sede_id', how='left') #Left join con datos_sedes con condicion de union los id de las sedes
    res = res[['pais_castellano' , 'sede_id' , 'Redes Sociales' , 'url' ]]#Me quedo con las columnas que me interesan 
    res = res.rename(columns={'pais_castellano':'Pais' , 'sede_id':'Sede' , 'url':'URL'})#Cambio de nombre de columnas
    res = res.sort_values(by=['Pais', 'Sede' , 'Redes Sociales' , 'URL'], ascending=True)
    res = res.reset_index(drop=True)
    return res

        
reporte = reporte_final(reporteBase)


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




























