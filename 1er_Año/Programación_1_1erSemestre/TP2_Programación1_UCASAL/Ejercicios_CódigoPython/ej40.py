'''
Universidad Católica de Salta
Programación 1 - 1er Semestre
TP1
autor: Gaspar Ramiro Sebastian

ej 40:
Mostrar los números impares del 60 al 30 en forma descendente.
'''
for i in range(60, 29, -1):
    if i % 2 != 0:
        print(i)