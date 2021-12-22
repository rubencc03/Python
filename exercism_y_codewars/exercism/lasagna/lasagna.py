EXPECTED_BAKE_TIME = 40 #Constante sobre el tiempo que se espera que tarde en cocinarse
PREPARATION_TIME = 2 #Tiempo de preparación por capa
def bake_time_remaining(cuantoLleva):
    '''
    Funcion a la que le pasas el tiempo que llevas cocinando y te devuelve lo que le queda
    '''
    return EXPECTED_BAKE_TIME - cuantoLleva
   

def preparation_time_in_minutes(capas):
   
    '''
     este metodo te calcula cuando tiempo plus necesita dependiendo de las capas,ada capa tarda dos minutos
    '''
    return capas * PREPARATION_TIME

def elapsed_time_in_minutes(capas,cuantoLleva):
    #Cada capa tarda dos minutos
    
    '''
    Calcula 
    '''
    return preparation_time_in_minutes(capas) + cuantoLleva

print(elapsed_time_in_minutes(1,3))