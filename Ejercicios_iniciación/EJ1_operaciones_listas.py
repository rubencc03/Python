#Creamos una lista con muchos elementos
lista=["casilla1", "casilla2", "casilla3","casilla4", "casilla5"]

#copiamos una lista
copy_lista = lista.copy()
#Mostramos la posicion de una lista 
print(copy_lista[0])
#Añadimos un elemento a una lista en la ultima posición
copy_lista.append("Añadido")
#Mostramos el elemento recien añadido
print(copy_lista[3])
#Quitamos el primer elemento de la lista
copy_lista.remove("casilla1")
#Imprimimos el primer elemento de la lista para que vemos que ha cambiado
print(copy_lista[0])

#Creamos una lista con los ultimos 4 elementos de 
listaUltimos=[copy_lista[-1], copy_lista[-2], copy_lista[-3], copy_lista[-4]]
#Print de espacio, podemos ponerlo con \n pero lo he puesto así
print("")
#Print indicativo para mi para saber que aquí mostrabamos la lista de los ultimos
print("A partir de aquí empieza el bucle")
for i in listaUltimos:
    print(i)

 #Otro salto de linea
print("")

#Aquí empieza la lista En la que separamos por espacios

#Creamos un string con 4 letras
separado = "A B C D"
#Utilizamos un split para que solo coja las litras sin el espacio -> ' ' lo indica
output=separado.split(' ')
list(output)

#Ultimo buble para mostrar que realmente no hay espacios
for i in output:
    print(i)

'''
Aqui ha 
acabado la lista

'''


    
'''
○ ¿Quina és la diferència en Python entre “shallow copy” i “deep copy”?

-Deep copy: construeix un nou objecte compost i es copia de l'original
-Shallow copy:Es crea un nou objecte amb referències a altres objectes


'''