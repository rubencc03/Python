#Importamos la biblioteca math
import math
def get_middle(s):
  #Guardamos la mitad redondeando para arriba de la longitud del string
   longi=math.ceil(len(s)/2)
   #Si la longitud del string es par
   if (len(s) % 2 == 0):
     #Devolveremos dos letras
     return  s[longi-1:longi+1]
    #Si es impar,devolvemos 1 letra
   else: return s[longi-1:longi]




print(get_middle("testing"))
print(get_middle("middle"))
