'''
Universidad Católica de Salta
Programación 1 - 1er Semestre
TP1
autor: Gaspar Ramiro Sebastian

ej 34:
Mostrar la tabla de multiplicar del 6 (Ej. 6x1=6; 6x2=12; 6x3=18, etc.)
'''
i = 1  
print("Tabla del 6:")  

while True:  
    print(f"6x{i} = {6 * i}")  
    i += 1  
    if i > 10:  
        break  