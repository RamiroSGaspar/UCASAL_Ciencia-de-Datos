'''
Universidad Católica de Salta
Programación 1 - 1er Semestre
TP1
autor: Gaspar Ramiro Sebastian

ej 36:
Desde un número N y otro P ingresados por el usuario, mostrar todos
los números desde P hasta N. (suponer que P es mayor que N)
'''
N = int(input("Ingresa N: "))  
P = int(input("Ingresa P (mayor que N): "))  

i = P  
while True:  
    print(i)  
    i -= 1  
    if i < N:  
        break  