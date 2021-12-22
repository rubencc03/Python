#Pedimos texto
cadena=input("DIME UNA CADENA: ")


#Creamos una fancion a la que le pasaremos el texto
def numPatrones(text):
   save=""
   patron00=0
   ejecount=True
   sumtot=0

   listaR=[]
   #Utilizamos un bucle for para meter en una lista los valores de una cadena separados 
   for i in range(0,len(cadena),1):
     listaR.append(cadena[i:i+1])
    
    #Le añadimos un guión por si acaso la funcion es 000 de el resultado correcto
   listaR.append("-")

#Utilizamos el metodo count que nos devuelve las veces que se repite un patron en una cadena y lo sumamos a una global
  
   patron00=patron00+ cadena.count("101")
   patron00=patron00+ cadena.count("ABC")
   patron00=patron00+ cadena.count("HO")
     
   
#Creamos bucles encargados de guardarnos los numeros de la cadena
   for i in listaR:
     save=save + i
     #Si el numero es 0 puede que la siguiente vez sea 00 entonces ponemos este if para que no borre nada si es 0
     #pero si es otro numero lo borre
     if (not i =="0"):
         save=""
    
    #Si es 00 ponemos un  0 en el save ya que 000 seria tiene que ser como si fuera 00 00 por lo tanto al guardar un 0,a la siguiente
    #entra otra vez en este if
     if(save=="00"):
         save="0"
         #Le decimos,eh que aqui ha pasado una vez el patron 00
         patron00=patron00+1



   #Devolvemos la suma de todo
   return patron00

print(numPatrones(cadena))



