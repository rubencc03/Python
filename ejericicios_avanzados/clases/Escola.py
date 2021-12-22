
class Escola:
    nom="";localitat="" ;resposable=""
    alumnos=[]#Array donde iran objetos Alumno
    profesores=[]#Array donde iran objetos Profesor

    #Constructor de Escuela
    def __init__(self,nom,localitat,responsable):
        self.nom = nom
        self.localitat=localitat
        self.resposable=responsable

    #ToString en phyton encargado de al hacer un print de una escuela mostrar toda su estructura
    def __str__(self):
        totalP=""

        #Metemos en un simple String todos los Profesores para mostrarlos en el futuro
        for i in self.profesores:
            totalP = totalP +  "-" +str(i) + "\n"

        totalA=""
        #Metemos en un simple String todos los Alumnos para mostrarlos en el futuro
        for i in self.alumnos:
            totalA = totalA + "-" +  str(i) + "\n"

        #Esto muestra todo
        cadena=self.nom + "es una escuela situada en " + self.localitat + " y su responsable es " + self.resposable + " \n\nProfesores: \n" + totalP + "\n\nAlumnos:\n" +totalA
        return cadena

    #metodo encargado de cambiar la localidad de un colegio(es raro pero alomejor cae un meteorito y se mudan)
    def modiLocalitat(self,localitat):
         self.localitat=localitat

    #metodo cambiar nombre de colegio(Alomejor un Sponsor les obliga)
    def modiNom(self,nom):
         self.nom=nom

    #Metodo cambiar responsable(muy responsable no seria...)
    def modiResponsable(self,resposable):
         self.resposable=resposable

    #Metemos un alumno nuevo(pobrecillo...)
    def insertarAlumno(self,alumno): 
        if(not alumno.tieneInsti):
         self.alumnos.append(alumno)
         alumno.tieneInsti=True
         alumno.instituto=self.nom
        else:
            print( "<ERROR>El alumno " + alumno.nom+" no puede completar su inscripción en el instituto "  +self.nom +" por que ya esta inscrito en " + alumno.instituto )
    #Metemos un profesor nuevo
    def insertarProfesores(self,profesor):
        if(not profesor.trabajaInsti):
             self.profesores.append(profesor)
             profesor.trabajaInsti=True
             profesor.instituto=self.nom
        else:
            print( "<ERROR>El profesor " + profesor.nom+" no puede  trabajar en el instituto "  +self.nom +" por que ya esta trabajando en " + profesor.instituto )
