'''
Universidad Católica de Salta
Programación 1 - 1er Semestre
TP1
autor: Gaspar Ramiro Sebastian

ej 45:
Mostrar todas las tablas de multiplicar del 1 al 10, con un subtítulo entre
cada tabla separando las mismas. Ej: “Tabla del 1; 1x1=1;1x2=2;1x3=3…1x10=10;
Tabla del 2; 2x1=2; 2x2=4….
'''
print("Tablas del 1 al 10")
for tabla in range(1, 11):
    
    multiplicador = 1
    print(f"tabla del {tabla}:")
    
    for i in range(1, 11):
        r = tabla * multiplicador
        print(f"{tabla} x {multiplicador} = {r}")
        multiplicador += 1

    print(" ")
    
    