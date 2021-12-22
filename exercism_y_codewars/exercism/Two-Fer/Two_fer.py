#Este metodo simplemente dice la frase One for you ,one for me dependiendo de si hay nombre o no
#En el metodo debemos asignar que si no se le pasa ningún valor,por defecto será ""
def two_fer(name=""):
    #Si no se le ha pasado nombre y esta el de por defecto devuelve la opción sin nombre
    if(name=="") : return "One for you, one for me."
    #Si si hay nombre le decimos su nombre
    else: return "One for " + name + ", one for me."
    


print(two_fer("Marcos"))
print(two_fer())