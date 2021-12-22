def exchange_money(budget, exchange_rate):
    """

    :param budget: float - amount of money you are planning to exchange.
    :param exchange_rate: float - unit value of the foreign currency.
    :return: float - exchanged value of the foreign currency you can receive.
    """
    #Este return realiza una transformación de USD  a EUR ,el usuario decide cuantos USD vale 1€
    return budget / exchange_rate


def get_change(budget, exchanging_value):
    """

    :param budget: float - amount of money you own.
    :param exchanging_value: int - amount of your money you want to exchange now.
    :return: float - amount left of your starting currency after exchanging.
    """
    #Este return devuelve la pasta que nos queda en el monedero despues de realizar x operacion exchange_money(127.5, 1.2) = 106.25
    return budget - exchanging_value


def get_value_of_bills(denomination, number_of_bills):
    """

    :param denomination: int - the value of a bill.
    :param number_of_bills: int - amount of bills you received.
    :return: int - total value of bills you now have.
    """
    #Este return nos devuelve el dinero total multiplicando x monedas iguales por el precio de cada una |get_change(127.5, 120) = 7.5
    return denomination * number_of_bills


def get_number_of_bills(budget, denomination):
    """

    :param budget: float - the amount of money you are planning to exchange.
    :param denomination: int - the value of a single bill.
    :return: int - number of bills after exchanging all your money.
    """
    #Este return simplemente devuelve la cantidad de criptomonedas que podemos comprar con nuestro dinero | get_value_of_bills(5, 128) = 640
    return int(budget/denomination)


def exchangeable_value(budget, exchange_rate, spread, denomination):
    """

    :param budget: float - the amount of your money you are planning to exchange.
    :param exchange_rate: float - the unit value of the foreign currency.
    :param spread: int - percentage that is taken as an exchange fee.
    :param denomination: int - the value of a single bill.
    :return: int - maximum value you can get.
    """
    #Calculamos el nuevo spread y le sumamos uno por que tiene que multiplicar a la cuota de intercambio,ya que el exchange_rate es lo que perdemos y
    #ese porcentaje de spread nos quita money,no nos lo da
    spread = 1+ (spread/100) 
    #Realizamos una multiplicación que nos da 1,32 que eso significa que por cada 1,32€ nos daran 1USD,asi que realizamos la conversion de la budget
    budget = budget/(spread*exchange_rate)
    #Ene ste punto nos quedan 96€ y queremos saber cuanto podemos gastar de ello para comprar monedas,así que lo primero será calcular cuantas monedas podemos
    #comprar que en este caso será 96/20 = 4.8
    budget = budget/denomination
    #Pero claro,no puedes comprar 4.8 monedas,se pueden comprar 4,5,6 ,pero no 5.6 ,4.2 ,tiene que ser un entero.
    #Entonces parseamos ese double a int y lo multiplicamos por lo que vale cada moneda, entonces nos el precio de las monedas reales que podemos comprar
    # Recuerda que tenemos 96€ y podemos comprar 4 monedad(80€) ,si quisieramos comprar 5 serían 100€ y no podemos por que tenemos 96
    budget = int(budget)*denomination
    

    return budget # exchangeable_value(127.25, 1.20, 10, 20) = 80

#print(exchangeable_value(127.25, 1.20, 10, 5))


def non_exchangeable_value(budget, exchange_rate, spread, denomination):
    """

    :param budget: float - the amount of your money you are planning to exchange.
    :param exchange_rate: float - the unit value of the foreign currency.
    :param spread: int - percentage that is taken as an exchange fee.
    :param denomination: int - the value of a single bill.
    :return: int non-exchangeable value.
    """
    spread = 1+ (spread/100)
    budget = budget/(spread*exchange_rate)
    #Hasta este punto realizamos los mismos calculos que en el anterior,solo que aquí no queremos saber el valor real de las monedas que queremos comprar,
    #Lo que queremos saber es el dinero que nos sobrará si hacemos x compra, recuerda que teniamos 96€ pues si sacamos el modulo de 20 nos quedan 16€

    budget = budget % denomination

    return int(budget) #non_exchangeable_value(127.25, 1.20, 10, 20) = 16

print(non_exchangeable_value(127.25, 1.20, 10, 20))
