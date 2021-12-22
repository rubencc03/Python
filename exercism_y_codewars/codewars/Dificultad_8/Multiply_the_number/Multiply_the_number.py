#Este metodo basicamente multiplica un numero * 5 con la unica variación que se elevara el 5 dependiendo de la longitud del numero
#Por ejemplo si nos dan 200 sería 200 * 5^3
def multiply(n):
    #Guardamos la longitud del numero quitandole el - ya que no es un digito
    lonNum=len(str(n).replace("-",""))
    #Devolvemos la operación anteriormente comentada
    return n * (5**lonNum)

print(multiply(10))
print(multiply(200))                
print(multiply(-3))