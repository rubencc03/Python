import math
#Este metodo nos calcula los litros que debe beber una persona por  hora
def litres(time):
    #Cada km es medio litro así que truncamos el tiempo multiplicado por el medio litro por hora
    truncate_time=math.trunc(time*0.5)
    #Le devolvemos rapido los Litros de agua que necesita para no deshidratarse
    return truncate_time

print(litres(11.8))