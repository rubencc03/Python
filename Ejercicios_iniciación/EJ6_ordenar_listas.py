
#Creamos una lista y le añadimos distintas alturas y pesos
listaSuprema=[]
listaSuprema.append([200,50])
listaSuprema.append([185,89])
listaSuprema.append([200,90])
#utilizamos el sorted para ordenar,el reverse le indica que tiene que ser de menos a mayor y la lamda le indica
#que si compare por altura pero que si estan = compare por peso
print(sorted(listaSuprema,key=lambda x: (x[0], -x[1]), reverse=True))

