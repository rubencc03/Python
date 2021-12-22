import sys

#ESTE ES UN EJEMPLO EN EL QUE AL USUARIO LE PIDE SUS DATOS PARA REGISTRARSE Y REALIZA
#UNAS ACCIONES DEPENDIENDO DEL RESULTADO


usu_registrado="Ruben"
contra_oficial="12345"

#Si el primer valor que pasas al hacer python ej1.... es correcto continuamos
if sys.argv[1] == usu_registrado:
    #Si el segundo valor que pasas al hacer python ej1.... es correcto Le decimos que ha accedido al sistema
   if sys.argv[2] == contra_oficial:
       print("Ha accedido al sistema correctamente")
       #Si el segundo valor que pasas al hacer python ej1.... es incorrecto Le decimos que se ha equivocado de contraseña
   else: print("Te has equivocado de contraseña,canelo")
#Si el primer valor que pasas al hacer python ej1.... es incorrecto le decimos qu el usuario no existe
else: print("Ese usuario no existe")



print("")
#PARTE SOBRECARGAS FUNCIONES ,BÁSICAMENTE ACCEDEMOS A LA FUNCION INVOCANDOLA DE DOS FORMAS DISTINTAS

def fun( i='por defecto'):   
        print("Has accedido al metodo") 
    
fun(2)#MANERA 1 DE INVOCAR
fun()#MANERA 2 DE INVOCAR