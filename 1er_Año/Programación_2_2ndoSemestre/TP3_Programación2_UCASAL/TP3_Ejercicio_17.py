'''
Universidad Católica de Salta
Programación 2 - 2ndo Semestre
TP3
autor: Gaspar Ramiro Sebastian

Ej 17
Mostrar la tabla de multiplicar del 6 (Ej. 6x1=6; 6x2=12; 6x3=18, etc. hasta 6x10)
'''
print("--Tabla del 6--")
n = 6
for i in range(1,11):
    # n = 6
    mult = i * n
    print(f"{n} x {i} = {mult}")