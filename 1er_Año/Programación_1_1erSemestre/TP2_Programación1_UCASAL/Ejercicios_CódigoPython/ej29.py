'''
Universidad Católica de Salta
Programación 1 - 1er Semestre
TP1
autor: Gaspar Ramiro Sebastian

ej 29:
Dada una lista de 10 números ingresados por el usuario, calcular y
mostrar:
a) La cantidad de números múltiplos de 4.
b) La cantidad de números múltiplos de 2.
c) La cantidad de números positivos.
d) La cantidad de números negativos.
'''
i = 1
mult4 = []
mult2 = []  
positivos = [] 
negativos = []

print("Ingresa diez números a continuación")

while i <= 10:
    numero = int(input("Ingresa un número: "))
    
    if numero % 4 == 0:
        mult4.append(numero)
    if numero % 2 == 0:
        mult2.append(numero)
    if numero >= 0:
        positivos.append(numero)
    if numero < 0:
        negativos.append(numero)
    i += 1

print("\nMúltiplos de 4:", mult4)
print("Múltiplos de 2 (no de 4):", mult2)
print("Positivos no múltiplos de 2 o 4:", positivos)
print("Negativos:", negativos)