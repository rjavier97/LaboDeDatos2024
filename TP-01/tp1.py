# -*- coding: utf-8 -*-
"""
Creado: 16/02/2024
Materia: Laboratorio de Datos - FCEyN - UBA
@autores: Carlos Porcel, Javier Suarez, Valentino Pons
"""
# Importo librearias
import pandas as pd
import numpy as np
from inline_sql import sql, sql_val

# cargo los dataframes de TWB

pbi_paises = pd.read_csv('API_NY.GDP.PCAP.CD_DS2_en_csv_v2_73.csv',skiprows=4)

codigo_paises = pd.read_csv('Metadata_Country_API_NY.GDP.PCAP.CD_DS2_en_csv_v2_73.csv')

metadata = pd.read_csv('Metadata_Indicator_API_NY.GDP.PCAP.CD_DS2_en_csv_v2_73.csv')

# cargo Dataframes del Ministerio

secciones_original = pd.read_csv('lista-secciones.csv')

sedes_original = pd.read_csv('lista-sedes.csv')

datos_sedes = pd.read_csv('lista-sedes-datos.csv')

    
'''
Anslisis datos TWB

Descripcion info. de TWB:
    El PIB per cápita es el producto interno bruto dividido por la población a mitad de año. 
    El PIB es la suma del valor agregado bruto de todos los productores residentes en la economía más los impuestos 
    sobre los productos y menos los subsidios no incluidos en el valor de los productos. Se calcula sin hacer deducciones por 
    depreciación de activos fabricados o por agotamiento y degradación de recursos naturales. Los datos están en dólares estadounidenses
    actuales.
    
    
csv -> Nombre para el analisis -> Nombre variable dataframe:
    - API_NY.GDP.PCAP.CD_DS2_en_csv_v2_73 -> PBI per cápita(USD) -> pbi_paises
    - Metadata_Country_API_NY.GDP.PCAP.CD_DS2_en_csv_v2_73 -> Código de los Paises -> codigo_paises 
    - Metadata_Indicator_API_NY.GDP.PCAP.CD_DS2_en_csv_v2_73 -> Metadata -> metadata

Info. tablas:
    
- PBI per cápita:
    - Columnas: 'Country Name', 'Country Code', 'Indicator Name', 'Indicator Code',
           '1960', '1961', '1962', '1963', '1964', '1965', '1966', '1967', '1968',
           '1969', '1970', '1971', '1972', '1973', '1974', '1975', '1976', '1977',
           '1978', '1979', '1980', '1981', '1982', '1983', '1984', '1985', '1986',
           '1987', '1988', '1989', '1990', '1991', '1992', '1993', '1994', '1995',
           '1996', '1997', '1998', '1999', '2000', '2001', '2002', '2003', '2004',
           '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013',
           '2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022',
           'Unnamed: 67'
           
    - Descripcion columnas:
        - 'Country Name': Nombre del País
        - 'Country Code': Código del País
        - 'Indicator Name': Nombre del indicador
        - 'Indicator Code'': Código del indicador
        -['1960', '1961', ... ,'2022']: PBI per cápita del país en ese año
        - 'Unnamed: 67': Columna sin sin datos
        
    - Tipos de datos de las columnas:
        -Categoricos:
            - Nominal:
                - 'Country Name'
                - 'Country Code''
                -'Indicator Name'
                - 'Indicator Code'
                
        - Cuantitativos:
            - Discreto:
                - Las columnas de los años: ['1960', '1961', ... ,'2022']
                
    - Formato datos en columnas:
        - str: 'Country Name', 'Country Code', 'Indicator Name', 'Indicator Code'
        - float: '1960', '1961', ... ,'2022'
        
    - Observaciones:
        - Columna 'Unnamed: 67' todos sus datos son nulos.
        - Sin filas repetidas.
        
- Código de los Paises    
    - Columnas:'Country Code', 'Region', 'IncomeGroup', 'SpecialNotes', 'TableName',
               'Unnamed: 5'
               
    - Descripcion columnas: 
        - 'Country Code': Código del País
        - 'Region': Región a la que pertenece el país
        - 'IncomeGroup': Grupo de ingresos
        - 'SpecialNotes': Nota sobre el país
        - 'TableName': Nombre que lleva el país en la tabla PBI per cápita(USD)
        - 'Unnamed: 5': Columna sin datos
     
    - Tipos de datos de las columnas:
        -categoricos:
            - Nominal: Todas las columnas, excepto 'IncomeGroup' y 'Unnamed: 5'
            - Ordinal:'IncomeGroup'
           
    - Formato datos en columnas:
        - str: 'Country Code', 'Region', 'IncomeGroup', 'SpecialNotes', 'TableName'
    - Observaciones:
        - Columna 'Unnamed: 5' todos sus datos son nulos.
        - Sin datos duplicados
        
- Metadata:
    - Columnas:'INDICATOR_CODE', 'INDICATOR_NAME', 'SOURCE_NOTE',
               'SOURCE_ORGANIZATION', 'Unnamed: 4'
               
    - Descripcion columnas: 
        - 'INDICATOR_CODE': Código del indicador
        - 'INDICATOR_NAME': Nombre del Indicador
        - 'SOURCE_NOTE': Nota sobre el indicador 
        - 'SOURCE_ORGANIZATION': Organizacion/es que recolecaton los datos
        - 'Unnamed: 4': Columna sin datos
    - Tipos de datos de las columnas:
        -categoricos:
            - Nominal: Todas las columnas, excepto 'Unnamed: 4'
    - Formato datos en columnas:
        - str: Todas las columnas, excepto 'Unnamed: 4'
    - Observaciones:
        - Solo hay una tupla
        - Columna 'Unnamed: 4' todos sus datos son nulos.


Anslisis datos Ministerio de Relaciones Exteriores, Comercio Internacional y Culto

Descripcion info.:
    Datos de las Representaciones Argentinas en el exterior.
CSV -> Nombre para el analisis -> Nombre variable dataframe:
    - lista-secciones -> **Secciones** -> secciones
    - lista-sedes -> **Sedes** -> sedes
    - lista-sedes-datos -> **Datos de Sedes** -> datos_sedes
    
Info. tablas:
    - **Secciones**
        - Columnas: 'sede_id', 'sede_desc_castellano', 'sede_desc_ingles', 'tipo_seccion','nombre_titular', 'apellido_titular', 'cargo_titular','telefono_principal', 'telefonos_adicionales', 'celular_de_guardia', 'celulares_adicionales', 'fax_principal', 'faxes_adicionales', 'correo_electronico', 'correos_adicionales', 'sitio_web', 'sitios_web_adicionales', 'atencion_dia_desde', 'atencion_dia_hasta', 'atencion_hora_desde', 'atencion_hora_hasta', 'comentario_del_horario', 'temas'
        - Descripcion columnas: 
            - 'sede_id': Código de Sede 
            - 'sede_desc_castellano': Denominación de la Sección de la Sede en español 
            - 'sede_desc_ingles': Denominación de la Sección de la Sede en inglés 
            - 'tipo_seccion': Tipo de sección 
            - 'nombre_titular': Nombre del funcionario titular de la Sección 
            - 'apellido_titular': Apellido del funcionario titular de la Sección 
            - 'cargo_titular': Cargo del funcionario titular de la Sección 
            - 'telefono_principal': Número telefónico principal de la Sección 
            - 'telefonos_adicionales': Números telefónicos adicionales de la Sección 
            - 'celular_de_guardia': Número celular de guardia de la Sección 
            - 'celulares_adicionales': Números celulares adicionales de la Sección 
            - 'fax_principal': Número de fax principal de la Sección 
            - 'faxes_adicionales': Números de fax adicionales de la Sección 
            - 'correo_electronico': Dirección correo electrónico principal de la Sección 
            - 'correos_adicionales': Direcciones correo electrónico adicionales de la Sección 
            - 'sitio_web': URL sitio web de la Sección 
            - 'sitios_web_adicionales': URLs sitios webs adicionales de la Sección 
            - 'atencion_dia_desde': Día de atención de la Sección desde 
            - 'atencion_dia_hasta': Día de atención de la Sección hasta 
            - 'atencion_hora_desde': Hora de atención de la Sección desde 
            - 'atencion_hora_hasta': Hora de atención de la Sección hasta 
            - 'comentario_del_horario': Comentario asociado al horario de atención de la Sección 
            - 'temas': Temas de competencia de la Sección 
            
        - Tipos de datos de las columnas:
            - Categoricos:
                - Nominal: 'sede_id', 'sede_desc_castellano', 'sede_desc_ingles', 'tipo_seccion','nombre_titular', 'apellido_titular', 'cargo_titular','telefono_principal', 'telefonos_adicionales', 'celular_de_guardia', 'celulares_adicionales', 'fax_principal', 'faxes_adicionales', 'correo_electronico', 'correos_adicionales', 'sitio_web', 'sitios_web_adicionales'
            - Fecha y hora: 'atencion_dia_desde', 'atencion_dia_hasta', 'atencion_hora_desde', 'atencion_hora_hasta', 'comentario_del_horario'
                
        - Formato datos en columnas:
            - str : Todas las columnas, excepto la columna 'temas'
            
        - Observaciones:
            - Columna 'temas' sin datos
            - Sin columnas repetidas
            
    - **Sedes**
        - Columnas: 'sede_id', 'sede_desc_castellano', 'sede_desc_ingles', 'pais_iso_2', 'pais_iso_3', 'pais_castellano', 'pais_ingles', 'ciudad_castellano', 'ciudad_ingles', 'estado', 'sede_tipo'
        
        - Descripcion columnas: 
            - 'sede_id': Código de Sede 
            - 'sede_desc_castellano': Denominación de la Sede en español 
            - 'sede_desc_ingles': Denominación de la Sede en inglés 
            - 'pais_iso_2': Código ISO2 país donde está la Sede 
            - 'pais_iso_3': Código ISO3 país donde está la Sede 
            - 'pais_castellano': País donde está la Sede en español 
            - 'pais_ingles': País donde está la Sede en inglés 
            - 'ciudad_castellano': Ciudad donde está la Sede en español 
            - 'ciudad_ingles': Ciudad donde está la Sede en inglés 
            - 'estado': Estado (activo o inactivo) 
            - 'sede_tipo': Tipo de sede 
            
        - Tipos de datos de las columnas:
            - Categoricos:
                - Nominal: Todas las columnas,excepto 'estado'
                - Binario: 'estado'
                
        - Formato datos en columnas:
            - str: Todas las columnas 
            
        - Observaciones:
            -
            
    - **Datos de Sedes**
        - Columnas: 'sede_id', 'sede_desc_castellano', 'sede_desc_ingles', 'pais_castellano', 'pais_ingles', 'region_geografica', 'pais_iso_2', 'pais_iso_3', 'pais_codigo_telefonico', 'ciudad_castellano', 'ciudad_ingles', 'ciudad_zona_horaria_gmt', 'ciudad_codigo_telefonico', 'estado', 'titular_nombre', 'titular_apellido', 'titular_cargo', 'direccion', 'codigo_postal', 'telefono_principal', 'telefonos_adicionales', 'celular_guardia', 'celulares_adicionales', 'fax_principal', 'faxes_adicionales', 'correo_electronico', 'correos_electronicos_adicionales', 'sitio_web', 'sitios_web_adicionales', 'redes_sociales', 'atencion_dia_desde', 'atencion_dia_hasta', 'atencion_hora_desde', 'atencion_hora_hasta', 'atencion_comentario', 'concurrencias', 'circunscripcion'
        
        - Descripcion columnas: 
            - 'sede_desc_castellano': Denominación de la Sede en español 
            - 'sede_desc_ingles': Denominación de la Sede en inglés 
            - 'pais_castellano': País donde está la Sede en español 
            - 'pais_ingles': País donde está la Sede en inglés 
            - 'region_geografica': Región geográfica 
            - 'pais_iso_2': Código ISO2 país donde está la Sede 
            - 'pais_iso_3': Código ISO3 país donde está la Sede 
            - 'pais_codigo_telefonico Código telefónico del país 
            - 'ciudad_castellano': Ciudad donde está la Sede en español 
            - 'ciudad_ingles': Ciudad donde está la Sede en inglés 
            - 'ciudad_zona_horaria_gmt': Zona horaria de la ciudad (GMT) 
            - 'ciudad_codigo_telefonico': Código telefónico de la ciudad 
            - 'estado': Estado (activo o inactivo) 
            - 'titular_nombre': Nombre del funcionario titular de la Sede 
            - 'titular_apellido': Apellido del funcionario titular de la Sede 
            - 'titular_cargo': Cargo del funcionario titular de la Sede 
            - 'direccion': Dirección postal de la Sede 
            - 'codigo_postal': Código postal correspondiente a la dirección de la Sede 
            - 'telefono_principal': Número telefónico principal de la Sede 
            - 'telefonos_adicionales': Números telefónicos adicionales de la Sede 
            - 'celular_guardia': Número celular de guardia de la Sede 
            - 'celulares_adicionales': Números celulares adicionales de la Sede 
            - 'fax_principal': Número de fax principal de la Sede 
            - 'faxes_adicionales': Números de fax adicionales de la Sede 
            - 'correo_electronico': Dirección correo electrónico principal de la Sede 
            - 'correos_electronicos_adicionales': Direcciones correo electrónico adicionales de la Sede 
            - 'sitio_web': URL sitio web de la Sede 
            - 'sitios_web_adicionales': URLs sitios webs adicionales de la Sede 
            - 'redes_sociales': Direcciones de la Sede en las redes sociales 
            - 'atencion_dia_desde': Día de atención de la Sede desde 
            - 'atencion_dia_hasta': Día de atención de la Sede hasta 
            - 'atencion_hora_desde': Hora de atención de la Sede desde 
            - 'atencion_hora_hasta': Hora de atención de la Sede hasta 
            - 'atencion_comentario': Comentario asociado al horario de atención de la Sede 
            - 'concurrencias': Concurrencias de la Sede 
            - 'circunscripcion': Circunscripción Consular 
            
        - Tipos de datos de las columnas:
            - Categoricos:
                - Nominal: 'sede_id', 'sede_desc_castellano', 'sede_desc_ingles', 'pais_castellano', 'pais_ingles', 'region_geografica', 'pais_iso_2', 'pais_iso_3', 'pais_codigo_telefonico', 'ciudad_castellano', 'ciudad_ingles', 'ciudad_zona_horaria_gmt', 'ciudad_codigo_telefonico', 'titular_nombre', 'titular_apellido', 'titular_cargo', 'direccion', 'codigo_postal', 'telefono_principal', 'telefonos_adicionales', 'celular_guardia', 'celulares_adicionales', 'fax_principal', 'faxes_adicionales', 'correo_electronico', 'correos_electronicos_adicionales', 'sitio_web', 'redes_sociales', 'circunscripcion'
                - Binario: 'estado'
            - Fecha y hora: 'atencion_dia_desde', 'atencion_dia_hasta', 'atencion_hora_desde', 'atencion_hora_hasta', 'atencion_comentario'

        - Formato datos en columnas:
            - int: 'pais_codigo_telefonico', 'ciudad_zona_horaria_gmt', 'ciudad_codigo_telefonico'
        - Observaciones:
            - La columna 'sitios_web_adicionales' no tiene datos
            
'''

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

