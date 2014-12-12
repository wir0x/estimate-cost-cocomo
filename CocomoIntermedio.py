#!/usr/bin/phython
# coding=utf-8
__author__ = 'gsv'
from SoftwareProject import  SoftwareProject
sp = SoftwareProject()

class CocomoIntermedio(object):

    def __init__(self):
        self.escala = 3

    def seleccionar_proyecto(self):
        proyecto = 0
        while (proyecto != 4):
            proyecto = input("\nSeleccione un tipo de proyecto:\n\n"
                             "1.- Organico\n"
                             "2.- Semi Organico\n"
                             "3.- Empotrado\n"
                             "4.- Salir\n")
            if proyecto == 1:
                sp.organic()
                self.calcular_organico()

            elif proyecto == 2:
                sp.semi_dechead()
                self.calcular_semiAcoplado()

            elif proyecto == 3:
                sp.embedded()
                self.calcular_empotrado()

        print("*" *50 +
              "\nGracias por utilizar COCOMO!\n" +
              "*" * 50)

    def calcular_organico(self):
        kloc = input("Ingrese KLOC (1000 lineas de código fuente):\n")
        pf = 261.36
        kloc = (pf * kloc) / 1000
        E = ((sp.a * kloc) ** sp.b) * self.iniciar()
        D = (sp.c * E) ** sp.d
        P = E / D
        print("=" * 50 +
              "\nEsfuerzo (personas/mes):\n " + str(E) +
              "\nDuracion (meses):\n " + str(D) +
              "\nPersonal (recomendado)): \n" + str(P)+"\n"+
              "=" * 50)

    def calcular_semiAcoplado(self):
        kloc = input("Ingrese KLOC (1000 lineas de código fuente):\n")
        pf = 261.36
        kloc = (pf * kloc) / 1000
        E = ((sp.a * kloc) ** sp.b) * self.iniciar()
        D = (sp.c * E) ** sp.d
        P = E / D
        print("=" * 50 +
              "\nEsfuerzo (personas/mes):\n " + str(E) +
              "\nDuracion (meses):\n " + str(D) +
              "\nPersonal (recomendado)): \n" + str(P)+"\n"+
              "=" * 50)

    def calcular_empotrado(self):
        kloc = input("Ingrese KLOC (1000 lineas de código fuente):\n")
        pf = 261.36
        kloc = (pf * kloc) / 1000
        E = ((sp.a * kloc) ** sp.b) * self.iniciar()
        D = (sp.c * E) ** sp.d
        P = E / D
        print("=" * 50 +
              "\nEsfuerzo (personas/mes):\n " + str(E) +
              "\nDuracion (meses):\n " + str(D) +
              "\nPersonal (recomendado)): \n" + str(P)+"\n"+
              "=" * 50)

    def test(self):
        print("hello world")

    def iniciar(self):
        fae = 1

        print("-"*50 +"\n ATRIBUTOS DE SOFTWARE\n" + "-" * 50 + "\n")

        print("Fiabilidad")
        self.escala = self.entrada_escala()
        fae *= self.rely()
        print("\nTamanio de base de datos")
        self.escala = self.entrada_escala()
        fae *= self.data()
        print("\nComplejidad")
        self.escala = self.entrada_escala()
        fae *= self.cplx()

        print("-"*50 +"\nATRIBUTOS DE HARDWARE\n"+ "-" * 50 + "\n")

        print("\nRestricciones de tiempo de ejecución")
        self.escala = self.entrada_escala()
        fae *= self.time()
        print("\nRestricciones de memoria virtual")
        self.escala = self.entrada_escala()
        fae *= self.stor()
        print("\nVolatilidad de la máquina virtual")
        self.escala = self.entrada_escala()
        fae *= self.virt()
        print("\nTiempo de respuesta")
        self.escala = self.entrada_escala()
        fae *= self.turn()

        print("-"*50 +"\nATRIBUTOS DE PERSONAL\n"+ "-" * 50 + "\n")

        print("\nCapacidad de análisis")
        self.escala = self.entrada_escala()
        fae *= self.acap()
        print("\nExperiencia en la aplicación")
        self.escala = self.entrada_escala()
        fae *= self.aexp()
        print("\nCalidad de los programadores")
        self.escala = self.entrada_escala()
        fae *= self.pcap()
        print("\nExperiencia en la máquina virtual")
        self.escala = self.entrada_escala()
        fae *= self.vexp()
        print("\nExperiencia en el lenguaje")
        self.escala = self.entrada_escala()
        fae *= self.lexp()

        print("-"*50 +"\nATRIBUTOS DE PERSONAL\n"+ "-" * 50 + "\n")

        print("\nTécnicas actualizadas de programación")
        self.escala = self.entrada_escala()
        fae *= self.modp()
        print("\nUtilización de herramientas de software")
        self.escala = self.entrada_escala()
        fae *= self.tool()
        print("\nRestriccion de tiempo de desarrollo ")
        self.escala = self.entrada_escala()
        fae *= self.sced()

        return  fae

    def entrada_escala(self):
        escl = input("Seleccione la Escala:\n "
                       "\n 1.- Muy bajo"
                       "\n 2.- Bajo"
                       "\n 3.- Nominal"
                       "\n 4.- Alto"
                       "\n 5.- Muy alto"
                       "\n 6.- Extra alto\n")
        return escl

    # Atributos de Sofware
    def rely(self):
        valor = 1
        # Muy bajo
        if self.escala == 1:
            valor = 0.75
        # Bajo
        elif self.escala == 2:
            valor = 0.88
        # Nominal
        elif self.escala == 3:
            valor = 1
        # Alto
        elif self.escala == 4:
            valor = 1.15
        # Muy Alto
        elif self.escala == 5:
            valor = 1.40
        # Extra Alto
        elif self.escala == 6:
            valor = 1
        return valor

    def data(self):
        valor = 1
        # Muy bajo
        if self.escala == 1:
            valor = 1
        # Bajo
        elif self.escala == 2:
            valor = 0.94
        # Nominal
        elif self.escala == 3:
            valor = 1
        # Alto
        elif self.escala == 4:
            valor = 1.08
        # Muy Alto
        elif self.escala == 5:
            valor = 1.16
        # Extra Alto
        elif self.escala == 6:
            valor = 1
        return valor

    def cplx(self):
        valor = 1
        # Muy bajo
        if self.escala == 1:
            valor = 0.70
        # Bajo
        elif self.escala == 2:
            valor = 0.85
        # Nominal
        elif self.escala == 3:
            valor = 1
        # Alto
        elif self.escala == 4:
            valor = 1.15
        # Muy Alto
        elif self.escala == 5:
            valor = 1.30
        # Extra Alto
        elif self.escala == 6:
            valor = 1.65
        return valor

    # Atributos de Hardaware
    def time(self):
        valor = 1
        # Muy bajo
        if self.escala == 1:
            valor = 1
        # Bajo
        elif self.escala == 2:
            valor = 1
        # Nominal
        elif self.escala == 3:
            valor = 1
        # Alto
        elif self.escala == 4:
            valor = 1.11
        # Muy Alto
        elif self.escala == 5:
            valor = 1.30
        # Extra Alto
        elif self.escala == 6:
            valor = 1.66
        return valor

    def stor(self):
        valor = 1
        # Muy bajo
        if self.escala == 1:
            valor = 1
        # Bajo
        elif self.escala == 2:
            valor = 1
        # Nominal
        elif self.escala == 3:
            valor = 1
        # Alto
        elif self.escala == 4:
            valor = 1.06
        # Muy Alto
        elif self.escala == 5:
            valor = 1.21
        # Extra Alto
        elif self.escala == 6:
            valor = 1.56
        return valor

    def virt(self):
        valor = 1
        # Muy bajo
        if self.escala == 1:
            valor = 1
        # Bajo
        elif self.escala == 2:
            valor = 0.87
        # Nominal
        elif self.escala == 3:
            valor = 1
        # Alto
        elif self.escala == 4:
            valor = 1.15
        # Muy Alto
        elif self.escala == 5:
            valor = 1.30
        # Extra Alto
        elif self.escala == 6:
            valor = 1
        return valor

    def turn(self):
        valor = 1
        # Muy bajo
        if self.escala == 1:
            valor = 1
        # Bajo
        elif self.escala == 2:
            valor = 0.87
        # Nominal
        elif self.escala == 3:
            valor = 1
        # Alto
        elif self.escala == 4:
            valor = 1.07
        # Muy Alto
        elif self.escala == 5:
            valor = 1.15
        # Extra Alto
        elif self.escala == 6:
            valor = 1
        return valor

