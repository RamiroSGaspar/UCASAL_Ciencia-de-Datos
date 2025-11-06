'''
Universidad Católica de Salta
Programación 2 - 2ndo Semestre
TP3
autor: Gaspar Ramiro Sebastian

Ej 20
Dado el nombre de una persona y un número N ingresados por el usuario,
mostrarlo N veces seguidas, tanto el nombre como su repetición. Por Ej: Ana 1,
Ana 2, Ana 3.
'''
nombre = input("Ingresa un nombre: ")
num = int(input("Ingresa un numero: "))
n = nombre[0].upper() + nombre[1:].lower()
for i in range(1,num + 1): print(f"{n} {i}")