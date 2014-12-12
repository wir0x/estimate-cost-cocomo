
__author__ = 'gsv'
from CocomoBasico     import CocomoBasico
from CocomoIntermedio import CocomoIntermedio
from CocomoAvanzado   import CocomoAvanzado


print("*") * 50
print("\nBienvenido a estimacion de costos COCOMO\n")
print("*") * 50

cocomoBasico = CocomoBasico()
cocomoIntermedio = CocomoIntermedio()

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
    print("*" *50 +
          "\nGracias por utilizar COCOMO!\n" +
          "*" * 50)
iniciar()










