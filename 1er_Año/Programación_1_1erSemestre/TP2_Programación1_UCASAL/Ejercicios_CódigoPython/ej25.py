'''
Universidad Católica de Salta
Programación 1 - 1er Semestre
TP1
autor: Gaspar Ramiro Sebastian

ej 25:
Solicitar 5 números al usuario. Luego mostrar: la suma total de todos
los números y el producto de todos los números.
'''
i = 1
ac = 0
ac2 = 1
print("Ingresa cinco numeros")

while i <= 5:
    
    numero = int(input("Ingresa un numero: "))
    
    ac += numero
    ac2 *= numero
    i += 1

print("Sumando todos los numeros ingresados da: ", ac)
print("Multiplicando todos los numeros ingresados da: ", ac2)
    