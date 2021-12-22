from kivy.app import App 
from kivy.uix.widget import Widget 
from kivy.uix.screenmanager import ScreenManager, Screen 
from kivy.properties import ObjectProperty 
from kivy.lang import Builder 
from kivy.uix.popup import Popup 
from kivy.uix.floatlayout import FloatLayout 
import pandas as pd 
import os
#Indicamos el directorio en el que quiero trabajar
os.chdir("C:/Users/ruben/Desktop/phyton2/kivy/")

class PopupWindow(Widget): 
    def btn(self): 
        popFun() 
  
class P(FloatLayout): 
    pass
  
  #Creamos una función que muestra el Pop up que hemos creado en el login llamado P y le pone como titulo error contraseña o usuario y le asigna un tamaño
def popFun(): 
    show = P() 
    window = Popup(title = "Error Contrasña o usuario", content = show, 
                   size_hint = (None, None), size = (300, 130)) 
    window.open() 
  
class loginWindow(Screen):
    #Inicializamos el email y el pwd que son los id de los textinput de la contraseña(definidos)
    user = ObjectProperty(None) 
    password = ObjectProperty(None) 

    #Creamos una función encargada de validar si un usuario esta dentro
    def validate(self): 
        boolean=False

        #Recorremos un bucle de los usuarios con una variable que va incrementando,así seremos capaz de acceder a la miventanaPa posición a la vez de las dos listas
        for i in range(0, 2, +1):     

        #Si el usuario esta en la posición i de los users compruebame la contraseña de la misma posición i
         if self.user.text  in users.iloc[i].unique(): 
             
            #Si el password también esta 
            if self.password.text in users.iloc[i].unique():
              #Ponme el bolean a True
              boolean=True
              #Cambiamos a la siguiente ventana
              ventanaP.current = 'logdata'
  
            
              #Vaciamos los textos de los inputs por si luego el pibe vuelve
              self.user.text = "" 
              self.password.text = "" 
  
        #Si el boolean es false signfica que no ha conseguido iniciar sesión,por ello muestra  el popFun
        if(not boolean):
         popFun() 
      
#Creamos la ventana del kv aquí en el fichero .py
class windowManager(ScreenManager): 
    #El pass es una manera de decirle que no quieres que pase nada
    pass

#Creamos la ventana del kv aquí en el fichero .py
class home(Screen): 
    #El pass es una manera de decirle que no quieres que pase nada


    pass
  

  
#Creamos el fichero kivy dentro del programa phyton  para trabajar con el
kv = Builder.load_file('login.kv') 
#Creamos un windowManager(clase que engloba todo en el fichero login.kv)
ventanaP = windowManager() 
#Creamos un loginWindows(ventana 1 donde se realiza el login)
ventanaL = loginWindow(name='login')
#Le cambiamos el tamaño aunque evidentemente no va y sigue apareciendo en grande
ventanaL.size=(1,1)
#Guardamos los usuarios del fichero csv en un DataFrame
users=pd.read_csv('login.csv') 
  
#Añadimos la ventana de login a la ventana principal
ventanaP.add_widget(ventanaL) 
#Añadimos la ventana postLogin a la parte princiapl
ventanaP.add_widget(home(name='logdata')) 
  
#Clase loginMain donde esta todo
class loginMain(App): 
    def build(self): 
        return ventanaP 
  
#If encargado de ejecutar el main
if __name__=="__main__": 
    loginMain().run()