# -*- coding: utf-8 -*-
"""
Materia: Laboratorio de datos - FCEyN - UBA
Clase  : Clase SQL. Script clase.
Autor  : Pablo Turjanski
Fecha  : 2023-03-07
"""

# Importamos bibliotecas
import pandas as pd
import csv
from inline_sql import sql, sql_val

def main():

    print()
    print("# =============================================================================")
    print("# Creamos/Importamos los datasets que vamos a utilizar en este programa")
    print("# =============================================================================")

    carpeta = ""
    
    # Ejercicios AR-PROJECT, SELECT, RENAME
    empleado       = get_empleado()
    # Ejercicios AR-UNION, INTERSECTION, MINUS
    alumnosBD      = get_alumnosBD()
    alumnosTLeng   = get_alumnosTLeng()
    # Ejercicios AR-CROSSJOIN
    persona        = get_persona_ejemploCrossJoin()
    nacionalidades = get_nacionalidades()
    # Ejercicios ¿Mismos Nombres?
    se_inscribe_en=get_se_inscribe_en_ejemploMismosNombres()
    materia       =get_materia_ejemploMismosNombres()
    # Ejercicio JOIN múltiples tablas
    vuelo      = pd.read_csv(carpeta+"vuelo.csv")    
    aeropuerto = pd.read_csv(carpeta+"aeropuerto.csv")    
    pasajero   = pd.read_csv(carpeta+"pasajero.csv")    
    reserva    = pd.read_csv(carpeta+"reserva.csv")    
    # Ejercicio JOIN tuplas espúreas
    empleadoRol= pd.read_csv(carpeta+"empleadoRol.csv")    
    rolProyecto= pd.read_csv(carpeta+"rolProyecto.csv")    
    # Ejercicios funciones de agregación, LIKE, Elección, Subqueries y variables de Python
    examen     = pd.read_csv(carpeta+"examen.csv")
    # Ejercicios de manejo de valores NULL
    examen03 = pd.read_csv(carpeta+"examen03.csv")
    
    
    print()
    print("# =============================================================================")
    print("# Ejemplo inicial")
    print("# =============================================================================")
    
    print(empleado)

    consultaSQL = """
                   SELECT DISTINCT DNI, Salario
                   FROM empleado;
                  """


    dataframeResultado = sql^ consultaSQL
    
    print(dataframeResultado)


    print()
    print("# =============================================================================")
    print("# Ejercicios AR-PROJECT <-> SELECT")
    print("# =============================================================================")
    
    consigna    = "a.- Listar DNI y Salario de empleados "
    consultaSQL = """
                   SELECT DISTINCT DNI, Salario
                   FROM empleado;
                  """
    imprimirEjercicio(consigna, [empleado], consultaSQL, sql^consultaSQL)    
    
    # -----------
    consigna    = "b.- Listar Sexo de empleados "
    consultaSQL = """
                   SELECT DISTINCT Sexo
                   FROM empleado
                  """
    imprimirEjercicio(consigna, [empleado], consultaSQL, sql^consultaSQL)    

    # -----------
    consigna    = "c.- Listar Sexo de empleados (sin DISTINCT)"
    consultaSQL = """
                   SELECT Sexo
                   FROM empleado
                  """
    imprimirEjercicio(consigna, [empleado], consultaSQL, sql^consultaSQL)    

    print()
    print("# =============================================================================")
    print("# Ejercicios AR-SELECT <-> WHERE")
    print("# =============================================================================")
    
    consigna    = "a.- Listar de EMPLEADO sólo aquellos cuyo sexo es femenino"
    consultaSQL = """
                   SELECT * 
                   FROM empleado
                   WHERE Sexo='F'
                  """
    imprimirEjercicio(consigna, [empleado], consultaSQL, sql^consultaSQL)    

    # -----------
    consigna    = "b.- Listar de EMPLEADO aquellos cuyo sexo es femenino y su salario es mayor a $15.000"
    consultaSQL = """
                   SELECT *
                   FROM empleado
                   WHERE Sexo='F' and Salario>15000
                  """
    imprimirEjercicio(consigna, [empleado], consultaSQL, sql^consultaSQL)    
    
    print()
    print("# =============================================================================")
    print("# Ejercicios AR-RENAME <-> AS")
    print("# =============================================================================")
    
    consigna    = """a.- Listar DNI y Salario de EMPLEADO, y renombrarlos como id e Ingreso"""
    consultaSQL = """
                   SELECT DNI as ID, Salario as Ingreso
                   FROM empleado
                  """
    
    imprimirEjercicio(consigna, [empleado], consultaSQL, sql^consultaSQL)    
 
    
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
     # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
     # #                                                                     # #
    # #    INICIO -->           EJERCICIO Nro. 01                             # #
     # #                                                                     # # 
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
     # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    
    # IMPORTANTE: Recordar que se utilizaran los datos de vuelo, aeropuerto, pasajero y reserva

    print()
    print("# =============================================================================")
    print("# EJERCICIOS PARA REALIZAR DE MANERA INDIVUDUAL --> EJERCICIO Nro. 01")
    print("# =============================================================================")

    
    consigna    = "Ejercicio 01.1.- Retornar Codigo y Nombre de los aeropuertos de Londres"
    consultaSQL = """
                   SELECT Codigo, Nombre
                   FROM aeropuerto
                   WHERE Ciudad = 'Londres'
                  """
    imprimirEjercicio(consigna, [vuelo, aeropuerto, pasajero, reserva], consultaSQL, sql^consultaSQL)    

    # -----------
    consigna    = "Ejercicio 01.2.- ¿Qué retorna \n     SELECT DISTINCT Ciudad AS City \n     FROM aeropuerto \n     WHERE Codigo='ORY' OR Codigo='CDG'; ?"
    consultaSQL = """
                   SELECT DISTINCT Ciudad AS City 
                   FROM aeropuerto
                   WHERE Codigo='ORY' OR Codigo='CDG'
                  """
    imprimirEjercicio(consigna, [vuelo, aeropuerto, pasajero, reserva], consultaSQL, sql^consultaSQL)    
    # Retorna Paris
    
    # -----------
    consigna    = "Ejercicio 01.3.- Obtener los números de vuelo que van desde CDG hacia LHR"
    consultaSQL = """
                   SELECT Numero 
                   FROM vuelo
                   WHERE Origen='CDG' and Destino='LHR'
                  """
    imprimirEjercicio(consigna, [vuelo, aeropuerto, pasajero, reserva], consultaSQL, sql^consultaSQL)    

    # -----------
    consigna    = "Ejercicio 01.4.- Obtener los números de vuelo que van desde CDG hacia LHR o viceversa"
    
    consultaSQL = """
                   SELECT DISTINCT Numero 
                   FROM vuelo
                   WHERE (Origen='LHR' AND Destino='CDG') OR (Origen='CDG' AND Destino='LHR')
                  """

    imprimirEjercicio(consigna, [vuelo, aeropuerto, pasajero, reserva], consultaSQL, sql^consultaSQL)    

    # -----------
    consigna    = "Ejercicio 01.5.- Devolver las fechas de reservas cuyos precios son mayores a $200"
    consultaSQL = """
                  SELECT Fecha
                  FROM reserva
                  WHERE Precio>200
                  """
    imprimirEjercicio(consigna, [vuelo, aeropuerto, pasajero, reserva], consultaSQL, sql^consultaSQL)    

    
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
     # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
     # #                                                                     # #
    # #    FIN -->              EJERCICIO Nro. 01                             # #
     # #                                                                     # # 
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
     # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    
    
    print()
    print("# =============================================================================")
    print("# Ejercicios AR-UNION, INTERSECTION, MINUS <-> UNION, INTERSECTION, EXCEPT")
    print("# =============================================================================")

    consigna    = """a1.- Listar a los alumnos que cursan BDs o TLENG"""
    
    consultaSQL = """
                   SELECT *
                   from alumnosBD
                   UNION
                   SELECT *
                   from alumnosTLeng
                   ORDER BY ID 
                  """

    imprimirEjercicio(consigna, [alumnosBD, alumnosTLeng], consultaSQL, sql^consultaSQL)    


    # -----------
    consigna    = """a2.- Listar a los alumnos que cursan BDs o TLENG (usando UNION ALL)"""
    
    consultaSQL = """
                   SELECT *
                   from alumnosBD
                   UNION ALL
                   SELECT *
                   from alumnosTLeng
                   ORDER BY ID 
                  """

    imprimirEjercicio(consigna, [alumnosBD, alumnosTLeng], consultaSQL, sql^consultaSQL)    


    # -----------
    consigna    = """b.- Listar a los alumnos que cursan simultáneamente BDs y TLENG"""
    
    consultaSQL = """
                  SELECT bd.ID, bd.Nombre
                  from alumnosBD as bd
                  INNER JOIN alumnosTLeng as tl
                  ON bd.ID = tl.ID
                  """
                   # SELECT *
                   # from alumnosBD
                   # INTERSECT
                   # SELECT *
                   # from alumnosTLeng
                   # Esta es otra opcion que tambien funciona

    imprimirEjercicio(consigna, [alumnosBD, alumnosTLeng], consultaSQL, sql^consultaSQL)    

    
    # -----------
    consigna    = """c.- Listar a los alumnos que cursan BDs y no cursan TLENG """
    
    consultaSQL = """
                   SELECT *
                   from alumnosBD
                   EXCEPT
                   SELECT *
                   from alumnosTLeng
                  """

    imprimirEjercicio(consigna, [alumnosBD, alumnosTLeng], consultaSQL, sql^consultaSQL)    


    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
     # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
     # #                                                                     # #
    # #    INICIO -->           EJERCICIO Nro. 02                             # #
     # #                                                                     # # 
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
     # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    
    # IMPORTANTE: Recordar que se utilizaran los datos de vuelo, aeropuerto, pasajero y reserva

    print()
    print("# =============================================================================")
    print("# EJERCICIOS PARA REALIZAR DE MANERA INDIVUDUAL --> EJERCICIO Nro. 02")
    print("# =============================================================================")

    
    consigna    = "Ejercicio 02.1.- Devolver los números de vuelo que tienen reservas generadas (utilizar intersección)"
    consultaSQL = """
                   SELECT vuelo.Numero
                   from vuelo 
                   INTERSECT
                   SELECT reserva.NroVuelo 
                   from reserva            
                  """
    imprimirEjercicio(consigna, [vuelo, aeropuerto, pasajero, reserva], consultaSQL, sql^consultaSQL)    

    # -----------
    consigna    = "Ejercicio 02.2.- Devolver los números de vuelo que aún no tienen reservas"
    consultaSQL = """
                   SELECT vuelo.Numero
                   from vuelo 
                   EXCEPT
                   SELECT reserva.NroVuelo 
                   from reserva           
                  """
    imprimirEjercicio(consigna, [vuelo, aeropuerto, pasajero, reserva], consultaSQL, sql^consultaSQL)    

    # -----------
    consigna    = "Ejercicio 02.3.- Retornar los códigos de aeropuerto de los que parten o arriban los vuelos"
    consultaSQL = """
                    SELECT Codigo 
                    from aeropuerto 
                    INTERSECT
                   (SELECT Origen 
                   FROM vuelo 
                   UNION 
                   SELECT Destino
                   FROM vuelo)
                  """
                  
    imprimirEjercicio(consigna, [vuelo, aeropuerto, pasajero, reserva], consultaSQL, sql^consultaSQL)    



    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
     # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
     # #                                                                     # #
    # #    FIN -->              EJERCICIO Nro. 02                             # #
     # #                                                                     # # 
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
     # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

   
    
    print("# =============================================================================")
    print("# Ejercicios AR-... JOIN <-> ... JOIN")
    print("# =============================================================================")

    consigna    = """a1.- Listar el producto cartesiano entre las tablas persona y nacionalidades"""
    
    consultaSQL = """
                   SELECT *
                   FROM persona
                   CROSS JOIN nacionalidades
                   ORDER BY Nombre
                  """
                  # SELECT *
                  # from persona, nacionalidades
                  # ORDER BY Nombre 
                  # Esta es otra opcion que tambien funciona

    imprimirEjercicio(consigna, [persona, nacionalidades], consultaSQL, sql^consultaSQL)


    # -----------
    consigna    = """a2.- Listar el producto cartesiano entre las tablas persona y nacionalidades (sin usar CROSS JOIN)"""
    
    consultaSQL = """
                    SELECT *
                    from persona, nacionalidades
                    ORDER BY Nombre
                  """

    imprimirEjercicio(consigna, [persona, nacionalidades], consultaSQL, sql^consultaSQL)


    # ---------------------------------------------------------------------------------------------- 
    # Carga los nuevos datos del dataframe persona para los ejercicios de AR-INNER y LEFT OUTER JOIN
    # ----------------------------------------------------------------------------------------------
    persona        = get_persona_ejemplosJoin()
    # ----------------------------------------------------------------------------------------------
    
    
    consigna    = """b1.- Vincular las tablas persona y nacionalidades a través de un INNER JOIN"""
    
    consultaSQL = """
                   SELECT persona.* , nac.Detalle 
                   from persona 
                   INNER JOIN nacionalidades as nac
                   ON Nacionalidad = IDN 
                   
                  """

    imprimirEjercicio(consigna, [persona, nacionalidades], consultaSQL, sql^consultaSQL)


    # -----------
    consigna    = """b2.- Vincular las tablas persona y nacionalidades (sin usar INNER JOIN)"""
    
    consultaSQL = """
                   SELECT *
                   FROM persona, nacionalidades
                   WHERE Nacionalidad = IDN
                  """

    imprimirEjercicio(consigna, [persona, nacionalidades], consultaSQL, sql^consultaSQL)


    # -----------
    consigna    = """c.- Vincular las tablas persona y nacionalidades a través de un LEFT OUTER JOIN"""
    
    consultaSQL = """
                   SELECT *
                   from persona
                   LEFT OUTER JOIN nacionalidades
                   ON Nacionalidad = IDN
                  """

    imprimirEjercicio(consigna, [persona, nacionalidades], consultaSQL, sql^consultaSQL)
    

    print("# =============================================================================")
    print("# Ejercicios SQL - ¿Mismos Nombres?")
    print("# =============================================================================")

    consigna    = """a.- Vincular las tablas Se_inscribe_en y Materia. Mostrar sólo LU y Nombre de materia"""
    
    consultaSQL = """
                   SELECT i.LU, m.Nombre
                   from se_inscribe_en as i
                   INNER JOIN materia as m 
                   ON i.Codigo_materia = m.Codigo_materia
                  """

    imprimirEjercicio(consigna, [persona, nacionalidades], consultaSQL, sql^consultaSQL)
    
    
    
    
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
     # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
     # #                                                                     # #
    # #    INICIO -->           EJERCICIO Nro. 03                             # #
     # #                                                                     # # 
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
     # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    
    # IMPORTANTE: Recordar que se utilizaran los datos de vuelo, aeropuerto, pasajero y reserva

    print()
    print("# =============================================================================")
    print("# EJERCICIOS PARA REALIZAR DE MANERA INDIVUDUAL --> EJERCICIO Nro. 03")
    print("# =============================================================================")
    
    consigna    = "Ejercicio 03.1.- Devolver el nombre de la ciudad de partida del vuelo número 165"

    consultaSQL = """
                    SELECT vu.Numero, ae.Ciudad
                    FROM aeropuerto AS ae
                    INNER JOIN vuelo AS vu
                    ON (ae.Codigo = vu.Origen) AND vu.Numero = 165
                  """

    imprimirEjercicio(consigna, [vuelo, aeropuerto, pasajero, reserva], consultaSQL, sql^consultaSQL)    

    # -----------
    consigna    = "Ejercicio 03.2.- Retornar el nombre de las personas que realizaron reservas a un valor menor a $200"

    consultaSQL = """
                    SELECT p.Nombre
                    FROM pasajero as p
                    INNER JOIN reserva as r
                    ON p.DNI = r.DNI AND r.PRECIO<200
                    
                  """

    imprimirEjercicio(consigna, [vuelo, aeropuerto, pasajero, reserva], consultaSQL, sql^consultaSQL)    

    # -----------
    consigna    = "Ejercicio 03.3.- Obtener Nombre, Fecha y Destino del Viaje de todos los pasajeros que vuelan desde Madrid"


    consultaSQL = """
                    SELECT p.Nombre, r.Fecha, a.Ciudad as Destino_Viaje
                    FROM pasajero as p
                    INNER JOIN reserva AS r ON p.DNI = r.DNI 
                    INNER JOIN vuelo AS v ON r.NroVuelo = v.Numero AND Origen='MAD'
                    INNER JOIN aeropuerto AS a ON v.Destino=a.Codigo 
                  """
    imprimirEjercicio(consigna, [vuelo, aeropuerto, pasajero, reserva], consultaSQL, sql^consultaSQL)    


    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
     # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
     # #                                                                     # #
    # #    FIN -->              EJERCICIO Nro. 03                             # #
     # #                                                                     # # 
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
     # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    
    
    print("# =============================================================================")
    print("# Ejercicios SQL - Join de varias tablas en simultáneo")
    print("# =============================================================================")

    consigna    = """a.- Vincular las tablas Reserva, Pasajero y Vuelo. Mostrar sólo Fecha de reserva, hora de salida del vuelo y nombre de pasajero."""
    
    consultaSQL = """
                   SELECT r.Fecha, v.Salida, p.Nombre 
                   FROM pasajero AS p
                   INNER JOIN reserva AS r ON p.DNI = r.DNI 
                   INNER JOIN vuelo AS v ON r.NroVuelo = v.Numero 
                   ORDER BY Fecha
                  """

    imprimirEjercicio(consigna, [reserva, pasajero, vuelo], consultaSQL, sql^consultaSQL)

    
    print("# =============================================================================")
    print("# Ejercicios SQL - Tuplas espúreas")
    print("# =============================================================================")

    consigna    = """a.- Vincular (JOIN)  EmpleadoRol y RolProyecto para obtener la tabla original EmpleadoRolProyecto"""
    
    consultaSQL = """
                  SELECT DISTINCT er.* , rp.proyecto
                  FROM empleadoRol AS er
                  INNER JOIN rolProyecto AS rp 
                  ON er.rol = rp.rol            
                  """
    TablaConTuplaDeMas = sql^consultaSQL
    
    consultaSQL = """
                   SELECT * 
                   FROM TablaConTuplaDeMas as t1
                   EXCEPT 
                   SELECT *
                   FROM TablaConTuplaDeMas as t2
                   WHERE t2.empleado='Bruno' AND t2.proyecto='YPF'
                   ORDER BY empleado
                  """

    imprimirEjercicio(consigna, [empleadoRol, rolProyecto], consultaSQL, sql^consultaSQL)

    print("# =============================================================================")
    print("# Ejercicios SQL - Funciones de agregación")
    print("# =============================================================================")

    consigna    = """a.- Usando sólo SELECT contar cuántos exámenes fueron rendidos (en total)"""
    
    consultaSQL = """
                  SELECT count(*) as Examenes_rendidos
                  FROM examen
                  """

    imprimirEjercicio(consigna, [examen], consultaSQL, sql^consultaSQL)


    # -----------
    consigna    = """b1.- Usando sólo SELECT contar cuántos exámenes fueron rendidos en cada Instancia"""
    
    consultaSQL = """
                    SELECT Instancia, count() as Examenes_rendidos
                    FROM examen
                    GROUP BY Instancia
                  """

    imprimirEjercicio(consigna, [examen], consultaSQL, sql^consultaSQL)


    # -----------
    consigna    = """b2.- Usando sólo SELECT contar cuántos exámenes fueron rendidos en cada Instancia (ordenado por instancia)"""
    
    consultaSQL = """
                  SELECT Instancia, count() as Examenes_rendidos
                  FROM examen
                  GROUP BY Instancia
                  ORDER BY Instancia
                  """

    imprimirEjercicio(consigna, [examen], consultaSQL, sql^consultaSQL)


    # -----------
    consigna    = """b3.- Ídem ejercicio anterior, pero mostrar sólo las instancias a las que asistieron menos de 4 Estudiantes"""
    
    consultaSQL = """
                    SELECT Instancia, count() as Examenes_rendidos
                    FROM examen
                    GROUP BY Instancia
                    HAVING Examenes_rendidos < 4
                    ORDER BY Instancia
                  """

    imprimirEjercicio(consigna, [examen], consultaSQL, sql^consultaSQL)


    # -----------
    consigna    = """c.- Mostrar el promedio de edad de los estudiantes en cada instancia de examen"""
    
    consultaSQL = """ 
                    SELECT Instancia, ROUND(AVG(Edad),2) as Promedio_Edad
                    FROM examen
                    GROUP BY Instancia
                    ORDER BY Instancia
                    
                  """

    imprimirEjercicio(consigna, [examen], consultaSQL, sql^consultaSQL)


    print("# =============================================================================")
    print("# Ejercicios SQL - LIKE")
    print("# =============================================================================")

    consigna    = """a1.- Mostrar cuál fue el promedio de notas en cada instancia de examen, sólo para instancias de parcial."""
    
    consultaSQL = """
                   SELECT Instancia, ROUND(AVG(Nota),2) as PromedioNotas
                   FROM examen
                   GROUP BY Instancia
                   HAVING Instancia LIKE 'Parcial%'
                   ORDER BY Instancia
                  """ 

    imprimirEjercicio(consigna, [examen], consultaSQL, sql^consultaSQL)


    # -----------
    consigna    = """a2.- Mostrar cuál fue el promedio de notas en cada instancia de examen, sólo para instancias de parcial. Esta vez usando LIKE."""
    
    consultaSQL = """
                   SELECT Instancia, ROUND(AVG(Nota),2) as PromedioNotas
                   FROM examen
                   GROUP BY Instancia
                   HAVING Instancia LIKE 'Parcial%'
                   ORDER BY Instancia
    
                  """

    imprimirEjercicio(consigna, [examen], consultaSQL, sql^consultaSQL)


    print("# ===================== ====================================================")

    consigna    = """a1.- Listar a cada alumno que rindió el Parcial-01 y decir si aprobó o no (se aprueba con nota >=4)."""
    
    consultaSQL = """
                  SELECT Nombre,
                  Instancia,
                  Nota,
                  CASE WHEN Nota>=4 then 'Aprobó' else 'Desaprobó' END AS Estado
                  FROM examen
                  WHERE Instancia='Parcial-01'
                  ORDER BY Nombre
                  """

    imprimirEjercicio(consigna, [examen], consultaSQL, sql^consultaSQL)


    # -----------
    consigna    = """a2.- Modificar la consulta anterior para que informe cuántos estudiantes aprobaron/reprobaron en cada instancia."""
    
    consultaSQL = """
                 SELECT Instancia,
                 CASE WHEN Nota>=4 then 'Aprobó' else 'Desaprobó' END AS Estado,
                 count(*) AS Cantidad_personas
                 FROM examen
                 GROUP BY Instancia, Estado
                 ORDER BY Instancia
                  """

    imprimirEjercicio(consigna, [examen], consultaSQL, sql^consultaSQL)


    print("# =============================================================================")
    print("# Ejercicios SQL - Subqueries")
    print("# =============================================================================")

    consigna    = """a.- Listar los alumnos que en cada instancia obtuvieron una nota mayor al promedio de dicha instancia"""
    
    
    otraManera = """
                     SELECT e1.nombre, e1.Instancia, e1.Nota
                     FROM examen AS e1
                     WHERE e1.Nota > (
                         SELECT AVG(e2.Nota)
                         FROM examen as e2
                         WHERE e2.Instancia = e1.Instancia) 
                     ORDER BY Instancia ASC, Nota Desc
                     """
    
    otraManera1 = sql^otraManera                 
    
    otraManeraCompleta = """
                        SELECT e1.nombre, e1.Instancia, e1.Nota, e1.Nota as Promedio
                        FROM examen AS e1
                        WHERE e1.Nota > (
                            SELECT AVG(e2.Nota)
                            FROM examen as e2
                            WHERE e2.Instancia = e1.Instancia) 
                        AND Promedio = (
                            SELECT ROUND(AVG(e2.Nota),2)
                            FROM examen as e2
                            GROUP BY Instancia 
                            HAVING e2.Instancia = e1.Instancia)
                         ORDER BY Instancia ASC, Nota Desc
                         """
    

    imprimirEjercicio(consigna, [examen], otraManera, sql^otraManera)


    # -----------
    consigna    = """b.- Listar los alumnos que en cada instancia obtuvieron la mayor nota de dicha instancia"""
    
    otraManera = """
                 SELECT e1.Nombre, e1.Instancia, e1.Nota
                 FROM examen AS e1
                 WHERE e1.Nota = (
                     SELECT MAX(e2.Nota)
                     FROM examen as e2
                     WHERE e2.Instancia = e1.Instancia)
                 ORDER BY Instancia ASC, Nota Desc
                 """

    imprimirEjercicio(consigna, [examen], otraManera, sql^otraManera)


    # -----------
    consigna    = """c.- Listar el nombre, instancia y nota sólo de los estudiantes que no rindieron ningún Recuperatorio"""
    
    consultaSQL = """
                  SELECT e1.Nombre, e1.Instancia, e1.Nota 
                  FROM examen AS e1
                  WHERE NOT EXISTS (
                      SELECT e2.Nombre
                      FROM examen as e2
                      WHERE e1.Nombre = e2.Nombre AND e2.Instancia LIKE 'Recuperatorio%') 
                  ORDER BY Nombre              
                  """

    imprimirEjercicio(consigna, [examen], consultaSQL, sql^consultaSQL)


    print("# =============================================================================")
    print("# Ejercicios SQL - Integrando variables de Python")
    print("# =============================================================================")

    consigna    = """a.- Mostrar Nombre, Instancia y Nota de los alumnos cuya Nota supera el umbral indicado en la variable de Python umbralNota"""
    
    umbralNota = 7
    
    consultaSQL = """
                  SELECT Nombre, Instancia, Nota
                  FROM examen
                  WHERE Nota >$umbralNota
                 """

    imprimirEjercicio(consigna, [examen], consultaSQL, sql^consultaSQL)


    print("# =============================================================================")
    print("# Ejercicios SQL - Manejo de NULLs")
    print("# =============================================================================")

    consigna    = """a.- Listar todas las tuplas de Examen03 cuyas Notas son menores a 9"""
    
    consultaSQL = """
                   SELECT *
                   FROM examen03
                   WHERE Nota < 9
                  """

    imprimirEjercicio(consigna, [examen03], consultaSQL, sql^consultaSQL)

    # -----------
    consigna    = """b.- Listar todas las tuplas de Examen03 cuyas Notas son mayores o iguales a 9"""
    
    consultaSQL = """
                  SELECT *
                  FROM examen03
                  WHERE Nota>=9
                  """


    imprimirEjercicio(consigna, [examen03], consultaSQL, sql^consultaSQL)


    # -----------
    consigna    = """c.- Listar el UNION de todas las tuplas de Examen03 cuyas Notas son menores a 9 y las que son mayores o iguales a 9"""
    
    consultaSQL = """
                  SELECT * 
                  FROM examen03
                  WHERE Nota<9
                  UNION
                  SELECT *
                  FROM examen03
                  WHERE Nota>=9
                  ORDER BY Nombre
                  """


    imprimirEjercicio(consigna, [examen03], consultaSQL, sql^consultaSQL)


    # -----------
    consigna    = """d1.- Obtener el promedio de notas"""
    
    consultaSQL = """
                  SELECT AVG(Nota) as PROMEDIO
                  FROM examen03
                  """


    imprimirEjercicio(consigna, [examen03], consultaSQL, sql^consultaSQL)


    # -----------
    consigna    = """d2.- Obtener el promedio de notas (tomando a NULL==0)"""
    
    consultaSQL = """
                   SELECT AVG(CASE WHEN Nota = NULL THEN 0 ELSE Nota END) AS Promedio
                   FROM examen03

                  """


    imprimirEjercicio(consigna, [examen03], consultaSQL, sql^consultaSQL)

    print("# =============================================================================")
    print("# Ejercicios SQL - Desafío")
    print("# =============================================================================")

    consigna    = """a.- Mostrar para cada estudiante las siguientes columnas con sus datos: Nombre, Sexo, Edad, Nota-Parcial-01, Nota-Parcial-02, Recuperatorio-01 y , Recuperatorio-02"""
    
    # ... Paso 1: Obtenemos los datos de los estudiantes
    datosEstudiantes = sql^consultaSQL
    
    consultaSQL = """
                    SELECT DISTINCT Nombre, Edad, Sexo
                    FROM examen
                  """

    datosEstudiantes = sql^ consultaSQL
    
    # ... Paso 2: Agregamos las notas del Parcial_01
    consultaSQL = """
                  SELECT de.*, e.Nota AS Parcial_01 
                  FROM datosEstudiantes AS de
                  LEFT OUTER JOIN examen AS e 
                  ON de.Nombre = e.Nombre AND e.Instancia = 'Parcial-01'         
                  """
                  # cuidado con colocar where luego del on 

    datosHastaParcial01 = sql^ consultaSQL

    # ... Paso 3: Agregamos las notas del Parcial-02
    consultaSQL = """
                     
                  """

    datosHastaParcial02 = sql^ consultaSQL

    # ... Paso 4: Agregamos las notas del Recuperatorio-01
    consultaSQL = """
                     
                  """

    datosHastaRecuperatorio01 = sql^ consultaSQL

    # ... Paso 5: Agregamos las notas del Recuperatorio-02
    consultaSQL = """
                     
                  """

    datosHastaRecuperatorio02 = sql^ consultaSQL

    desafio_01 = datosHastaRecuperatorio02

    imprimirEjercicio(consigna, [examen], consultaSQL, sql^consultaSQL)


    # -----------
    consigna    = """b.- Agregar al ejercicio anterior la columna Estado, que informa si el alumno aprobó la cursada (APROBÓ/NO APROBÓ). Se aprueba con 4."""
    
    consultaSQL = """

                  """

    desafio_02 = sql^ consultaSQL
    
    imprimirEjercicio(consigna, [examen], consultaSQL, sql^consultaSQL)

    # -----------
    consigna    = """c.- Generar la tabla Examen a partir de la tabla obtenida en el desafío anterior."""
    
    consultaSQL = """

                  """

    desafio_03 = sql^ consultaSQL
    
    imprimirEjercicio(consigna, [examen], consultaSQL, sql^consultaSQL)

    print("# =============================================================================")
    print("# Ejercicios SQL - Reemplazos")
    print("# =============================================================================")

    consigna    = """a.- Consigna: En la descripción de los roles de los empleados reemplazar las ñ por ni"""
    
    consultaSQL = """
                  SELECT empleado, replace(rol,'ñ', 'ni' ) AS rol
                  FROM empleadoRol
                  """

    imprimirEjercicio(consigna, [empleadoRol], consultaSQL, sql^consultaSQL)

    print("# =============================================================================")
    print("# Ejercicios SQL - Mayúsculas/Minúsculas")
    print("# =============================================================================")

    consigna    = """a.- Consigna: Transformar todos los caracteres de las descripciones de los roles a mayúscula"""
    
    consultaSQL = """
                  SELECT empleado, UPPER(rol) AS rol
                  FROM empleadoRol
                  
                  """

    imprimirEjercicio(consigna, [empleadoRol], consultaSQL, sql^consultaSQL)

    # -----------
    consigna    = """b.- Consigna: Transformar todos los caracteres de las descripciones de los roles a minúscula"""
    
    consultaSQL = """
                      SELECT empleado, LOWER(rol) AS rol
                      FROM empleadoRol
                  """

    imprimirEjercicio(consigna, [empleadoRol], consultaSQL, sql^consultaSQL)

    # -----------


