############
#Excepciones
############
#Una excepción es un tipo de errorque ocurre durante la ejecución

#try: ->Aquí dentro va el código que nos puede ocasionar una excepción
#except ->Aquí va la excepción, nos puede enviar un mensaje
#else: -> Si no ocurre ninguna excepción, entramos al else
#finally: -> Se va a ejecutar siempre, haya o no haya exepción

try:
	numero=int(input("Ingresa un numero, te lo voy a dividir: "))
	print(10/numero)
except ZeroDivisionError:
	print("Error, no puedes dividir entre cero")
except ValueError:
	print("Estamos solicitando un entero, ingresa un entero")
else:
	print("Todo está bien, no se levantó ninguna exepción")
finally:
	print("Finally se ejecuta siempre, haya o no haya alguna excepción")