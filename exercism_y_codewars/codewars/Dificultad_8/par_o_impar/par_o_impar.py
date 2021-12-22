#Comprueba si es par o impar y lo devuelve(Esta en inglés por que así lo pedia la web)
def even_or_odd(n):
    #Si el resto de un numero/2 = 0 es que es par,matematicas puras
    if n % 2 == 0:
        return "Even"
    else : return "Odd"