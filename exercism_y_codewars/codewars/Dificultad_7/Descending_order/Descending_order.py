def Descending_Order(num):
    #Esta variable será la que devolveremos en el return
    devolver=""
    #Creamos una lista que ordene los numeroa al reves
    lista= sorted(str(num), reverse=True)
    #Metemos los elementos de esta lista en un String
    for i in lista:
        devolver+=i

    #Casteamos a int que es lo que pide la web
    return int(devolver)

print(Descending_Order(23323923672))
