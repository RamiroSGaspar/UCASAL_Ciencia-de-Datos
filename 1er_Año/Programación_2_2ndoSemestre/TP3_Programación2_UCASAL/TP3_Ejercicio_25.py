'''
Universidad Católica de Salta
Programación 2 - 2ndo Semestre
TP3
autor: Gaspar Ramiro Sebastian

Ej 25
Dada una lista de 10 números ingresados por el usuario, calcular y mostrar:
a) La suma de todos los números múltiplos de 3.
b) El producto de todos los números múltiplos de 5.
'''
import math
numeros = []
numeros_m3 = []
numeros_m5 = []

for i in range(1,11):
    num = int(input("Ingresa un numero: "))
    numeros.append(num)
    if num % 3 == 0: numeros_m3.append(num)
    if num % 5 == 0: numeros_m5.append(num)

suma_m3 = sum(numeros_m3)
if numeros_m5: prod_m5 = math.prod(numeros_m5)
else: prod_m5 = 0

print(f"""
Los numeros ingresados: {numeros}
La suma de los multiplos de 3: {suma_m3}
El producto de todos los numeros multiplos de 5: {prod_m5}
      """)