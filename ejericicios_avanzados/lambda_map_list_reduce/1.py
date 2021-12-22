#Esta función lambda es simple,recoge 3 numeros y los suma entre si
from typing import List
import functools

#Creamos una lamda encargada de sumar 3 numeros que le pases
f = lambda x, y, z: x + y + z

print(f(2, 3, 4))



#Ponemos espacio para separar ejercicios
print("") ;print("");print("");print("")





print("Dime una cadena de Numeros separados por espacios")
cadena = input()
#Utilizamos el split para separar el String cadena en distintos apartados de una lista
listaR = list(cadena.split(" "))

#Realizamos un try except para que si nos ha pasado una letra suelte una excepcion
try:
 listaRint=list(map(int,listaR))
 for i in listaRint:
    print(i)
except ValueError:
   print("Ponia bien claro que SOLO numeros,a ver si leemos los enunciados")


#Creamos una funcion que quite los numeros menores de 10
def comproMen10(numeros):
   if(int(numeros)>10):
     return True

#Utilizamos un filter en el que le pasamos a la anterior funcion la lista
lisFiltr=list(filter(comproMen10,listaRint))

#Enseñamos el contenido de la lista ya limpia
print("LISTA FILTRADA")
for i in lisFiltr:
    print(i)

#Creamos una lambda del reduce sobre la lista para que nos multiplique todo
print("MULTIPLICACIÓN: " +functools.reduce(lambda a, b: a*b, listaRint))





















































