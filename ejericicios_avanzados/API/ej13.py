import requests
import json

#ESTA VERSION NO ES LA QUE SE ESPERA DE COGERLO POR PÁGINAS,PERO ES MAS OPTIMA POR QUE SOLO HAGO UN REQUEST Y LA OBTENCION DE LOS PERSONAJES ES INSTANTANEA
#APARTE GRACIAS AL COUNT SI MAÑANA METEN 983403403489 PERSONAJES SEGUIRA SIENDO INSTANTANEA Y FUNCIONANDO PERFECTAMENTE

#Ponemos la url de la página donde pone el numero de personajes totales
URL = 'https://rickandmortyapi.com/api/character/'
#Metemos la información en data
data = requests.get(URL)
data = data.json() 
#Guardaremos en una variable lo que hay en info
info = data['info']
#Buscamos el count y lo guardamos
totalPersonajes = int(info['count'])







#Pedimos una especie
especie= input("Dime una especie: ")
#el aegs en teoría hace un filtro pero al tener diccionarios dentro de un array no me va(no se por que)
args= {'species':'Human'} 

#Guardamos una cadena para añadirlo a una URL que estan los numeros de los personajes,asi me carga TODOS de golpe en una misma Request
todosP=""

for i in range(1, totalPersonajes+1, +1): 
    todosP+=str(i) + ","

#Creamos la url que seria 'https://rickandmortyapi.com/api/character/1,2,3,4...' asi hasta 826
URL2 = 'https://rickandmortyapi.com/api/character/' + todosP

#Creamos una lista para almacenar el json
xd=[]
#Realizamos el request cogiendo el texto
data = requests.get(URL2,args).text 
#Convertimos en xd la lista PRINCIPAL que dentro tendra 826 diccionarios (si no se comprende ir a https://rickandmortyapi.com/api/character/1,2 y mirar codigo )
xd = json.loads(data) 

#hacemos un for para acceder a cada uno de los diccionarios de la lista xd
for i in xd:
    #Creamos un filtro manual ya que a nosotros no nos va args
    if(i['species'] ==especie):
    #Mostramos el nombre y la especie que nos han indicado
      print(i['name']+ " " + i['species']) 
