#Este metodo quita la primera y la ultima letra de un string
def remove_char(s):
#Quita la primera letra
 str1=s[:-1]
 #~Quita la segunda
 str2=str1[1:]
 #Devuelve la palabra final sin las dos letras
 return str2

#Quería trabajar con solo una variable pero da fallos
print(remove_char("python"))