#Recorremos un array y devolvemos el numero menor
def find_smallest_int(arr):
    smaller=0 #Variable que guarda el numero mas pequeño
    contador=0#Variable utilizada para que si es el primer numero del array lo ponga en smaller
    #Recorremos el array
    for i in arr:
        #Si el numero es mas pequeño asignamelo a la variable smaller y suma el contador +1
        if(i<smaller): 
            smaller=i
            contador+=1
        #Si no es mas pequeño igualmente al ser el primero lo asigna
        elif(contador==0):
            smaller=i
            #Suma contador mas uno para que no asigne por defecto
            contador+=1
    return smaller

my_list=[-873, -72, -581, 996, -117, -613]

print(find_smallest_int(my_list))