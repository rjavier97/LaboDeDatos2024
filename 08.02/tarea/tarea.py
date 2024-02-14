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
   

print()
print("# ====================================================================")
print("# Ejercicios: A. Consultas sobre una tabla ")
print("# ====================================================================")

# ===============================  a   ========================================
consigna = """a. Listar sólo los nombres de todos los departamentos que hay en 
la tabla departamento (dejando los registros repetidos)"""
# =============================================================================
consultaSQL = sql^"""
                  SELECT descripcion
                  FROM departamento 
                  ORDER BY descripcion
                  """ 
print(consultaSQL)                  


# =============================   b   =========================================
consigna = """b. Listar sólo los nombres de todos los departamentos que 
hay en la tabla departamento (eliminando los registros repetidos)"""
# =============================================================================
consultaSQL = sql^"""
                  SELECT DISTINCT descripcion
                  FROM departamento 
                  ORDER BY descripcion
                  """ 
print(consultaSQL)          
  

# =============================   c   =========================================
consigna = """c. Listar sólo los códigos de departamento y sus nombres, de 
todos los departamentos que hay en la tabla departamento."""
# =============================================================================
consultaSQL = sql^"""
                  SELECT DISTINCT id, descripcion
                  FROM departamento 
                  ORDER BY id
                  """ 
print(consultaSQL)   



# =============================   d   =========================================
consigna = """d. Listar todas las columnas de la tabla departamento."""
# =============================================================================
consultaSQL = sql^"""
                  SELECT *
                  FROM departamento 
                  ORDER BY id
                  """ 
print(consultaSQL) 


# =============================   e   =========================================
consigna = """e. Listar los códigos de departamento y nombres de todos los 
departamentos que hay en la tabla departamento. Utilizar los siguientes alias 
para las columnas: codigo_depto y nombre_depto, respectivamente"""
# =============================================================================
consultaSQL = sql^"""
                  SELECT id AS codigo_depto, descripcion AS nombre_depto
                  FROM departamento 
                  ORDER BY id
                  """ 
print(consultaSQL) 


# =============================   f   =========================================
consigna = """f. Listar los registros de la tabla departamento 
cuyo código de provincia es igual a 54 """
# =============================================================================
consultaSQL = sql^"""
                  SELECT DISTINCT *
                  FROM departamento 
                  WHERE id_provincia=54
                  ORDER BY descripcion
                  """ 
print(consultaSQL) 


# =============================   g   =========================================
consigna = """g. Listar los registros de la tabla departamento 
cuyo código de provincia es igual a 22, 78 u 86. """
# =============================================================================
consultaSQL = sql^"""
                  SELECT DISTINCT *
                  FROM departamento 
                  WHERE id_provincia=22 OR id_provincia=78 OR id_provincia=86
                  ORDER BY id_provincia, descripcion
                  """ 
print(consultaSQL) 


# =============================   h   =========================================
consigna = """h. Listar los registros de la tabla departamento cuyos códigos 
de provincia se encuentren entre el 50 y el 59 (ambos valores inclusive). """
# =============================================================================
consultaSQL = sql^"""
                  SELECT DISTINCT *
                  FROM departamento 
                  WHERE id_provincia>=50 AND id_provincia<60
                  ORDER BY id_provincia, descripcion
                  """ 
print(consultaSQL) 



print()
print("# ====================================================================")
print("# Ejercicios: B. Consultas multitabla (INNER JOIN) ")
print("# ====================================================================")

# ===============================  a   ========================================
consigna = """a. Devolver una lista con los código y nombres de departamentos, 
asociados al nombre de la provincia al que pertenecen."""
# =============================================================================
consultaSQL = sql^"""
                  SELECT DISTINCT dep.id, dep.descripcion, prov.descripcion
                  FROM departamento AS dep
                  INNER JOIN provincia AS prov
                  ON dep.id_provincia = prov.id
                  ORDER BY prov.descripcion, dep.descripcion
                  """ 
print(consultaSQL)   


