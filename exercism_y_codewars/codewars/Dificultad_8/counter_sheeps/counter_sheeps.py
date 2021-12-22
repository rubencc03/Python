#Metodo que cuenta los True de dentro de una lista
def count_sheeps(sheep):
  #Variable donde guardamos las ovejas que hay
  numOvejas=0
  #Bucle que recorre todas las celdas de ovejas
  for i in sheep:
      #Si hay una obeja sumera al contador
      if (i == True) : numOvejas+=1
  #Devuelve el numero de obejas
  return numOvejas

my_list=[True,  True,  True,  False,
  True,  True,  True,  True ,
  True,  False, True,  False,
  True,  False, False, True ,
  True,  True,  True,  True ,
  False, False, True,  True]

print(count_sheeps(my_list))