#Metod que recoge un string y un int y repite ese string n veces
def repeat_str(repeat, string):
    #Variable que devolveremos con el string repetido
    acumulador=""
    #Recorremos un bucle n veces dependiendo del numero que nos hayan pasado
    for i in range(0,repeat,1):
        #En el acumulador que devolvemos ponemos el string
        acumulador+=string 
    return acumulador

print(repeat_str(5,"python"))