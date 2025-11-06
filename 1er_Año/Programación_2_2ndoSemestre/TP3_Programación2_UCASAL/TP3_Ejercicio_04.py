'''
Universidad Católica de Salta
Programación 2 - 2ndo Semestre
TP3
autor: Gaspar Ramiro Sebastian

Ej 4
Escribir un programa que solicite el ingreso de una letra, luego valide si es una
vocal, mostrando el mensaje “Es vocal” o “No es vocal”. 
'''
print("--Programa para deteriminar si una letra ingresada es vocal o no--")
letra = input("Ingresa una letra: ").upper()
if letra in ("A", "E", "I", "O", "U"): print(f"{letra} es una vocal")
else: print(f"{letra} no es una vocal")