# ===============================  c   ========================================
consigna = """c. Devolver los casos registrados en la provincia de 'Chaco' """
# =============================================================================
consultaSQL = sql^"""
                  SELECT DISTINCT casos.* 
                  FROM casos
                  INNER JOIN departamento as dep
                  ON casos.id_depto = dep.id
                  INNER JOIN provincia as prov
                  ON prov.id = dep.id_provincia AND prov.descripcion = 'Chaco'
                  ORDER BY casos.anio             
                  """ 
print(consultaSQL)   


# ===============================  d   ========================================
consigna = """d. Devolver aquellos casos de la provincia de “Buenos Aires” 
cuyo campo cantidad supere los 10 casos. """
# =============================================================================
consultaSQL = sql^"""
        SELECT DISTINCT casos.*          
        FROM casos
        INNER JOIN departamento as dep
        ON casos.id_depto = dep.id
        INNER JOIN provincia as prov
        ON prov.id = dep.id_provincia AND prov.descripcion = 'Buenos Aires'
        WHERE casos.cantidad>10
        ORDER BY casos.cantidad
         """ 
print(consultaSQL)   



print()
print("# ====================================================================")
print("# Ejercicios: C. Consultas multitabla (OUTER JOIN) ")
print("# ====================================================================")

# ===============================  a   ========================================
consigna = """a. Devolver un listado con los nombres de los departamentos 
que no tienen ningún caso asociado."""
# =============================================================================
consultaSQL = sql^"""
                  SELECT DISTINCT dep1.descripcion 
                  FROM departamento AS dep1 
                  ORDER BY dep1.descripcion
                  """
                  
consultaSQL1 = sql^"""
                   SELECT DISTINCT dep2.descripcion
                   FROM departamento AS dep2
                   INNER JOIN casos 
                   ON casos.id_depto = dep2.id
                   ORDER BY dep2.descripcion
                   """
                  
consultaSQL2 = sql^"""
                  SELECT *
                  FROM consultaSQL
                  EXCEPT 
                  SELECT * 
                  FROM consultaSQL1
                  """
                  
consultaSQL3 = sql^"""
                   SELECT DISTINCT dep.descripcion, id_depto
                   FROM departamento as dep
                   LEFT OUTER JOIN casos 
                   ON dep.id = casos.id_depto
                   WHERE casos.id_depto IS NULL
                   
                   """                  
                                    
                  
   # en este caso, se puede sacar el DISTINCT, y trae el mismo resultado  
print("\n", consultaSQL)
print("\n", consultaSQL1)
print("\n", consultaSQL2)  
print("\n", consultaSQL3)  


# ===============================  b   ========================================
consigna = """b. Devolver un listado con los tipos de evento que no 
tienen ningún caso asociado. """
# =============================================================================
consultaSQL = sql^"""
                  SELECT tipoevento.descripcion as Eventos_SinCasos
                  FROM tipoevento 
                  LEFT OUTER JOIN casos
                  ON tipoevento.id = casos.id_tipoevento
                  WHERE casos.id_tipoevento IS NULL                          
                  """ 
print("\n", consultaSQL)   



print()
print("# ====================================================================")
print("# Ejercicios: D. Consultas resumen ")
print("# ====================================================================")

# ===============================  a   ========================================
consigna = """a. Calcular la cantidad total de casos que hay 
en la tabla casos."""
# =============================================================================
consultaSQL = sql^"""
                  SELECT SUM(
                    CASE WHEN cantidad IS NULL THEN 0
                    ELSE cantidad END) as Cantidad_Total_De_Casos
                  FROM casos
                  """ 

consultaSQL1 = sql^"""
                   SELECT SUM(cantidad) as Cantidad_Total_Casos    
                   FROM casos 
                   """
                   
print("\n", consultaSQL)      # Ambos casos dan el mismo resultado: 61444
print("\n", consultaSQL1)


