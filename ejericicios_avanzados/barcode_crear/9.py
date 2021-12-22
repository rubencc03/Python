import pandas as pd
from barcode import EAN13
from barcode.writer import ImageWriter
import barcode
import os

#Guardamos ruta actual
url= os.getcwd()
#metemos en un DataFrame los datos del csv
datos=pd.read_csv('usuarios.csv',header=0) 
#Metemos los nombres del dataframe en una lista
lista=datos['nomalumne']
#Metemos los ids del dataframe en una lista
listab=datos['ID']


     
     
#Cremos un for que con zip recorre dos listas a la vez
for i, j in zip(lista, listab):
   EAN = barcode.get_barcode_class("ean13")
   #Creamos el ean en el que el valor j es el id del wacho
   ean = EAN(str(j), writer=ImageWriter())
   #Guardamos la imagen en la url(i es el nombre,por eso la doble lista)
   ean.save(url+'/'  + i)

