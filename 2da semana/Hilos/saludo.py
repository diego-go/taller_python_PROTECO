import threading

#Definimos la funcion que realizará el hilo
def saluda(nombre):
	print("Hola",nombre)

#Creamos dos objetos de tipo thread
hilo=threading.Thread(target=saluda,args=("Diego",))
hilo2=threading.Thread(target=saluda,args=("Alan",))
hilo3=threading.Thread(target=saluda,args=("Alfredo",))
hilo4=threading.Thread(target=saluda,args=("Alejandro",))
hilo5=threading.Thread(target=saluda,args=("Javier",))
hilo6=threading.Thread(target=saluda,args=("Jorge",))
hilo7=threading.Thread(target=saluda,args=("Edgar",))


#Inicializamos los hilos
hilo.start()
hilo2.start()
hilo3.start()
hilo4.start()
hilo5.start()
hilo6.start()
hilo7.start()