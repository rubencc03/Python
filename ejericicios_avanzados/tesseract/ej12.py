from PIL import Image
import pytesseract
import os
#Guardamos en una variable la  localización donde estamos
os.chdir("C:/Users/ruben/Desktop/phyton2/tesseract/")

url= os.getcwd()
#Le indicamos donde esta el.exe del tesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

#Cogemos una imagen 
img = Image.open(url+ '\prueba.jpeg')
#Utilizamos pytesseract para leerla
result = pytesseract.image_to_string(img)
#Imprimimos el resultado obtenido de la imagen(Quitando las barras que aparecen inserviblesy)
print(result.replace('_',"").replace('—',""))