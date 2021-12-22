import math
def is_square(n):    
    if(n<0):return False
    #Aqui es muy importante castear a int un solo numero,si el numero tiene raiz cuadrada por ejemplo de 4 es dos, da igual que castees ,siempre sera 2-2
    #Pero si es 5 por ejemplo,su raiz cuadrada da 2.22 , por lo tanto si lo restas no dará 0
    if ((math.sqrt(n)-int(math.sqrt(n)))>0): return False
    else:return True
    
print(is_square(5))
