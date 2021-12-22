def high_and_low(numbers):
    #Utilizamos el split para transformar los numeros separados por espacios en una lista
    listaNum = numbers.split(" ")
    #Contador que utilizaremos para acceder a las distintas posiciones de una lista
    i = 0
    #Hacemos estas dos operaciones ya que si lo igualamos a 0 como he hecho en otros ejercicios tocaría meter otra variable
    masPequeño = int(listaNum[0])
    masGrande = int(listaNum[0])
    #Bucle que recorre numero a numero la lista
    while i < len(listaNum):
        #Transformamos a int y lo asignamos otra vez al mismo sitio(No se puede castear directamente en el int,da eeror)
        listaNum[i] = int(listaNum[i])
        #Si es mayor guardalo como el mas grande
        if listaNum[i] > masGrande:
            masGrande = listaNum[i]
        #Si es menor,guardalo como el mas pequeño
        if listaNum[i] < masPequeño:
            masPequeño = listaNum[i]
        #Avanzamos una posición en la lista
        i += 1
    
    #Casteamos a str para poder  devolverlo todo junto sin que se haga una suma ni de error
    return  str(masGrande)+" "+ str(masPequeño)



print(high_and_low("1 2 3 4 5"))