# =============================================================================
# FUNCIONES PARA LA GENERACIÓN DE DATAFRAMES 
# =============================================================================
def get_empleado():
    # Genera el dataframe "empleado" que contiene las siguientes columnas 
    # (en el orden mencionado):
        # 1. DNI
        # 2. Nombre
        # 3. Sexo
        # 4. Salaro
        
    # ... Creamos el dataframe vacío (sólo con los nombres de sus columnas)
    empleado = pd.DataFrame(columns = ['DNI', 'Nombre', 'Sexo', 'Salario'])
    # ... Agregamos cada una de las filas al dataFrame
    empleado = pd.concat([empleado,pd.DataFrame([
        {'DNI' : 20222333, 'Nombre' : 'Diego' , 'Sexo' : 'M', 'Salario' : 20000.0},
        {'DNI' : 33456234, 'Nombre' : 'Laura' , 'Sexo' : 'F', 'Salario' : 25000.0},
        {'DNI' : 45432345, 'Nombre' : 'Marina', 'Sexo' : 'F', 'Salario' : 10000.0}
                                                ])
                        ])
    return empleado


def get_alumnosBD():
    # Genera el dataframe "alumnosBD" que contiene las siguientes columnas 
    # (en el orden mencionado):
        # 1. ID
        # 2. Nombre
        
    # ... Creamos el dataframe vacío (sólo con los nombres de sus columnas)
    alumnosBD = pd.DataFrame(columns = ['ID', 'Nombre'])
    # ... Agregamos cada una de las filas al dataFrame
    alumnosBD = pd.concat([alumnosBD,pd.DataFrame([
        {'ID' : 1, 'Nombre' : 'Diego' },
        {'ID' : 2, 'Nombre' : 'Laura' },
        {'ID' : 3, 'Nombre' : 'Marina'}
                                                    ])
                        ])
    return alumnosBD


