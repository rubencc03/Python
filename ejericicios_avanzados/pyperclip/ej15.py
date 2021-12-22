from typing import Text
import pyperclip
import re
import os
listaR=[]

os.chdir("C:/Users/ruben/Desktop/phyton2/pyperclip/")

#Abrimos el fichero .txt
with open("llista.txt") as fname:
#Recorremos sus lineas 
 for lineas in fname:
     #utilizamos replace para eliminar un posible salto de linea
     lineas= lineas.replace("\n","")
     #Metemos la palabra a la lista
     listaR.append(lineas)
     

def copyPaste(texto):

    #Este bucle for se encargade coger todas las palabras de la lista de prohibidas y sustituirlas por 4 asteriscos
    # En un futuro se hará una mejora con el len() para que tengan x * dependiendo de la longitud 
    for i in range(len(listaR)):
        auxiliar=listaR[i]
        longitus=""

        #Aquí estamos creando un bucle de la longitud de la palabra que esta cogiendo para que si la palabra es hola ponga 4 * 
        # y si es python ponga 6 * ,es decir el numero de * varie segun la palabra
        for i in range(len(listaR[i])):
            longitus+="*"

        #Es como un replace mas avanzado en el que podemos utilizar IGNORACASE
        src_str  = re.compile(auxiliar, re.IGNORECASE)
        texto  = src_str.sub(longitus, texto)

    #Copiamos la cadena qu enoshan pasado con la modificacion
    pyperclip.copy(texto)


#No continuara hasta que no se modifique lo que hay en el portapapeles
pyperclip.waitForNewPaste()

#Ejecutamos nuestra función
copyPaste(pyperclip.paste())

#Enseñamos llo que tenemos ahora en el portapapeles
print(pyperclip.paste())





