#############
#Archivos CSV
#############

import csv

with open("muestra.csv","r") as f:
	reader=csv.reader(f)
	for linea in reader:
		print(linea)

f=open("muestra.csv","r")
reader=csv.reader(f)

filas=0

for linea in reader:
	if filas==0:
		header=linea
	else:
		columnas=0
		for columna in linea:
			print("Fila: %d , columna: %d, contenido: %s"%(filas,columnas,datos))
	filas+=1