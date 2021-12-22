import os
from Escola import Escola
from Profesor import Profesor
from Alumne import Alumne
os.system ("cls") 
os.chdir("C:/Users/ruben/Desktop/phyton2/clases/")


#Aqui creamos alumnos profesores y una escuela y la imprimimos
#También probamos algunos metodos(No hacen falta todos por que son iguales)
print("")
perenxisa = Escola("Perenxisa","Torrente","Maria Jose")
gadea = Escola("Gadea","Aldaia","Miguel Angel")

carlos=Profesor("Carlos","Informatica","mixto")
sergi=Profesor("Manolo","Peluqueria","noestudia")
sergi.modiCien("Informatica")
sergi.modiNom("Sergi")
sergi.modiLlomix("llomix")

ruben=Alumne("Rubén","2DAM",carlos)
fede=Alumne("Fede","2DAM",sergi)

perenxisa.insertarProfesores(carlos)
perenxisa.insertarProfesores(sergi)

perenxisa.insertarAlumno(ruben)
perenxisa.insertarAlumno(fede)
gadea.insertarAlumno(ruben)
gadea.insertarProfesores(carlos)
print(perenxisa)


