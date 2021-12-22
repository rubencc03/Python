#CLASE PROFESOR


class Profesor:
     trabajaInsti=False
     nom="";ciencies="";llomix="";instituto=""

     #Constructor por defecto profesor
     def __init__(self,nom="campo vacio",ciencies="campo vacio",llomix="campo vacio"):
        self.nom = nom
        self.ciencies=ciencies
        self.llomix=llomix

     

     #ToString profesor(por eso se muestra así enla escuela)
     def __str__(self):
        cadena=self.nom+" profesor de "+self.ciencies + " / " + self.llomix
        return cadena

    #Funcion para cambiar nombre
     def modiNom(self,nom):
         self.nom=nom

    #Funcion para cambiar Ciencias
     def modiCien(self,ciencies):
         self.ciencies=ciencies

    #Funcion para cambiar llomix
     def modiLlomix(self,llomix):
         self.llomix=llomix