# Atributos Personal
    def acap(self):
        valor = 1
        # Muy bajo
        if self.escala == 1:
            valor = 1.46
        # Bajo
        elif self.escala == 2:
            valor = 1.19
        # Nominal
        elif self.escala == 3:
            valor = 1
        # Alto
        elif self.escala == 4:
            valor = 0.86
        # Muy Alto
        elif self.escala == 5:
            valor = 1.71
        # Extra Alto
        elif self.escala == 6:
            valor = 1
        return valor

    def aexp(self):
        valor = 1
        # Muy bajo
        if self.escala == 1:
            valor = 1.29
        # Bajo
        elif self.escala == 2:
            valor = 1.13
        # Nominal
        elif self.escala == 3:
            valor = 1
        # Alto
        elif self.escala == 4:
            valor = 0.91
        # Muy Alto
        elif self.escala == 5:
            valor = 1.82
        # Extra Alto
        elif self.escala == 6:
            valor = 1
        return valor

    def pcap(self):
        valor = 1
        # Muy bajo
        if self.escala == 1:
            valor = 1.42
        # Bajo
        elif self.escala == 2:
            valor = 1.17
        # Nominal
        elif self.escala == 3:
            valor = 1
        # Alto
        elif self.escala == 4:
            valor = 1.86
        # Muy Alto
        elif self.escala == 5:
            valor = 1.70
        # Extra Alto
        elif self.escala == 6:
            valor = 1
        return valor

    def vexp(self):
        valor = 1
        # Muy bajo
        if self.escala == 1:
            valor = 1.21
        # Bajo
        elif self.escala == 2:
            valor = 1.10
        # Nominal
        elif self.escala == 3:
            valor = 1
        # Alto
        elif self.escala == 4:
            valor = 0.90
        # Muy Alto
        elif self.escala == 5:
            valor = 1
        # Extra Alto
        elif self.escala == 6:
            valor = 1
        return valor

    def lexp(self):
        valor = 1
        # Muy bajo
        if self.escala == 1:
            valor = 1.14
        # Bajo
        elif self.escala == 2:
            valor = 1.07
        # Nominal
        elif self.escala == 3:
            valor = 1
        # Alto
        elif self.escala == 4:
            valor = 0.95
        # Muy Alto
        elif self.escala == 5:
            valor = 1
        # Extra Alto
        elif self.escala == 6:
            valor = 1
        return valor

    # Atributos de proyecto
    def modp(self):
        valor = 1
        # Muy bajo
        if self.escala == 1:
            valor = 1.24
        # Bajo
        elif self.escala == 2:
            valor = 1.10
        # Nominal
        elif self.escala == 3:
            valor = 1
        # Alto
        elif self.escala == 4:
            valor = 0.91
        # Muy Alto
        elif self.escala == 5:
            valor = 0.82
        # Extra Alto
        elif self.escala == 6:
            valor = 1
        return valor

    def tool(self):
        valor = 1
        # Muy bajo
        if self.escala == 1:
            valor = 1.24
        # Bajo
        elif self.escala == 2:
            valor = 1.10
        # Nominal
        elif self.escala == 3:
            valor = 1
        # Alto
        elif self.escala == 4:
            valor = 0.91
        # Muy Alto
        elif self.escala == 5:
            valor = 0.83
        # Extra Alto
        elif self.escala == 6:
            valor = 1
        return valor

    def sced(self):
        valor = 1
        # Muy bajo
        if self.escala == 1:
            valor = 1.22
        # Bajo
        elif self.escala == 2:
            valor = 1.08
        # Nominal
        elif self.escala == 3:
            valor = 1
        # Alto
        elif self.escala == 4:
            valor = 1.04
        # Muy Alto
        elif self.escala == 5:
            valor = 1.10
        # Extra Alto
        elif self.escala == 6:
            valor = 1
        return valor




