'''
Universidad Católica de Salta
Programación 1 - 1er Semestre
TP1
autor: Gaspar Ramiro Sebastian

ej 44:
Dado el nombre de una persona y un número N ingresados por el
usuario, mostrarlo N veces seguidas, tanto el nombre como su repetición.
Por Ej: Ana 1, Ana 2, Ana 3.
'''

cantidad = int(input("Ingresa una cantidad: "))
nombre = input("Ingresa tu nombre: ")

for i in range(1, cantidad + 1):
    print(f"{nombre} {i}")