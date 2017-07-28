class Persona4:
	def __init__(self,nombre2,apellido2,edad2,estatura2,dinero2):
		self.nombre=nombre2
		self.apellido=apellido2
		self.edad=edad2
		self.estatura=estatura2
		self.dinero=dinero2

	#LA CLASE EJECUTA ESTE MÉTODO
	@classmethod
	def vivir(clase):
		print("Soy una",clase,"y estoy vivo")

	#LO EJECUTA CUALQUIERA, TANTO LA CLASE COMO LA INSTANCIA
	@staticmethod
	def respirar():
		print("respirar")

	def comer(self):
		print("comer")

diego=Persona4("Diego","Hernandez",26,1.68,200)

#Metodo de clase
Persona4.vivir()

#Método estático, no lleva parametros, lo ejecuta la clase y la instancia
Persona4.respirar()
diego.respirar()

#Método estático
Persona4.comer(diego)
diego.comer()
