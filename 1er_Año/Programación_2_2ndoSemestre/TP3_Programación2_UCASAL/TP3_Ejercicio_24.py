'''
Universidad Católica de Salta
Programación 2 - 2ndo Semestre
TP3
autor: Gaspar Ramiro Sebastian

Ej 24
Dada una lista de 10 números ingresados por el usuario, calcular y mostrar:
a) La suma de todos los números pares.
b) El producto de todos los números impares.
'''
import math
numeros = []
numeros_pares = []
numeros_impares = []

for i in range(1, 11):
    num = int(input("Ingresa un numero: "))
    numeros.append(num)
    if num % 2 == 0: numeros_pares.append(num)
    elif num % 2 != 0: numeros_impares.append(num)

suma_pares = sum(numeros_pares)
prod_impares = math.prod(numeros_impares)

print(f"""
Los numeros ingresados: {numeros}
La suma de todos los numeros pares: {suma_pares}
El producto de todos los numeros impares: {prod_impares}
      """)