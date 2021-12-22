import random


class car:
    garaje=[]
    matricula=""
    color=""

    #Creamos un constructor de la clase al cual le tiene que pasar una matricula y un color
    def __init__(self,matricula,color):
        self.matricula=matricula #con el self accedemos a la matricula del objeto y la sustituimos por la que le han pasado al metodo
        self.color=color #con el self accedemos al color del objeto y lo sustituimos por la que le han pasado al metodo
      
        #Mostramos la información del coche
        print("Esta es la matricula: " )
        print(matricula)
        print("Y este el color: " )   
        print(color)

    #Creamos una función encargada de añadir un coche al garaje 
    def añadirGaraje(self):
        xd =input("Quieres añadirlo al garaje? (si/no)")
        #Si el usuario dice si metemos todo lo que sabemos del coche en una lista y esta lista a otra llamada garake
        if xd == "si":
          print("Ha sido añadido a tu garaje")
          self.garaje.append([self.matricula,self.color])
        else: print("Como tu veas")
    
    #Funcion en la que un esperto te puntua tu coche dependiendo del color
    def evaluarCoche(self):
        xd =input("Quieres que te evaluen el coche? (si/no)")
        if xd == "si":
          if self.color == "black":
              print("Este coche es 10/10")
          elif self.color=="white":
              print("Este coche es 8/10")
          elif self.color=="blue":
              print("Este coche es 6/10")
          elif self.color=="red":
              print("Este coche es 4/10")
          elif self.color=="pink":
              print("Este coche es 2/10")

          
        else: print("Tu te lo pierdes")
    
    




#Creamos una lista de colores para pasar colores all azar
lista=["red","white","black","blue","pink"]

#Le pedimos el numero de coches que quiere crear
num_car=int(input("Dime el numero de doches que quieres crear: "))
i=0
#Realizamos un bucle creando los coches y realizando las funciones que hemos creado
while  num_car is not i:
        car1 = car(i+1,random.choice(lista))
        i=i+1
        car1.añadirGaraje()
        car1.evaluarCoche()
        print("")





        
