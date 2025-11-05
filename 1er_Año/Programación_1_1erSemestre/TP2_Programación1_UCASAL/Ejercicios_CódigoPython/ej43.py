'''
Universidad Católica de Salta
Programación 1 - 1er Semestre
TP1
autor: Gaspar Ramiro Sebastian

ej 43:
Desde un número N y otro P ingresados por el usuario, mostrar todos
los números desde N hasta P. (suponer que P es mayor que N)
'''

N = int(input("Ingresa N: "))
P = int(input("Ingresa P (mayor que N): "))

if N < P:
    for i in range(N + 1, P):
        print(i)