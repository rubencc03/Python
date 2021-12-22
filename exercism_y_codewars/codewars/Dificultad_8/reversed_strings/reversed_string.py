#Este metodo devuelve un String al reves
def solution(string):
    #Variable donde guardaremos el nuevo string
    alreves=""
    #Utilizamos un bucle for con la variable reversed para que recorra el string al reves
    for i in reversed(string):
        #Añadimos cada letra al nuevo str
        alreves+=i
    #Lo devolvemos
    return alreves

print(solution("abc"))
 