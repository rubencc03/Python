#Metodo que devuelve la suma de todos los numeros POSITIVOS de una lista
def positive_sum(arr):
    #Variable donde guardamos la suma total
    sum=0
    #Recorremos el array
    for i in arr:
        #Si el numero es positivo
        if(i>=0):
            #sumalo
            sum+=i
    #Devuelve la suma
    return sum

mylist = [1,-4,7,-3]

print(positive_sum(mylist))