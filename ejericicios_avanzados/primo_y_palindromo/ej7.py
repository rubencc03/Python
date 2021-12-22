import sys
import os
os.chdir("C:/Users/ruben/Desktop/phyton2/primo_y_palindromo")
numPrimos=0
numPali=0
url= os.getcwd()
print(url)
listaR=[]
listaPrimos=[]
listaPali=[]
listaPriPali=[]

with open(sys.argv[1]) as fname:

#Recorremos sus lineas 
 for lineas in fname:
     #utilizamos replace para eliminar un posible salto de linea
     lineas= lineas.replace("\n","")
     #Metemos la palabra a la lista
     listaR.append(lineas)



"""

>>> esPrimo(9)

"""
#Funcion encargada de saber si un numero es primo
def esPrimo(num):
    #Accedemos a dos variables globales 
    global listaPrimos
    global numPrimos

    #Este bucle se encarga de comprobar si un numero es primo,si NO lo es devuelve false
    for n in range(2, num):
        if num % n == 0:
            return False
   
   #Si el numero es primo sumaremos a la variable numPrimos un numero(indicando la cantidad de numeros primos que hay) 
    numPrimos+=1
    #También lo añadiremos a la lista de numeros primos
    listaPrimos.append(num)
    return True

#Utilizamos un bucle para ejecutar la función esPrimo en todas las palabras de la lista
for i in listaR:
     esPrimo(int(i))

#Mostramos la lista numPrimos
print(numPrimos)

#función encargada de controlar si un numero o un texto es palindromo   
def esPalindromo(numero):
    #Variable que cuenta el numero de palindromos que hay
    global numPali
    #Lista donde meteremos los palindromos
    global listaPali
    #¿Por que hago esto?,para esta función de palindromo poder utilizarla con textos como 'oso',en esta actividad no la utilizaremos por que no lo pide pero ya
    #Que funciona igual lo pongo así,el str es para castear todo a string, el lower es por si la palabra es 'Oso' para que O = o y el replace es por si es una frase con espacios
    estandar = str(numero).lower().replace(' ','')
    #Si es = 
    if(estandar == estandar[::-1] ):
        #Hay un palindromo mas
        numPali+=1
        #El cual voy a meter a la lista
        listaPali.append(numero)

    #Lo devolvemos por que si aunque no es necesario
    return estandar == estandar[::-1] 


#Realizamos el esPalindromo a todos los valores de la lista que hemos cogido del fichero .txt
for i in listaR:
    esPalindromo(int(i))



#Texto indicativo para el programador
print("VALORES QUE COINCIDEN")
#Si un numero esta en las dos listas entonces metelo en una lista aparte donde solo estan los numeros que son primos y palindromos a la vez
for i in listaPrimos:
    if(i in listaPali):
       listaPriPali.append(i)




#Abrimos el fichero en modo escritura
file = open(sys.argv[2], "w")
#Mostramos el segundo argumento que se le ha pasado al usuario en la ejecución del .py(ficheros destino)
print(sys.argv[2])
#Linea donde decimos los numeros palindromos
file.write("Hi han " +str(numPali)+ " numeros palindromos" + os.linesep)
#Linea donde decimos los numeros primos
file.write("Hi han " +str(numPrimos)+ " numeros Primos" + os.linesep)
#Linea donde hacemos una introducción a los números que son Palindromos o Primos
file.write("Los numeros que son primos o Palindromos son: " +os.linesep)
#Bucle for en el que escribimos todos los numeros que son palindromos y primos
for i in listaPriPali:
    file.write(str(i)+ os.linesep)
file.close()