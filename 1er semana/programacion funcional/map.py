items=list(range(1,11))
print(items)

cuadrados=[]

cuadrados=map(lambda x:x ** 2,items)

print(list(cuadrados))