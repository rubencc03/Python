#Metodo que quita los espacios de un String
def no_space(x):
    #Utilizamos la función replace de python y sustituimos el espacio " " por nada
    x=x.replace(" ","")
    #Devolvemos la palabra
    return x

print(no_space("alca chofas"))