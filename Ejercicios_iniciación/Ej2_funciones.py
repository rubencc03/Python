#PARTE 1
#Esta funcion pide dos numeros(VAL 1 Y VAL 2) y devuelve la suma (return val1 + val2)
def suma(val1, val2):
  return val1 + val2

print(suma(3, 5))  

#PARTE 2
#Espacio para que no se solapen los ejercicios
print("")
#Indicativo en pantalla de que empieza el ejercicio 2
print("A PARTIR DE AQUÍ EMPIEZA LA PARTE 2")

#Creamos una lista para hacer el ejercicio
lista=[2,70,80,1000]

#esta funcion te recorre la lista y te multiplica *2 todos sus valores(NO DEVUELVE NADA)
def multi(lista):
    for indice in range(len(lista)):
     lista[indice] = lista[indice] * 2
     
#Ejecutamos la funcion pasandole la lista anteriormente creada
multi(lista)

#Mostramos la lista ya multiplicada por 2
for i in lista:
    print(i)

    #PARTE 3
#Espacio para que no se solapen los ejercicios
print("")
#Indicador de que empieza la parte 3 del ejercicio
print("A PARTIR DE AQUÍ EMPIEZA LA PARTE 3")

#Creamos otra lista 
lista2=[2,70,80,1000]

#Funcion igual que la anterior per con la diferencia de que la lista original no ha sido modificada
def multi2(lista2):
    listacopiada=[] 
    listacopiada=lista2.copy()
    for indice in range(len(lista2)):
     lista2[indice] = lista2[indice] * 2  
    return listacopiada


listanueva=[] 
listanueva=multi2(lista2)

print("DOS LISTAS")

for i in listanueva:
    print(i)

for i in lista2:
    print(i)