def get_alumnosTLeng():
    # Genera el dataframe alumnosTLeng que contiene las siguientes columnas 
    # (en el orden mencionado):
        # 1. ID
        # 2. Nombre
        
    # ... Creamos el dataframe vacío (sólo con los nombres de sus columnas)
    alumnosTLeng = pd.DataFrame(columns = ['ID', 'Nombre'])
    # ... Agregamos cada una de las filas al dataFrame
    alumnosTLeng = pd.concat([alumnosTLeng,pd.DataFrame([
        {'ID' : 2, 'Nombre' : 'Laura'    },
        {'ID' : 4, 'Nombre' : 'Alejandro'}
                                                        ])
                        ])
    return alumnosTLeng


def get_persona_ejemploCrossJoin():
    # Genera el dataframe "persona" que contiene las siguientes columnas 
    # (en el orden mencionado):
        # 1. Nombre
        # 2. Nacionalidad
        
    # ... Creamos el dataframe vacío (sólo con los nombres de sus columnas)
    persona = pd.DataFrame(columns = ['Nombre', 'Nacionalidad'])
    # ... Agregamos cada una de las filas al dataFrame
    persona = pd.concat([persona,pd.DataFrame([
        {'Nombre' : 'Diego'   , 'Nacionalidad' : 'AR'    },
        {'Nombre' : 'Laura'   , 'Nacionalidad' : 'BR'    },
        {'Nombre' : 'Marina'  , 'Nacionalidad' : 'AR'    }
                                              ])
                        ])
    return persona


