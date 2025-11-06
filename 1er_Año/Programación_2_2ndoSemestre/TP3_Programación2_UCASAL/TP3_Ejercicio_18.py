'''
Universidad Católica de Salta
Programación 2 - 2ndo Semestre
TP3
autor: Gaspar Ramiro Sebastian

Ej 18
Mostrar los múltiplos de 5 desde el 1 al 100. (usar mod)
'''
print("--Multiplos del 5 desde el 1 hasta el 100--")
print("Multiplos de 5")
for i in range(1, 101):
    if i % 5 == 0: print(i)