# ===============================  b   ========================================
consigna = """b. Calcular la cantidad total de casos que hay en la tabla casos
para cada año y cada tipo de caso. 
Presentar la información de la siguiente manera:
descripción del tipo de caso, año y cantidad. Ordenarlo por tipo de caso
(ascendente) y año (ascendente)."""
# =============================================================================
consultaSQL = sql^"""
SELECT tipoevento.descripcion,casos.anio,SUM(casos.cantidad) AS Cantidad_casos 
FROM tipoevento 
INNER JOIN casos
ON tipoevento.id = casos.id_tipoevento
GROUP BY tipoevento.descripcion, anio
ORDER BY tipoevento.descripcion ASC, anio DESC
""" 
print("\n", consultaSQL)   


# ===============================  c   ========================================
consigna = """c. Misma consulta que el ítem anterior, 
pero sólo para el año 2019. """
# =============================================================================
consultaSQL = sql^"""
SELECT tipoevento.descripcion,casos.anio,SUM(casos.cantidad) AS Cantidad_casos 
FROM tipoevento 
INNER JOIN casos
ON tipoevento.id = casos.id_tipoevento AND casos.anio = 2019
GROUP BY tipoevento.descripcion, anio
ORDER BY tipoevento.descripcion ASC, anio DESC
""" 
print("\n", consultaSQL)   


# ===============================  d   ========================================
consigna = """d. Calcular la cantidad total de departamentos que hay 
por provincia. Presentar la información ordenada por código de provincia."""
# =============================================================================
consultaSQL = sql^"""
SELECT prov.id, prov.descripcion, COUNT(*) AS Cantidad_deptos
FROM provincia AS prov 
INNER JOIN departamento AS dep
ON prov.id = dep.id_provincia
GROUP BY prov.id , prov.descripcion
ORDER BY prov.id 
""" 
print("\n", consultaSQL)   

# print(sql^"""
#             SELECT SUM(Cantidad_deptos) 
#             from consultaSQL               #Se comprueba que esta bien
#             """)                           # Tiene que dar 333 en total
                          # ya que son 333 los deptos que hay en total
# ===============================  e   ========================================
consigna = """e. Listar los departamentos con menos cantidad de 
casos en el año 2019. """
# =============================================================================
consultaSQL = sql^"""
SELECT dep.descripcion, casos.anio, SUM(casos.cantidad) as Cantidad_casos
FROM departamento as dep
INNER JOIN casos 
ON dep.id = casos.id_depto
GROUP BY dep.descripcion, casos.anio
HAVING casos.anio=2019
ORDER BY Cantidad_casos ASC LIMIT 20
""" 
print("\n", consultaSQL)


# ===============================  f   ========================================
consigna = """f. Listar los departamentos con más cantidad de casos 
en el año 2020. """
# =============================================================================
consultaSQL = sql^"""
SELECT dep.descripcion, casos.anio, SUM(casos.cantidad) as Cantidad_casos
FROM departamento as dep
INNER JOIN casos 
ON dep.id = casos.id_depto
GROUP BY dep.descripcion, casos.anio
HAVING casos.anio=2019
ORDER BY Cantidad_casos DESC LIMIT 20
""" 
print("\n", consultaSQL)   


# ===============================  g   ========================================
consigna = """g. Listar el promedio de cantidad de casos por provincia y año.
"""
# =============================================================================
consultaSQL = sql^"""
SELECT prov.descripcion, casos.anio, 
SUM(casos.cantidad) AS suma_casos, 
COUNT(casos.cantidad) AS cantidad_casos,
AVG(casos.cantidad) AS promedio_casos
FROM casos
INNER JOIN departamento AS dep
ON casos.id_depto = dep.id
INNER JOIN provincia as prov
ON dep.id_provincia = prov.id
GROUP BY prov.descripcion, casos.anio
ORDER BY prov.descripcion
""" 
print("\n", consultaSQL)   


