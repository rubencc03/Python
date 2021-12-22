#Devuelve la suma de la longitud de un numero hasta llegar a el,por ejemplo la suma de 3 seria 1+2+3 ; la de 6 -> 1+2+3+4+5+6
def summation(num):
#Variable donde guardamos el total
    total=0
    #Variable que guarda lo que hay que sumar
    suma=1
    #Hacemos el bucle para que se recorra x,por ejemplo si el numero es 2 se recorrera 2 veces 
    for i in range(0,num,1):
        #Vamos sumando al total
        total+=suma
        #Y  vamos actualizando lo que debe sumar en 1 todo el rato
        suma+=1
    #Devolvemos el total
    return total


print(summation(2))
