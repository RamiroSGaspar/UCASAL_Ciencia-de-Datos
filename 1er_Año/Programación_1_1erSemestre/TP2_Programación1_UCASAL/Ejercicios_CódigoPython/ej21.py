'''
Universidad Católica de Salta
Programación 1 - 1er Semestre
TP1
autor: Gaspar Ramiro Sebastian

ej 21:
Mostrar los múltiplos de 5 desde el 1 al 100. (usar mod).
'''
i = 1
while i <= 100:
    if i % 5 == 0:
        print(i)
    i += 1