#Metodo encargado de recoger un boolean y devolver yes o no
def bool_to_word(boolean):
    #Si es true devuelve yes
    if(boolean):return "Yes"
    #si es un false devuelve no
    elif(not boolean):return "No"
    #Si no es ninguno de esto dos devuelve un sutil mensaje hacia el usuario
    else: return "Eso no es un true o un false down"


print(bool_to_word(True))
print(bool_to_word(False))