'''
Universidad Católica de Salta
Programación 2 - 2ndo Semestre
TP3
autor: Gaspar Ramiro Sebastian

Ej 21
Mostrar todas las tablas de multiplicar del 1 al 10, con un subtítulo entre cada
tabla separando las mismas. Ej: “Tabla del 1; 1x1=1; 1x2=2;1x3=3…1x10=10;
Tabla del 2; 2x1=2; 2x2=4….
'''
print("--Tablas de multiplicar del 1 al 10--")
c = 0
for i in range(1,11):
    print(f"\nTabla de {i}:\n")
    for j in range (1,11):
        mult = j * i
        print(f"{j} x {i} = {mult}")