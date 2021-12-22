from pyzbar.pyzbar import decode
from PIL import Image
import os
#Guardamos en una variable la  localización donde estamos
url= os.getcwd()
#Listamos el contenido de la ruta actual
contenido = os.listdir(url)
imagenes = []

for fichero in contenido:
    #Comprobamos que son ficheros
    if os.path.isfile(os.path.join(url, fichero)) :
        #Si son png o jpg los metemos en la lista(No haría falta jpg en nuestro caso)
       if (fichero.endswith('.jpg' ) or fichero.endswith('.png')):
         imagenes.append(fichero)

#Creamos un bucle que recorra todas las imagenes que hemos listado
for i in imagenes:
    #abrimos la image en el programa
    img = Image.open(i)
    #La decodificamos
    result = decode(img)

    for j in result:
        #imprimimos el nombre de la imagen quitandole el png
        print(i.replace(".png","") ,end=" ")
        #imprimimos el id sacado de result
        print(j.data.decode("utf-8"))

