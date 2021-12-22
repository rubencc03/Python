#EJEMPLO IN,BÁSICAMENTE DEVUELVE TRUE SI EL STRING QUE HAY DENTRO
#DE LA VARIABLE EL QUE PREGUNTA ESTA EN LALISTA DE APROBADOS Y DEPENDIENDO
#DE LO QUE DEVUELVA DARA UNA RESPUESTA U OTRA

lista_aprobados = ['Ruben','Adrian','Rada']
ElQuePregunta = 'Sergi'
if ElQuePregunta in lista_aprobados:
    print ("Enorabuena estas aprobado")
else:
    print ("No estas en la lista,vete a tu casa a estudiar Odoo")


#EJEMPLOS IS y NOT,ES UN LOGIN EN EL QUE PONES UNA CONTRASEÑA,SI ACIERTA (UTILIZO EL IS PARA COMPARAR)
#MANDA EL MENSAJE DE BIENVENIDO ADMINISTRADOR,SI NO ACIERTA (MISMA SENTENCIA PERO CON EL NOT) ,ADVIERTE
#AL USUARIO DE QUE NO INTENTE HACKER LA PASSWORD
contra_oficial='12345'
contra_probada='1234'

if contra_probada is contra_oficial:
    print("Bienvenido administrador")

if not contra_probada is contra_oficial:
    print("No intentes hackearnos,por favor")