#*-* coding: utf-8 *-*

import sqlite3, datetime #importamos la libreria

#conectamos a la base de datos
conexion=sqlite3.connect("chelas.sqlite")

#Seleccionamos el cursor para realizar la consulta
consulta=conexion.cursor()

sql="SELECT * FROM bebidas"

if(consulta.execute(sql)):
	filas=consulta.fetchall()
	for fila in filas:
		print(fila[0],fila[1],fila[2],fila[3])

#Redefinimos nuestra consulta con una especificación diferente
sql="SELECT * FROM bebidas WHERE id_bebida=%s" %2

#Extrayendo un solo registro(fila)
consulta.execute(sql)
fila=consulta.fetchone()
print("Seleccionamos del registro con id 2 ...",fila[0],fila[1],fila[2],fila[3])

#Redefinimos nuestra consulta tomandolas columan específicas
sql="SELECT nombre, precio FROM bebidas"
consulta.execute(sql)
fila=consulta.fetchall()
for fila in filas:
	print(fila[1],"$",fila[2])


#Terminamos la consulta
consulta.close()
#Guardamos los cambios en la base de datos
conexion.commit()
#Cerramos la conexión a la base de datos
conexion.close()