# ===============================  h   ========================================
consigna = """h. Listar, para cada provincia y año, cuáles fueron los 
departamentos que más cantidad de casos tuvieron. """
# =============================================================================
deptoCasosMax = sql^"""
SELECT prov.descripcion AS provincia,
casos.anio,
dep.descripcion AS depto,
SUM(casos.cantidad) as SumaCasos
FROM casos
INNER JOIN departamento AS dep
ON casos.id_depto = dep.id
INNER JOIN provincia as prov
ON dep.id_provincia = prov.id
GROUP BY provincia, anio, depto
ORDER BY provincia, anio DESC, SumaCasos DESC             
"""

consultaSQL2 = sql^"""
SELECT DISTINCT e.*
FROM deptoCasosMax AS e
INNER JOIN consultaSQL1 AS i
ON e.provincia = i.provincia AND e.anio = i.anio AND e.SumaCasos = i.SumaCasos
ORDER BY e.provincia, e.anio DESC
"""
# la tabla consultaSQL2 trae mas de un depto en caso de empate. 


print("\n", consultaSQL2)   


# ===============================  i   ========================================
consigna = """i. Mostrar la cantidad de casos total, máxima, mínima y 
promedio que tuvo la provincia de Buenos Aires en el año 2019. """
# =============================================================================
consultaSQL = sql^"""
SELECT SUM(casos.cantidad) AS CasosTotal, 
MAX(casos.cantidad) AS CasosMax,
MIN(casos.cantidad) AS CasosMin, 
AVG(casos.cantidad) AS PromedioCasos
FROM casos
INNER JOIN departamento AS dep
ON casos.id_depto = dep.id
INNER JOIN provincia AS prov
ON dep.id_provincia = prov.id AND prov.descripcion = 'Buenos Aires'
WHERE anio=2019

                  """ 
print("\n", consultaSQL)   


# ===============================  j   ========================================
consigna = """j. Misma consulta que el ítem anterior, pero sólo para aquellos 
casos en que la cantidad total es mayor a 1000 casos """
# =============================================================================
consultaSQL = sql^"""
                  SELECT descripcion
                  FROM departamento 
                  ORDER BY descripcion
                  """ 
print("\n", consultaSQL)   


# ===============================  k   ========================================
consigna = """k. Listar los nombres de departamento (y nombre de provincia)
que tienen mediciones tanto para el año 2019 como para el año 2020. 
Para cada uno de ellos devolver la cantidad de casos promedio. 
Ordenar por nombre de provincia (ascendente) y 
luego por nombre de departamento (ascendente). """
# =============================================================================
consultaSQL = sql^"""
                  SELECT prov.descripcion, dep.descripcion, 
                  FROM departamento 
                  ORDER BY descripcion
                  """ 
print("\n", consultaSQL)   


# ===============================  L  ========================================
consigna = """l. Devolver una tabla que tenga los siguientes campos: 
descripción de tipo de evento, id_depto, nombre de departamento, id_provincia,
nombre de provincia, total de casos 2019, total de casos 2020. """
# =============================================================================
totalCasos2019 = sql^"""
SELECT 
te.descripcion AS nombreCaso,
casos.id_depto,
dep.descripcion AS depto,
dep.id_provincia ,
prov.descripcion AS territorio,
SUM(casos.cantidad) AS TotalCasos2019,
casos.anio AS anio
FROM casos
INNER JOIN departamento AS dep
ON casos.id_depto = dep.id
INNER JOIN provincia AS prov
ON dep.id_provincia = prov.id
INNER JOIN tipoevento AS te
ON casos.id_tipoevento = te.id
WHERE anio = 2019
GROUP BY casos.id_depto, depto, nombreCaso, territorio, dep.id_provincia, anio
ORDER BY territorio
""" 
totalCasos2020 = sql^"""
SELECT 
te.descripcion AS nombreCaso,
casos.id_depto,
dep.descripcion AS depto,
dep.id_provincia ,
prov.descripcion AS territorio,
SUM(casos.cantidad) AS TotalCasos2020,
casos.anio AS anio
FROM casos
INNER JOIN departamento AS dep
ON casos.id_depto = dep.id
INNER JOIN provincia AS prov
ON dep.id_provincia = prov.id
INNER JOIN tipoevento AS te
ON casos.id_tipoevento = te.id
WHERE anio = 2020
GROUP BY casos.id_depto, depto, nombreCaso, territorio, dep.id_provincia, anio
ORDER BY territorio
"""

