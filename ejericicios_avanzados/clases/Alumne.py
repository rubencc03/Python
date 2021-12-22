from Profesor import Profesor

#CLASE ALUMNO
class Alumne:
    nom="";curs="";tieneInsti=False;instituto=""; profesor = Profesor()

    #Constructor por defecto alumno
    def __init__(self,nom,curs,profesorResp):
        self.nom = nom
        self.curs=curs
        self.profesor=profesorResp

    #toString de alumno(por eso se veia asi en la escuela)
    def __str__(self):
        cadena=self.nom+" estudio "+self.curs + " de " + self.profesor.nom
        return cadena

    #modificar nombre alumno
    def modiNom(self,nom):
         self.nom=nom

    #modificar curso
    def modiCurs(self,curs):
         self.curs=curs

    #modificar responsable del alumno
    def modiprofesorResp(self,profesorResp):
         self.profesorResp=profesorResp
