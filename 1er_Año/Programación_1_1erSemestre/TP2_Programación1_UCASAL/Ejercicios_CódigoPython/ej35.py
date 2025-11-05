'''
Universidad Católica de Salta
Programación 1 - 1er Semestre
TP1
autor: Gaspar Ramiro Sebastian

ej 35:
Mostrar los múltiplos de 5 desde el 1 al 100. (usar mod)
'''
i = 1  
print("Los múltiplos de 5 entre 1 y 100 son:")  

while True:  
    if i % 5 == 0:  
        print(i)  
    i += 1  
    if i > 100:  
        break  