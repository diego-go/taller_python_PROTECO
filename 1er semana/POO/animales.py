class Animal():
	def __init__(self,especie,nombre):
		self.especie=especie #atributo público
		self.__nombre=nombre #atributo privado

	"""def getNombre(self):
		return self.__nombre
	def setNombre(self,nombre):
		self.__nombre=nombre"""
	@property
	def __nombre (self):
		print("llamando al Getter")
		return self._nombre

	@__nombre.setter
	def __nombre(self,nombre):
		print("llamando al Setter")
		self._nombre=nombre

rafael=Animal("tortuga","Rafael")
#print("El animal tiene nombre: ",rafael.nombre)
print("El animal de especie: ",rafael.especie)
rafael.especie="gatito"
print("El animal de especie: ",rafael.especie)
#print("El animal tiene nombre: ",rafael.getNombre)
#rafael.setNombre="luis"
#print("El animal tiene nombre: ",rafael.getNombre)
print("El animal tiene nombre: ",rafael._nombre)