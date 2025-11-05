'''
Universidad Católica de Salta
Programación 1 - 1er Semestre
TP1
autor: Gaspar Ramiro Sebastian

ej 41:
Mostrar la tabla de multiplicar del 6 (Ej. 6x1=6; 6x2=12; 6x3=18, etc.)
'''

print("Tabla del 6: ")

for tabla in range(0, 11):
    multiplicacion = tabla * 6
    print(f"{tabla} x 6 = {multiplicacion}")
    