import os
import shutil

ejemplo_dir = 'C:/Users/ruben/Desktop/phyton2/organizador_ficheros'
contenido = os.listdir(ejemplo_dir)
imagenes = []
documentos = []
programacion = []
videosYmusica = []

url= os. getcwd()
print(url)

for fichero in contenido:

    #If encargado de SOLO coger ficheros(no directorios)
    if os.path.isfile(os.path.join(ejemplo_dir, fichero)) :
        #Si es una imagen se va a la lista imagenes
       if (fichero.endswith('.jpg' ) or fichero.endswith('.png')):
         imagenes.append(fichero)
         #creamos la carpeta imagenes si no existe
         if( not os.path.isdir(url + '\imagenes')):
              os.mkdir('imagenes')

       #si es un documento se va a la lista documentos
       elif(fichero.endswith('.txt') or fichero.endswith('.odt') or fichero.endswith('.doc') or fichero.endswith('.pdf')   ):
         documentos.append(fichero)
         #Si no existe la carpeta documentos se crea
         if(not os.path.isdir(url+'\documentos')):
              os.mkdir('documentos')
        #Los ficheros de programacion se va a la lista programacion  
       elif(fichero.endswith(  '.kt' ) or fichero.endswith(  '.py' )):
          programacion.append(fichero)
          if(not os.path.isdir(url+'\programacion')):
              os.mkdir('programacion')
        #Los ficheros musica/video se van a la lista videosYmusica
       elif(fichero.endswith(  '.mp4' ) or fichero.endswith(  '.wav' ) or fichero.endswith('mp3')):
          videosYmusica.append(fichero)
          if(not os.path.isdir(url+'\videosYmusica')):
              os.mkdir('videosYmusica')





#Todos estos for son los encargados de mover las imagenes
for i in imagenes:
    shutil.move(i,url + '\imagenes')
    print(i)

for i in documentos:
    shutil.move(i,url + '\documentos')
    print(i)
    
for i in programacion:
    shutil.move(i,url + '\programacion')
    print(i)

    
for i in videosYmusica:
    shutil.move(i,url + '\videosYmusica')
    print(i)


