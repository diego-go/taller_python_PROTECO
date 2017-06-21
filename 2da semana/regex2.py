import re

#SEARCH
texto="En este texto se encuentra la palabra mágica"

#re.search(regex,texto) regresa las posiciones

encontrado=re.search("mágica",texto)

print("Encontró la palabra? ", encontrado)

print(encontrado.start())
print(encontrado.end())
print(encontrado.span())
print(texto[encontrado.start():encontrado.end()])

#MATCH
texto="Hola mundo"

encontrado=re.match("Hola",texto) #regresa un valor booleano
if encontrado:
	print("Hizo coincidencia")
else:
	print("No hay coincidencia")

#SPLIT, divide la cadena
texto="vamos a dividir esta cadena"
encontrado=re.split(" ",texto) #Regresa una lista sin el caracter
print(encontrado)
print(" ".join(encontrado))

#METACARACTER . cualquier caracter una sola vez

texto="ola ala ula pla alo ilo"
patrones=[".la",".lo"]

def buscar(patrones, texto):
	for patron in patrones:
		print(re.findall(patron,texto))

buscar(patrones,texto)

#METACARACTER *

texto="hla hola hoola hoola hoooooooooooooola hula huuuulo"
patrones=["h*la","h*lo"]

def buscar(patrones, texto):
	for patron in patrones:
		print(re.findall(patron,texto))

buscar(patrones,texto)

#METACARACTER +

texto="hla hola hoola hoola hoooooooooooooola hula huuuulo"
patrones=["h+la","h+lo"]

def buscar(patrones, texto):
	for patron in patrones:
		print(re.findall(patron,texto))

buscar(patrones,texto)

#METACARACTER ?

texto="hla hola hoola hoola hoooooooooooooola hula huuuulo"
patrones=["h?la","h?lo"]

def buscar(patrones, texto):
	for patron in patrones:
		print(re.findall(patron,texto))

buscar(patrones,texto)

