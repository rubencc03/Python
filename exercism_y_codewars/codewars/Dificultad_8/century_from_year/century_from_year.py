import math
#Metodo que calcula a que siglo pertenece un año
def century(year):
    #Devolvemos el año/100 redondeado para arriba,por ejemplo con mi ejemplo haria 1601 -> 16.01 -> 17
    return math.ceil(year / 100)

print(century(1601))
