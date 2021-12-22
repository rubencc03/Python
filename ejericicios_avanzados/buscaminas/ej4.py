# Función usada para contar las minas adyacentes en cada posición del array
def contandoMinas(buscaMinas):
    #Miramos cada linea del buscaminas
    for ejeV in range(len(buscaMinas)):
        #Y a su vez cada valor de la linea
        for ejeH in range(len(buscaMinas[ejeV])):
            #Si el numero que estamos mirado en buscaMinas NO es una mina haz esto
            if buscaMinas[ejeV][ejeH] != -1:

                # Hay una mina en la parte superior izquierda
                if ejeV > 0 and ejeH > 0:
                    if buscaMinas[ejeV-1][ejeH-1] == -1:
                        buscaMinas[ejeV][ejeH] += 1
                
                #Comrpobamos si hay una mina superior,si ejeV es mayor que 0 hazme esa comprobación ya que puede ser que hay mina
                #Si no tiene un campo arriba no haría falta probar
                if ejeV > 0:
                    if buscaMinas[ejeV-1][ejeH] == -1:
                        buscaMinas[ejeV][ejeH] += 1

                #Comrpobamos si hay una mina a la izquierda,si ejeH es mayor que 0 hazme esa comprobación ya que puede ser que hay mina
                #Si no tiene un campo a la izquierda no haría falta probar
                if ejeH > 0:
                    if buscaMinas[ejeV][ejeH-1] == -1:
                        buscaMinas[ejeV][ejeH] += 1

               
               #Comprobamos mina inferior izquierda, lo de len(buscaminas) es para comprobar que no estamos en la primera ejeV,es decir
               #que no hay nada a la izquierda,si pusieramos ==0 iria,pero nos quitaría la posibilidad de hacer un sudoku mas grande
                if ejeV +1 < len(buscaMinas) and ejeH > 0 and buscaMinas[ejeV+1][ejeH-1] == -1:
                    buscaMinas[ejeV][ejeH] += 1

                #Comrpobamos si hay mina abajo utilizando el len como he dicho antes
                if ejeV+1 < len(buscaMinas) and buscaMinas[ejeV+1][ejeH] == -1:
                    buscaMinas[ejeV][ejeH] += 1

               
               #Comprobamos mina superior derecha, lo de len(buscaminas) es para comprobar que no estamos en ultima ejeH,es decir
               #que no hay nada a la derecha
                if ejeV>0 and ejeH+1 < len(buscaMinas) and buscaMinas[ejeV-1][ejeH+1] == -1:
                    buscaMinas[ejeV][ejeH] += 1

               #Comprobamos mina derecha, lo de len(buscaminas) es para comprobar que no estamos en la ultima ejeX,es decir
               #que no hay nada a la derecha
                if ejeH+1 < len(buscaMinas[ejeV]) and buscaMinas[ejeV][ejeH+1] == -1:
                    buscaMinas[ejeV][ejeH] += 1

               #Comprobamos mina inferior derecha, lo de len(buscaminas) es para comprobar que no estamos en ultima ejeH,es decir
               #que no hay nada a la derecha y lo de ejeV que hay debajo cosas
                if ejeV+1 < len(buscaMinas) and ejeH+1 < len(buscaMinas[ejeV]) and buscaMinas[ejeV+1][ejeH+1] == -1:
                    buscaMinas[ejeV][ejeH] += 1

    return buscaMinas #devolvemos el buscaminas modificado

#Array con el buscaminas de prueba que especifica el ejercicio
buscaMinas = [[0, 0, -1, 0], [0, -1, -1, 0]]

#Creamos otro array en el que invocaremos la función
minasPegadas = contandoMinas(buscaMinas)

#Mostramos el resultado
print(minasPegadas)