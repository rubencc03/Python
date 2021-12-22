#Este metodo devuelve el opuesto de un numero
def opposite(number):
    #Si esta en negativo devolvemos el absoluto que esta en positivo
   if(number <0):
       return abs(number)
    #Si esta en positivo lo multiplicamos *-1 para que devuelva un -1
   else : return number *-1


print(opposite(-1))
print(opposite(1))