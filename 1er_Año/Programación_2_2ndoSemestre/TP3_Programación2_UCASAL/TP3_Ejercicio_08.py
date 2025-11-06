'''
Universidad Católica de Salta
Programación 2 - 2ndo Semestre
TP3
autor: Gaspar Ramiro Sebastian

Ej 8
Solicitar al usuario el ingreso de la nota del Examen. Luego mostrar por pantalla:
a. “Sobresaliente! Felicitaciones!” (nota 10)
b. “Promocionado! Bravo!” (7 a 9)
c. “Aprobado. Bien pero a poner más empeño!” (4 a 6)
d. “Desaprobado. Prepararse para el recuperatorio!” (0 a 3)
'''
print("--Programa para clasificar la nota--")
while True:
    nota = int(input("Ingresa la nota (del 0 al 10): "))

    if 0 <= nota <= 10:    
        match nota:
            case 10: print("Sobresaliente! Felicitaciones!")
            case 7 | 8 | 9: print("Promocionado! Bravo!")
            case 4 | 5 | 6: print("Aprobado. Bien pero a poner más empeño!")
            case 0 | 1 | 2 | 3: print("Desaprobado. Prepararse para el recuperatorio!")
        break   
    else:
        print("Error: Ingresa una nota válida (0 a 10)\n")
