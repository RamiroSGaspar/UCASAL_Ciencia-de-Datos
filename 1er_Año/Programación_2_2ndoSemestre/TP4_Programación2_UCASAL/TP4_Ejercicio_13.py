'''
Universidad Católica de Salta
Programación 2 - 2ndo Semestre
TP4
autor: Gaspar Ramiro Sebastian

Ej 13:
Crear un array numpy: [1, 2, 4, 7]. Luego:
a. Crear la máscara para solo quedarnos con los números mayores a 1.
b. Crear la máscara para solo quedarnos con los números pares.
Mostrar todos los resultados.
'''
import numpy as np

array = np.array([1, 2, 4, 7])

def mascara_1(array):
    mascara1 = array > 1
    rto = array[mascara1]
    return rto, mascara1

def mascara_2(array):
    mascara2 = array % 2 == 0
    rto = array[mascara2]
    return rto, mascara2

rto, mascara = mascara_1(array)
rto2, mascara2 = mascara_2(array)

print(f"""
Array original: {array}
Con la mascara 1 (numeros mayores a 1): {mascara}
Array filtrado: {rto}

Con la mascara 2 (numeros pares): {mascara2}
Array filtrado: {rto2}
      """)