tabla2019y2020 = sql^"""
SELECT DISTINCT tc2019.nombreCaso, tc2019.id_depto, tc2019.depto, 
tc2019.id_provincia, tc2019.territorio, tc2019.TotalCasos2019, 
tc2020.TotalCasos2020
FROM totalCasos2019 AS tc2019
FULL OUTER JOIN totalCasos2020 AS tc2020
ON tc2019.nombreCaso = tc2020.nombreCaso 
AND tc2019.id_depto = tc2020.id_depto
AND tc2019.depto = tc2020.depto
AND tc2019.id_provincia = tc2020.id_provincia
AND tc2019.territorio = tc2020.territorio
ORDER BY tc2019.territorio, tc2019.depto
"""

# no es el resultado esperado

print("\n", consultaSQL)   



print()
print("# ====================================================================")
print("# Ejercicios: E. Subconsultas (ALL, ANY) ")
print("# ====================================================================")

# ===============================  a   ========================================
consigna = """a. Devolver el departamento que tuvo la mayor cantidad de casos 
sin hacer uso de MAX, ORDER BY ni LIMIT.
"""
# =============================================================================
deptoCasos = sql^"""
SELECT dep.descripcion, SUM(casos.cantidad) AS mayorCantidad
FROM casos
INNER JOIN departamento as dep
ON casos.id_depto = dep.id
GROUP BY dep.descripcion
""" 

resultadoConsultaSQL = sql^"""
SELECT *
FROM deptoCasos
WHERE mayorCantidad >= ALL (
    SELECT deptoCasos1.mayorCantidad
    FROM deptoCasos as deptoCasos1 )
"""

print("\n", resultadoConsultaSQL)   


# ===============================  b   ========================================
consigna = """b. Devolver los tipo de evento que tienen casos asociados. 
(Utilizando ALL o ANY). """
# =============================================================================
consultaSQL = sql^"""
SELECT DISTINCT te.descripcion
FROM tipoevento as te
INNER JOIN casos 
ON te.id = casos.id_tipoevento
WHERE te.descripcion = ALL (
    SELECT te1.descripcion 
    FROM tipoevento AS te1 
    WHERE te1.id = te.id)
ORDER BY te.descripcion
""" 
print("\n", consultaSQL)   



print()
print("# ====================================================================")
print("# Ejercicios: F. Subconsultas (IN, NOT IN) ")
print("# ====================================================================")

# ===============================  a   ========================================
consigna = """a. Devolver los tipo de evento que tienen casos asociados 
(Utilizando IN, NOT IN). """
# =============================================================================
consultaSQL = sql^"""
                  SELECT DISTINCT te.descripcion
                  FROM tipoevento as te 
                  WHERE te.id IN (
                      SELECT DISTINCT casos1.id_tipoevento
                      FROM casos AS casos1 
                      )
                  ORDER BY descripcion
                  """ 
print("\n", consultaSQL)   


# ===============================  b   ========================================
consigna = """b. Devolver los tipo de evento que NO tienen casos asociados
 (Utilizando IN, NOT IN). """
# =============================================================================
consultaSQL = sql^"""
              SELECT DISTINCT te.descripcion
              FROM tipoevento as te 
              WHERE te.id NOT IN (
                  SELECT DISTINCT casos1.id_tipoevento
                  FROM casos AS casos1
                  )
              ORDER BY te.descripcion
                  """ 
print("\n", consultaSQL)   



print()
print("# ====================================================================")
print("# Ejercicios: G. Subconsultas (EXISTS, NOT EXISTS) ")
print("# ====================================================================")

# ===============================  a   ========================================
consigna = """a. Devolver los tipo de evento que tienen casos asociados
 (Utilizando EXISTS, NOT EXISTS). """
