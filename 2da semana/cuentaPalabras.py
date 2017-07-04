import sys

nombreArchivo=sys.argv[1]

f=open(nombreArchivo,"r")

totalPalabras=0
totalCaracteres=0

for linea in f.readlines():#Lista con todas las lineas
	totalPalabras+=len(linea.split())#Lista con cantidad de palabras. strip

for palabra in linea:#.split():
	totalCaracteres+=len(palabra.split())

print("Total de palabras es: ",totalPalabras)
print("Total de caracteres: ",totalCaracteres)

f.seek(0)
totalS=0

cadenas=f.read()
print(str(cadenas).split())
lista=cadenas.split()

for palabra in lista:
	totalS+=len(palabra)

print("La cantidad de palabras es: ",len(lista))
print("La canditad de caracteres es: ",totalS)