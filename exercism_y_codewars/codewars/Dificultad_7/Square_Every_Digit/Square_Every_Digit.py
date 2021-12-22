#Este ejercicio devuelve el cuadrado de cada numero,si tenemos 9-2-4 sera 91-4-16
def square_digits(num):
    #Creamos una variable que devolveremos
    numDevolver=""
    #Recorremos el numero casteado a string para que no de error
    for i in str(num):
        #Metemos la elevacion del numero en la variable que devolveremos(importante esos dos casteos a int,los str no pueden multiplicarse)
        numDevolver+=str(int(i) * int(i))
    #Lo devolvemos casteado a int ya que es lo que quiere el programa
    return int(numDevolver)

print(square_digits(9119))
