'''
Universidad Católica de Salta
Programación 2 - 2ndo Semestre
TP4
autor: Gaspar Ramiro Sebastian

Ej 12:
Crear un array a partir de una lista: l1 = list(range(10)).
Luego, usando where:

a) Crear un nuevo array que solo tengo los números mayores a 3 del array numy
y los demás reemplazar por cero.
b) Crear un nuevo array que solo tengo los números pares del array numy y los
demás reemplazar por cero.
Mostrar todos los resultados.
'''
import numpy as np

lista = list(range(10))
array = np.array(lista)

array_1 = np.where(array > 3, array, 0)
array_2 = np.where(array % 2 == 0, array, 0)

print(f"""
El array original: {array}
array solo con numeros mayores a 3 (resto reemplazado con 0): {array_1}
array con numeros pares (el resto reemplazado con 0): {array_2}
      """)