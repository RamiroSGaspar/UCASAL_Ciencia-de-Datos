'''
Universidad Católica de Salta
Programación 2 - 2ndo Semestre
TP3
autor: Gaspar Ramiro Sebastian

Ej 15
Mostrar los números pares entre 10 y 40 en forma ascendente.
'''
print("-- Numeros pares entre 10 y 40 --")
print("Los numeros pares: ")
for i in range(10, 41):
    if i % 2 == 0: print(i)
    else: None