def get_persona_ejemplosJoin():
    # Genera el dataframe "persona" que contiene las siguientes columnas 
    # (en el orden mencionado):
        # 1. Nombre
        # 2. Nacionalidad
        
    # ... Creamos el dataframe vacío (sólo con los nombres de sus columnas)
    persona = pd.DataFrame(columns = ['Nombre', 'Nacionalidad'])
    # ... Agregamos cada una de las filas al dataFrame
    persona = pd.concat([persona,pd.DataFrame([
        {'Nombre' : 'Diego'   , 'Nacionalidad' : 'BR'    },
        {'Nombre' : 'Laura'   , 'Nacionalidad' : None    },
        {'Nombre' : 'Marina'  , 'Nacionalidad' : 'AR'    },
        {'Nombre' : 'Santiago', 'Nacionalidad' : 'UY'    }
                                              ])
                        ])
    return persona


def get_se_inscribe_en_ejemploMismosNombres():
    # Genera el dataframe "se_inscribe_en" que contiene las siguientes columnas 
    # (en el orden mencionado):
        # 1. LU
        # 2. Codigo_materia
        
    # ... Creamos el dataframe vacío (sólo con los nombres de sus columnas)
    se_inscribe_en = pd.DataFrame(columns = ['LU','Codigo_materia'])
    # ... Agregamos cada una de las filas al dataFrame
    se_inscribe_en = pd.concat([se_inscribe_en,pd.DataFrame([
        {'LU':'123/09','Codigo_materia': 1},
        {'LU':' 22/10','Codigo_materia': 1},
        {'LU':' 22/10','Codigo_materia': 2},
        {'LU':'344/09','Codigo_materia': 1}
                                              ])
                        ])
    return se_inscribe_en

