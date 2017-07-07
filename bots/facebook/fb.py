# -*- coding: utf-8 -*-
from fbchat import Client
from fbchat.models import *
from getpass import getpass

usuario = input("Dame tu correo: ")
cliente = Client(usuario,getpass())

amigos = cliente.fetchThreadList()
nAmigo=0
for amigo in amigos:
	print(nAmigo+1,". "+amigo.name)
	nAmigo+=1

idAmigo=int(input("Ingresa el id del amigo o grupo: "))
idAmigo-=1
mensaje=input("Ingresa tu mensaje:")
cliente.sendMessage(mensaje, thread_id=amigos[idAmigo].uid, thread_type=ThreadType.USER)


cliente.logout()