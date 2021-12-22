#Este ejercicio consiste en comprobar si hay el mismo numero de o que x
def xo(s):
    #Lo pasamos todo a mayusculas para evitar fallos
    s = s.upper()
    #Esta linea cuenta las veces que aparece x y O y si son las mismas devuelve True,si no,false
    return s.count('X') == s.count('O')

print(xo("ooxx"))
print(xo("xooxx"))
print(xo("ooxxm"))
print(xo("zpzpzpp"))
print(xo("zzoo"))