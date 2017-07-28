########
#Cadenas
########

cadena = "hola"
cadena2 = ' mundo'
cadenaLarga = """Esta es una
cadena
con
saltos de
linea"""
cadenaVacia=""
cadenaCruda=r"hola\n\r\t"

#print(cadena)
#print(cadenaCruda)

print("Tipo de cadena: ",type(cadena))
print("Indexación: ",cadena[-2])
print("Tamaño de cadena: ",len(cadena))
print("Concatenación: ",cadena+cadena2)
print("Repetición: ", cadena*3)
#Asignacion no está permitido porque son inmutables
#cadena[0]="H"
#Pueden ser opcionales
print("Slicing: ",cadena[1:3])