'''
F = {
     DF1: 'id_sede' -> {'nom_sede','codigo_pais'},
     DF2: 'id_sede' -> 'url',
     DF4: 'codigo_pais' -> 'nom_pais','id_region','PIB'
     DF5: 'id_region' -> 'nom_region'
     }


F+ = {
      
      
      
      }


'''




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
SELECT paises_sed_sec.nom_pais, paises_sed_sec.pais, 
paises_sed_sec.id_sede,
SUM(CASE WHEN ter_sed_sec.nom_seccion IS NULL THEN 0 ELSE 1 END ) as cantidad_secciones
FROM paises_sedes_secciones AS paises_sed_sec
GROUP BY ter_sed_sec.nom_pais, paises_sed_sec.codigo_pais, 
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
(Paises_Con_Sedes_Argentinas) AS Paises_Con_Sedes_Argentinas
FROM regiones_sedes_arg
GROUP BY Region_geografica
"""

promedio_pbi = sql^"""
SELECT regiones.nom_region AS Region_geografica, ejercicio1.*
FROM ejercicio1
LEFT OUTER JOIN paises
ON ejercicio1.Pais = paises.nom_pais
LEFT OUTER JOIN regiones
ON regiones.id_region = pais.id_region
WHERE ejercicio1.sedes >0
"""
promedio_pbi = sql^"""
SELECT promedio_pbi.Region_geografica, 
ROUND(AVG(promedio_pbi.Pbi_per_Capita_2022_U$S),2) AS Pbi_per_Capita_2022_U$S
FROM promedio_pbi
WHERE sedes>0
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




SELECT ter_sed_sec.nom_territorio, ter_sed_sec.codigo_territorio,
sedes.id_sede,
count(CASE WHEN secciones.nom_seccion IS NULL THEN 0 ELSE 1 IS END) as cantidad_secciones
FROM territorios 