
variable = 1 #Valor que le asignaremos a una sola columna
ajedrez=[0] #No necesitamos la casilla 0 ya que el usuario solo interpeta de la 1 a la 64,asi que ponemos un 0 en la primera
ajedrez.append(variable)#Añadimos manualmente el valor de la primera casilla

#Creamos un bucle que recorra 63 casillas -> 2:65 (No recorremos la primera por que ya tiene el valor asignado manualmente) 
for i in range(2,65):
    ajedrez.append(ajedrez[i-1]*2)#Le decimos básicamente que el valor de la nueva casilla es el de la anterior * 2
    

def square(number):
    #Si el numero es un numero de casilla de ajedrez valido
    if (number > 0 and number < 65):
        #Devuelve el valor de esa casilla
        return ajedrez[number]

    #Si no,devuelve el ValueError que pide,ni un espacio mas ,ni uno menos
    raise ValueError("square must be between 1 and 64")


def total():
    #Variable que guarda una suma
    suma=0
    #Bucle que recorre el array con los valores
    for i in ajedrez:
        #Y los va sumando
        suma+=i
    #Después,devuelve la suma
    return suma
