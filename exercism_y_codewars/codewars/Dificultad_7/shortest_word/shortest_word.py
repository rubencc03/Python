#Este metodo lee todas las palabras y nos dice cual es la longitud de la mas corta
def find_short(s):
    #Esta variable es donde guardaremos la longitud de la palabra mas corta
    min_longitud=999
    #Guardamos las palabras separadas por " " en distintos espacios de una lista
    palabras=s.split(" ")
    #Bucle que recorre la lista
    for i in palabras:
        #Si la longitud de x palabra es mas pequeña que la longitud de la variable anterior guardamos la longitud de esta
        if(len(i)< min_longitud): min_longitud=len(i)

    #Devolvemos la longitud minima
    return min_longitud

print(find_short("bitcoin take over the world maybe who knows perhaps"))