def get_materia_ejemploMismosNombres():
    # Genera el dataframe "materia" que contiene las siguientes columnas 
    # (en el orden mencionado):
        # 1. Codigo_materia
        # 2. Nombre
        
    # ... Creamos el dataframe vacío (sólo con los nombres de sus columnas)
    materia = pd.DataFrame(columns = ['Codigo_materia','Nombre'])
    # ... Agregamos cada una de las filas al dataFrame
    materia = pd.concat([materia,pd.DataFrame([
        {'Codigo_materia': 1, 'Nombre':'Laboratorio de Datos'   },
        {'Codigo_materia': 2, 'Nombre':'Análisis II'   },
        {'Codigo_materia': 3, 'Nombre':'Probabilidad'   }
                                              ])
                        ])
    return materia


def get_nacionalidades():
    # Genera el dataframe "nacionalidades" que contiene las siguientes columnas 
    # (en el orden mencionado):
        # 1. IDN (Id Nacionalidad)
        # 2. Detalle
    
    # ... Creamos el dataframe vacío (sólo con los nombres de sus columnas)
    nacionalidades = pd.DataFrame(columns = ['IDN', 'Detalle'])
    # ... Agregamos cada una de las filas al dataFrame
    nacionalidades = pd.concat([nacionalidades,pd.DataFrame([
        {'IDN' : 'AR', 'Detalle' : 'Agentina'},
        {'IDN' : 'BR', 'Detalle' : 'Brasilera'},
        {'IDN' : 'CH', 'Detalle' : 'Chilena'}
                                                          ])
                        ])
    return nacionalidades

# =============================================================================
# DEFINICION DE FUNCIÓN DE IMPRESIÓN EN PANTALLA
# =============================================================================
# Imprime en pantalla en un formato ordenado:
    # 2. Cada dataframe de la lista de dataframes de entrada
    # 3. Query
    # 4. Dataframe de salida
def imprimirEjercicio(consigna, listaDeDataframesDeEntrada, consultaSQL, dataframeResultadoDeConsultaSQL):
    
    print("# -----------------------------------------------------------------------------")
    print("# Consigna: ", consigna)
    print("# -----------------------------------------------------------------------------")
    print()
    for i in range(len(listaDeDataframesDeEntrada)):
        print("# Entrada 0",i,sep='')
        print("# -----------")
        print(listaDeDataframesDeEntrada[i])
        print()
    print("# SQL:")
    print("# ----")
    print(consultaSQL)
    print()
    print("# Salida:")
    print("# -------")
    print(dataframeResultadoDeConsultaSQL)
    print()
    print("# -----------------------------------------------------------------------------")
    print("# -----------------------------------------------------------------------------")
    print()
    print()


# =============================================================================
# EJECUCIÓN MAIN
# =============================================================================
   # 1. Consigna
 
if __name__ == "__main__":
    main()