class Persona3:
	#Definir los atributos
	def __init__(self,nombre,apellido,edad,estatura,dinero):
		self.nombre=nombre
		self.apellido=apellido
		self.edad=edad
		self.estatura=estatura
		self.dinero=dinero
		print("Hola soy", self.nombre,self.apellido,", tengo ",self.edad,"años, y mido",self.estatura)
		print("Tengo $ ",self.dinero,"pesos en mi cuenta")
	def comer(self,comida):
		print("Soy",self.nombre,"y estoy comiendo", comida)
	def informarSaldo(self):
		print("Soy",self.nombre, "y actualmente tengo",self.dinero,"en mi cuenta")
#Vamos a hacer que 2 objetos interactuen entre ellos
#monto: cuanto vamos a prestar
#destinatario: a quien le vamos a prestar
	def prestarDinero(self,monto,destinatario):
		self.informarSaldo()
		destinatario.informarSaldo()

		self.dinero=self.dinero-monto#Aquí le restamos la cantidad que va a prestar
		destinatario.dinero=destinatario.dinero+monto#Aqui le sumamos la cantidad a quien le prestaremos

		self.informarSaldo()
		destinatario.informarSaldo()
	#Método de la claase
	def regalarDinero(donacion,donador,beneficiado):
		donador.informarSaldo()
		beneficiado.informarSaldo()
		donador.dinero=donador.dinero-donacion
		beneficiado.dinero=beneficiado.dinero+donacion

diego=Persona3("Diego","Hernadez",26,1.68,1000)
edgar=Persona3("Edgar","Verges",25,1.80,200)

diego.comer("tacos")

edgar.informarSaldo()

diego.prestarDinero(500,edgar)

print("***********Donación***********")
Persona3.regalarDinero(200,edgar,diego)

diego.informarSaldo()