import abc
import hashlib #Importamos la libreria que nos permitira crear las contraseñas

#Creamos llas password codificandolas con sha1 utilizanod hashlib

password1=hashlib.new("sha1",b"soyMarcos")
password2=hashlib.new("sha1",b"soyJuan")
password3=hashlib.new("sha1",b"soyJulio")
password4=hashlib.new("sha1",b"soyPenelope")




#lista= [usu1,usu2,usu3,usu4]
diccionario = {"infoMarcos":["Marcos",password1],"infoJuan":["Juan",password2],"infoJulio":["Julio",password3],"infoPenelope":["Penelope",password4]}
print("DICCIONARIO")

#Mostramos los distitos elementos del diccionario
print (diccionario['infoMarcos']) 
print (diccionario['infoJuan']) 
print (diccionario['infoJulio']) 
print (diccionario['infoPenelope']) 
# linea separacion 
print()

print("LISTA")
#Creamos lista
lista=[]
#Le introducimos listas con la información de los usuarios
lista.append(["Marcos",password1])
lista.append(["Juan",password2])
lista.append(["Julio",password3])
lista.append(["Penelope",password4])

#Mostramoos la información de la lista
print(lista)