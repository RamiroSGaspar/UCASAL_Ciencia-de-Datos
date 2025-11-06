'''
Universidad Católica de Salta
Programación 2 - 2ndo Semestre
TP4
autor: Gaspar Ramiro Sebastian

Ej 11:
Dado el siguiente array numpy: [1, 5, -2, 10, 2], realizar las siguientes
operaciones:
a. Suma
b. Promedio
c. Ordenarlo
Mostrar todos los resultados.
'''
import numpy as np

array = np.array([1,5,-2,10,2])

suma = np.sum(array)
promedio = np.average(array)
ordenado = np.sort(array)

print(f"""
El array es este: {array}
La suma de todos sus numeros da: {suma}
El promedio es: {promedio}
El array ordenado es: {ordenado}
      """)