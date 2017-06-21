#*-* coding: utf-8 *-*

import sqlite3 #importamos la libreria

#conectamos a la base de datos
conexion=sqlite3.connect("chelas.sqlite")

"""El acceso a base de datos se define de modo estandar en 
las especificaciones DB-API"""

#Seleccionamos el cursor para realizar la consulta
consulta=conexion.cursor()

#Creando un string que contiene el código SQL
sql="""
CREATE TABLE IF NOT EXISTS bebidas(
id_bebida INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
nombre VARCHAR(50) NOT NULL,
precio FLOAT NOT NULL,
exportacion DATE NOT NULL
)"""

if(consulta.execute(sql)):
	print("Tabla creada con éxito :)")
else:
	print("Error al crear la tabla :(")

#Terminamos la consulta
consulta.close()
#Guardamos los cambios en la base de datos
conexion.commit()
#Cerramos la conexión a la base de datos
conexion.close()