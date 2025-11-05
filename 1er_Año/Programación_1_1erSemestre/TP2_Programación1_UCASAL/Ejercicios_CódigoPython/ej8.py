'''
Universidad Católica de Salta
Programación 1 - 1er Semestre
TP1
autor: Gaspar Ramiro Sebastian

Ej 8:
Solicitar al usuario el ingreso de la nota del Examen. Luego mostrar
“Promocionado” (7 a 10), “Regular” (4 a 6) o “Libre” (0 a 3) según la nota
ingresada.
'''

print("--Programa para calificar la nota de examen--")

nota = int(input("Ingresa la nota a calificar: "))
if nota >= 0:
    if nota >= 7:
        print(f"Promocionado con nota {nota}")
    elif nota >= 4 and nota <=6:
        print(f"Regular con nota {nota}")
    elif nota <= 3:
        print(f"Libre con nota {nota}")