# =============================================================================
consultaSQL = sql^"""
                  SELECT DISTINCT te.descripcion
                  FROM tipoevento AS te 
                  WHERE EXISTS (
                      SELECT casos.id_tipoevento
                      FROM casos
                      WHERE casos.id_tipoevento=te.id)
                  ORDER BY te.descripcion
                  """ 
print("\n", consultaSQL)   


# ===============================  b   ========================================
consigna = """b. Devolver los tipo de evento que NO tienen casos asociados
 (Utilizando IN, NOT IN). """
# =============================================================================
consultaSQL = sql^"""
    SELECT DISTINCT te.descripcion
    FROM tipoevento AS te 
    WHERE NOT EXISTS (
        SELECT casos.id_tipoevento
        FROM casos
        WHERE casos.id_tipoevento=te.id)
    ORDER BY te.descripcion
                  """ 
print("\n", consultaSQL)   



print()
print("# ====================================================================")
print("# Ejercicios: H. Subconsultas correlacionadas ")
print("# ====================================================================")

# ===============================  a   ========================================
consigna = """a. Listar las provincias que tienen una cantidad total de casos 
mayor al promedio de casos del país. Hacer el listado agrupado por año. """
# =============================================================================
consultaSQL = sql^"""
                  SELECT 
                  FROM 
                  ORDER BY 
                  """ 
print("\n", consultaSQL)   


# ===============================  b   ========================================
consigna = """b. Por cada año, listar las provincias que tuvieron una cantidad
total de casos mayor a la cantidad total de casos que 
la provincia de Corrientes. """
# =============================================================================
consultaSQL = sql^"""
                  SELECT
                  FROM 
                  ORDER BY
                  """ 
print("\n", consultaSQL)   



print()
print("# ====================================================================")
print("# Ejercicios: I: Más consultas sobre una tabla ")
print("# ====================================================================")

# ===============================  a   ========================================
consigna = """a. Listar los códigos de departamento y sus nombres, ordenados 
por estos últimos (sus nombres) de manera descendentes (de la Z a la A). 
En caso de empate, desempatar por código de departamento de manera ascendente.
 """
# =============================================================================
consultaSQL = sql^"""
                  SELECT DISTINCT id, descripcion 
                  FROM departamento 
                  ORDER BY descripcion DESC, id ASC
                  """ 
print("\n", consultaSQL)   


# ===============================  b   ========================================
consigna = """b. Listar los registros de la tabla provincia cuyos nombres 
comiencen con la letra M. """
# =============================================================================
consultaSQL = sql^"""
                  SELECT *
                  FROM provincia 
                  WHERE descripcion LIKE 'M%'
                  ORDER BY descripcion
                  """ 
print("\n", consultaSQL)   


# ===============================  c   ========================================
consigna = """c. Listar los registros de la tabla provincia cuyos nombres 
comiencen con la letra S y su quinta letra sea una letra A. """
# =============================================================================
consultaSQL = sql^"""
                  SELECT *
                  FROM provincia 
                  WHERE descripcion LIKE 'S___a%'
                  """ 
print("\n", consultaSQL)   


# ===============================  d   ========================================
consigna = """d. Listar los registros de la tabla provincia cuyos nombres 
terminan con la letra A."""
# =============================================================================
consultaSQL = sql^"""
                  SELECT *
                  FROM provincia
                  WHERE descripcion LIKE '%a'
                  ORDER BY descripcion
                  """ 
print("\n", consultaSQL)   


# ===============================  e   ========================================
consigna = """e. Listar los registros de la tabla provincia cuyos nombres 
tengan exactamente 5 letras. """
# =============================================================================
consultaSQL = sql^"""
                  SELECT *
                  FROM provincia
                  WHERE descripcion LIKE '_____'
                  ORDER BY descripcion
                  """ 
print("\n", consultaSQL)   


# ===============================  f   ========================================
consigna = """f. Listar los registros de la tabla provincia cuyos nombres 
tengan ”do” en alguna parte de su nombre."""
# =============================================================================
consultaSQL = sql^"""
                  SELECT *
                  FROM provincia
                  WHERE descripcion LIKE '%do%'
                  ORDER BY descripcion
                  """ 
