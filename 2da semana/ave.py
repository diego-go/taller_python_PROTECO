class Animal:
	pass

class Volador:
	pass

class Ave(Animal,Volador):
	def __init__(self,plumas1): #El objeto hace referencia a si mismo
		self.plumas=plumas1

	#Definiendo los métodos, se pasa como parametro el nombre de la clase
	@classmethod
	def volar(par1):
		print(par1)

	def hablar(self):
		return "Pio"

pollito=Ave("muchas plumas")

#Invocando método de clase
pollito.volar()
Ave.volar()

#Método de instancia normal, se pasa el objeto
print(pollito.hablar())

#@staticmethod no se pasa nada