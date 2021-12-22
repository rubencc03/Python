#Metodo que devuelve la suma de los cuadrados de una lista
def square_sum(numbers):
    #Variable que guarda el total de la suma
    total=0
    #Recorremos la lista y le vamos sumando al total el cuadrado del numero que le toque
    for i in numbers:
        total += i*i
    #Devolvemos el total
    return total

lista=[1,2,3]
print(square_sum(lista))