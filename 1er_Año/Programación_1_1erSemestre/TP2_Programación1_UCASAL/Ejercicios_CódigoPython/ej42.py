'''
Universidad Católica de Salta
Programación 1 - 1er Semestre
TP1
autor: Gaspar Ramiro Sebastian

ej 42:
Mostrar los múltiplos de 5 desde el 1 al 100. (usar mod)
'''
print("Tabla del 5")

for tabla in range(0, 101):
    
    if tabla % 5 == 0:
        print(tabla)