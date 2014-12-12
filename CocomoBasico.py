#!/usr/bin/phython
# coding=utf-8
from SoftwareProject import SoftwareProject

__author__ = 'gsv'

sp = SoftwareProject()
class CocomoBasico(object):

    def test(self):
        print("hello world")

    # sp = SoftwareProject()

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
        E = (sp.a * kloc) ** sp.b
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
        E = (sp.a * kloc) ** sp.b
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
        E = (sp.a * kloc) ** sp.b
        D = (sp.c * E) ** sp.d
        P = E / D
        print("=" * 50 +
              "\nEsfuerzo (personas/mes):\n " + str(E) +
              "\nDuracion (meses):\n " + str(D) +
              "\nPersonal (recomendado)): \n" + str(P)+"\n"+
              "=" * 50)

