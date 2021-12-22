#En este ejercicio quitamos las vocales de un String
def disemvowel(string_):
    string_=string_.replace("a","");string_=string_.replace("A","")
    string_=string_.replace("e","");string_=string_.replace("E","")
    string_=string_.replace("i","");string_=string_.replace("I","")
    string_=string_.replace("o","");string_=string_.replace("O","")
    string_=string_.replace("u","");string_=string_.replace("U","")

    return string_

print(disemvowel("This website is for losers LOL!"))