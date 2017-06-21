entrada=int(input("Cuantas horas estuviste estacionado?: "))
total=entrada*8
print("Debes de pagar un total de:",total,"pesos")
monedas=[1,2,5,10]
valorMoneda=int(input("\nIngresa las monedas para pagar: "))

if valorMoneda in monedas:
	print("Continua")
	pago=valorMoneda+total
elif:
	pago=total