print("\n", consultaSQL)   


# ===============================  g   ========================================
consigna = """g. Listar los registros de la tabla provincia cuyos nombres
 tengan ”do” en alguna parte de su nombre y su código sea menor a 30. """
# =============================================================================
consultaSQL = sql^"""
                  SELECT *
                  FROM provincia
                  WHERE descripcion LIKE '%do%' AND id<30
                  ORDER BY descripcion
                  """ 
print("\n", consultaSQL)   


# ===============================  h   ========================================
consigna = """h. Listar los registros de la tabla departamento cuyos nombres 
tengan ”san” en alguna parte de su nombre. Listar sólo id y descripcion. 
Utilizar los siguientes alias para las columnas: codigo_depto y nombre_depto,
respectivamente. El resultado debe estar ordenado por sus nombres de
manera descendentes (de la Z a la A). """
# =============================================================================
consultaSQL = sql^"""
                  SELECT DISTINCT id AS codigo_depto, 
                  LOWER(descripcion) AS nombre_depto
                  FROM departamento 
                  WHERE nombre_depto LIKE '%san%' 
                  ORDER BY nombre_depto DESC
                  """ 
print("\n", consultaSQL)   


# ===============================  i   ========================================
consigna = """i. Devolver aquellos casos de las provincias cuyo nombre terminen 
con la letra a y el campo cantidad supere 10. Mostrar: nombre de provincia, 
nombre de departamento, año, semana epidemiológica, descripción de grupo etario
y cantidad. Ordenar el resultado por la cantidad (descendente), luego por el
nombre de la provincia (ascendente), nombre del departamento
(ascendente), año (ascendente) y la descripción del grupo etario
(ascendente). """
# =============================================================================
consultaSQL = sql^"""
    SELECT prov.descripcion, dep.descripcion, casos.anio,
    casos.semana_epidemiologica, ge.descripcion,
    casos.cantidad 
    FROM casos 
    INNER JOIN departamento AS dep
    ON casos.id_depto = dep.id
    INNER JOIN provincia AS prov
    ON dep.id_provincia = prov.id
    INNER JOIN grupoetario AS ge
    ON casos.id_grupoetario = ge.id 
    WHERE (prov.descripcion LIKE '%a') AND casos.cantidad>10
    ORDER BY casos.cantidad DESC, prov.descripcion ASC, dep.descripcion ASC,
    casos.anio ASC, ge.descripcion ASC                  
""" 
print("\n", consultaSQL)   


# ===============================  j   ========================================
consigna = """j. Ídem anterior, pero devolver sólo aquellas tuplas que tienen
 el máximo en el campo cantidad. """
# =============================================================================
consultaSQL = sql^"""
                  SELECT prov.descripcion, dep.descripcion, 
                  FROM departamento 
                  ORDER BY descripcion
                  """ 
print("\n", consultaSQL)   

# El maximo de que? o con respecto a que ?

print()
print("# ====================================================================")
print("# Ejercicios: J: Reemplazos ")
print("# ====================================================================")

# ===============================  a   ========================================
consigna = """a. Listar los id y descripción de los departamentos.
Estos últimos sin tildes y en orden alfabético """
# =============================================================================
consultaSQL = sql^"""
SELECT id, 
REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(descripcion,'á','a'),'é','e'),'í','i'),'ó','o'),'ú','u') as Nombre_dpto
FROM departamento 
ORDER BY descripcion 
""" 
print("\n", consultaSQL)   


# ===============================  b   ========================================
consigna = """b. Listar los nombres de provincia en mayúscula, sin tildes 
y en orden alfabético """
# =============================================================================
consultaSQL = sql^"""
SELECT 
REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(descripcion,'á','a'),'é','e'),'í','i'),'ó','o'),'ú','u') as Provincia
FROM provincia
ORDER BY provincia
""" 
print("\n", consultaSQL)   





