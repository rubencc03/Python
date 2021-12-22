#Este metodo se encarga de coger un string y repetirlo dependiendo de la posicion del String donde este y poniendo la primera letra mayuscula
#Por ejemplo abc seria A-Bb-Ccc
def accum(s):
    contador=1
    guardar=""
    #Recorremos toda la palabra
    for i in s:
        #Creamos un contador interno que nos permitira poner la primera letra en mayusculas,tiene que estar aquí para cada vez que cambiemos de letra se resetee el valor a 0
        contadorInterno=0
        #Bucle para escribir x veces una letra,cada vez que cambiamos una letra le decimos que la escriba una vez más 
        for i2 in range(0,contador,1):
            #Si es la primera letra ponmela en mayuscula y aumentame el contador para que la siguiente no la ponga en mayuscula
            if(contadorInterno==0):
                guardar+=i.upper()
                contadorInterno+=1
            #Si no es la primera añadela en minusculas si o si
            else: guardar+=i.lower()
        #Añadimos el contador de las veces que escribira una letra
        contador+=1
        #Ponemos un guion despues de cada letra
        guardar+="-"

    #Devolvemos el String de todas las letras menos un - restante que sobra
    return guardar[:-1]

print(accum("zpglnrxqenu"))