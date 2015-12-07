
__author__ = 'gsv'
from CocomoBasico     import CocomoBasico
from CocomoIntermedio import CocomoIntermedio
from CocomoAvanzado   import CocomoAvanzado
from Util             import Util

util = Util()
cocomoBasico = CocomoBasico()
cocomoIntermedio = CocomoIntermedio()

util.printMessage("Bienvenido a estimacion de costos COCOMO") 

def iniciar():
    msg = 0
    while(msg != 3):
        msg = input("Seleccione el modelo cocomo:\n"
                      "1-. Modelo Basico\n"
                      "2.- Modelo Intermedio\n"
                      "3.- Salir\n")
        if msg == 1:
            cocomoBasico.seleccionar_proyecto()
        elif msg == 2:
            cocomoIntermedio.seleccionar_proyecto()
    
    util.printMessage("Gracias por utilizar COCOMO!")
    
iniciar()










