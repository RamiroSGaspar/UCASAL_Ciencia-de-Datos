'''
Universidad Católica de Salta
Programación 1 - 1er Semestre
TP1
autor: Gaspar Ramiro Sebastian

ej 23:
Dado el nombre de una persona y un número N ingresados por el
usuario, mostrarlo N veces seguidas, tanto el nombre como su repetición.
Por Ej: Ana 1, Ana 2, Ana 3.
'''
nombre = input("Ingresa tu nombre: ")
n = int(input("Ingresa un numero: "))

i = 0

while i <= n:
    print(f"{nombre} {i}")
    i += 1