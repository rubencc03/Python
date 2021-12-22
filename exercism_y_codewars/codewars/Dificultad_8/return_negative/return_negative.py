#Este metodo pasa un numero a negativo
def make_negative( number ):
    #Este if es para que si nos pasa un numero negativo NO se multiplique ya que -1 * -1 = 1 y queremos que el resultado sea negativo
    if(number>0):return number*-1
    #Si el numero es negativo devuelvelo así ya
    else:return number

print(make_negative(0))
print(make_negative(-5))
print(make_negative(7))
