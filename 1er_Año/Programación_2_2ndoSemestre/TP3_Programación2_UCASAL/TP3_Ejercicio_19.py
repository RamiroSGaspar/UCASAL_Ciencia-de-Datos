'''
Universidad Católica de Salta
Programación 2 - 2ndo Semestre
TP3
autor: Gaspar Ramiro Sebastian

Ej 19
Desde un número N y otro P ingresados por el usuario, mostrar todos los
números desde N hasta P. (suponer que P es mayor que N)
'''

N = int(input("Ingresa un numero: "))
P = int(input("Ingresa otro numero: "))

if N < P:
    for i in range(N, P + 1):
        print(i)
else: print("Error: El segundo numero debe ser mayor que el primero")



                    



