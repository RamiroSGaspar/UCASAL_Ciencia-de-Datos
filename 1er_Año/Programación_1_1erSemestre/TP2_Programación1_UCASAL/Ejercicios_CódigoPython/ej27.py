'''
Universidad Católica de Salta
Programación 1 - 1er Semestre
TP1
autor: Gaspar Ramiro Sebastian

ej 27:
Dada una lista de 10 números ingresados por el usuario, calcular y
mostrar:
a) La suma de todos los números pares.
b) El producto de todos los números impares.
'''
i = 1
numP = 0
numI = 1

print("Ingresa 10 números a continuación")

while i <= 10: 
    numero = int(input("Ingresa un número: "))
    
    if numero % 2 == 0:
        numP += numero
    else:
        numI *= numero
    i += 1

print("La suma total de los números pares:", numP)
print("El total del producto de los impares:", numI)