import os
#Limpiamos la pantalla cada vez que se ejecute el .py(para evitar suicidios en etapa de desarrollo)
os.system("cls")
def esSudokuCorrecto(listaNum2D):
    #Son contadores encargados de almacenar cuantos numeros hay repetidos
    repVerti = 0
    repHori = 0
    #Recorremos toda la lista filtrada que solo tiene numeros
    for i in range(len(listaNum2D)):
        #Ponemos otro for para así revisar las listas dentro de la lista(listaNum2D)
        for i2 in range(len(listaNum2D[i])):
            #Guardamos valor de x variable en num
            num = listaNum2D[i][i2]
               
            #Comprueba columna horizontal
            for i3 in range(len(listaNum2D[i])):
                if(num == listaNum2D[i][i3]):
                    repHori+=1
            #Comprueba columna vertical
            for i4 in range(len(listaNum2D)):
                if(num == listaNum2D[i4][i2]): 
                    repVerti+=1
    if(repHori == 81 and repVerti == 81): 
        return "Correcto!!! Eres una máquina de los sudokus!"
    else: return "Incorrecto... A ver si prácticamos mas"

#Le damos la ruta donde esta el sudoku(He adjuntado uno correcto(sudoku2.in) y otro incorrecto (sudoku.in))
url = os.getcwd() + "\Sudoku.in"
#abrimos el fichero .in
file = open(url,"r")
#hacemos una lista sucia de sus lineas(tiene espacios y posibles caracteres)
sudokuSucio = file.readlines()


#Este metodo es un filtro NECESARIO,ya que por defecto detecta los espacios y revienta,asi nos aseguramos que solo coja numeros
def filtraArray(n):
    numeros = "123456789"
    devuelveLimpio = []
    for i in range(len(n)):
        #Si encuentras algun numero de mi sudokuSucio en tu variable numeros metelo a la lista
        if(numeros.find(n[i]) != -1):
            devuelveLimpio.append(n[i])
    return devuelveLimpio  

'''
print("lista sucia")
for i in fileTextArray:
    print(i)
'''

#Utilizamos un list map para aplicar el filtro a la lista sucia y que nos devuelva una limpiar(Te he creado dos print comentados
# para que compruebes el antes y despues del filtrado de la lista)
sudokuLimpio = list(map(filtraArray,sudokuSucio))
'''
print("lista limpia")
for i in sudoku:
    print(i)

'''

#Finally, print the result
print("El sudoku del fichero \"" + url + "\" es:")
print(esSudokuCorrecto(sudokuLimpio))


