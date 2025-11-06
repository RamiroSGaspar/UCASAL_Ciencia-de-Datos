'''
Universidad Católica de Salta
Programación 2 - 2ndo Semestre
TP3
autor: Gaspar Ramiro Sebastian

Ej 22
Solicitar 5 números al usuario. Luego mostrar: la suma total de todos los números
y el producto de todos los números.
'''
import math

numeros = []
for i in range(1,6):
    n = float(input("Ingresa un numero: "))
    numeros.append(n)

suma = sum(numeros)
producto = math.prod(numeros)

print(f"""
Estos son los numeros dentro de la lista: {numeros}
La suma entre ellos da: {suma}
Y el producto entre ellos da: {producto}
      """)
