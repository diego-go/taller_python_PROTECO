import socket

ss=socket.socket()
ss.bind(("localhost",9000))
ss.listen(1)

conn,addr=ss.accept()
print("Iniciando servidor!")
print("Cliente conectado desde: ",addr[0],":",addr[1])

while True:
	recibido=conn.recv(5000).decode()
	if recibido=="Adios":
		break
	print("Cliente dice: ", recibido)
	conn.send(input("Ingresa tu mensaje: ").encode())

print("Se ha terminado la conexión")
ss.close()