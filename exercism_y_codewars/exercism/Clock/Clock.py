class Clock:
    #Trabajar con horas y minutos es muy complejo ,por eso lo pasamos todo a minutos 
    def __init__(self, hour, minute):
        print( (hour*60 + minute)% (24*60)) #Ver calculo con modulo
        print( (hour*60 + minute))#Ver calculo sin modulo

        #Lo pasamos todo a minutos y calculamos el modulo,por que? Da valores diferentes (EN ALGUNOS CASOS)como se puede comprobar ,nosotros queremos que si nos dan
        #24 h sean las 00:00 no las 24:00,que si le damos 25 h ,sean las 01:00 no las 25:00
        self.minutes = (hour*60 + minute)% (24*60)
    #Este metodo es el toString de la clase
    def __repr__(self):
        #Nos aprovechamos de un "printf" para mostrarlo correctamente,la primera parte del codigo (hasta el 60) es la operacion que se calcula y se muestra, la segunda (02) es los espacios que ocupa
        # y si el valor que pasamos solo ocupa uno pondra un 0 delante,todo esto se separa de los : que hay entre los diccionarios
        return f'{self.minutes // 60:02}:{self.minutes%60:02}'
    
    #Este metodo se encarga de comparar dos reloj y ver si son iguales,comparamos los minutos directamente por que si los dos le pasan las 8:00 los dos tendran 480 min
    def __eq__(reloj1, reloj2):
        return reloj1.minutes == reloj2.minutes

    #A este metodo le pasas un reloj y unos minutos que quieres pasar , si le pasas un reloj con las 8:00 y le sumas 3 minutos se quedara en 8:03
    def __add__(self, minutes):
        return Clock(0,self.minutes+minutes)

    #Lo mismo que el  anterior metodo pero restando
    def __sub__(self, minutes):
        return Clock(0,self.minutes-minutes)


reloj1 = Clock(25,00)

print(reloj1)
print(reloj1.__eq__(reloj1))
print(reloj1.__add__(30))
print(reloj1.__sub__(30))


