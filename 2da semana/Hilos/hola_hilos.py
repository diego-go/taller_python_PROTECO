import threading,time
from threading import Thread

def loop(nombre,n):
	for i in range(1,n):
		time.sleep(1) #Con esto hacemos que espere 1 seg
		print(nombre,":",i)

while True:
	t1=Thread(target=loop,args=("hilo A",16))
	t1.start()
	t2=Thread(target=loop,args=("hilo B",11))
	t2.start()
	#El threading.active_count() nos regresa un 
	#entero que indica el número de hilos que están
	#corriendo en ese momento
	print("En este momento hay :",threading.active_count(),"hilos corriento")
	print(threading.enumerate())
	#Con esto sabemos el nombre del hilo
	print("El hilo actual es: ",threading.currentThread().name)

	t1.join()
	t2.join()

	repetir=input("Si quieres repetir, presiona S, si no presiona N\n")

	if repetir == "n" or repetir == "N":
		break