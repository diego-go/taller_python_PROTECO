############
#Ejemplo POO
############

#definiendo una clase
class Persona:
	#Atributos
	edad=21
	saludo="Hola"
	#Este es un método de la clase persona
	def saludar(self):
		print("%s soy una persona" %self.saludo)

	def unaFuncion():
		print("Esto es una funcion de la clase persona")

#Instancia o creacion de un objeto a partir de una clase
diego=Persona()

print(diego.edad)
print(diego.saludo)

diego.saludar()

Persona.unaFuncion()

print(Persona.edad)