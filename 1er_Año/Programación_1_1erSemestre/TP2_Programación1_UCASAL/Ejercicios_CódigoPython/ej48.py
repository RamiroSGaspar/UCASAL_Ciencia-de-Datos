'''
Universidad Católica de Salta
Programación 1 - 1er Semestre
TP1
autor: Gaspar Ramiro Sebastian

ej 48:
Dada una lista de 10 números ingresados por el usuario, calcular y
mostrar:
a) La suma de todos los números pares.
b) El producto de todos los números impares.
'''
numP = 0
numI = 1

print("Ingresa diez numeros acontinuacion: ")
for i in range(1, 11):
    
    numero = int(input("Ingresa un numero: "))
    
    if numero % 2 == 0:
        numP += numero
    elif numero % 2 != 0:
        numI *= numero

print("La suma total de todos los numeros pares ingresados: ", numP)
print("El producto total de todos los numeros impares ingresados: ",numI)