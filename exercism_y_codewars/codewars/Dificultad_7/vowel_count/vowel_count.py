#Este metodo cuenta las vocales que tiene un string
def getCount(sentence):
    #Variable que guarda la cantidad de variables que hay
    vocales = 0
    #Bucle que recorre la palabra letra a letra
    for i in sentence:
        #Si la letra es una de estas vocales 
        if i in ['a', 'e', 'i', 'o', 'u']:
            #sumale una al contador
            vocales += 1
    #Devolvemos el numero de vocales
    return vocales

print(getCount("alcachofa"))