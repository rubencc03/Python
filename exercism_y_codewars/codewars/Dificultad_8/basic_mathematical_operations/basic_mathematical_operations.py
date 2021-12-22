#Metodo al que le pasamos un operador y dos valores y hará x operaciones dependiendo de lo que hayamos puesto
def basic_op(operator, value1, value2):
    #suma
    if (operator=="+"): return value1 + value2
    #resta
    elif (operator=="-"): return value1 - value2
    #divide
    elif (operator=="/"): return value1 / value2
    #multiplica
    elif (operator=="*"): return value1 * value2

print(basic_op("+",1,2))
print(basic_op("-",1,2))
print(basic_op("/",1,2))
print(basic_op("*",1,2))