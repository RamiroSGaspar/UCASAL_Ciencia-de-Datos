'''
Universidad Católica de Salta
Programación 1 - 1er Semestre
TP1
autor: Gaspar Ramiro Sebastian

ej 12:
Escribir un programa que solicite un número entero y luego muestre
por pantalla si el número es par o no. Recordar que un número es par si al
dividirlo por 2, su resto es igual 0.
'''
numero = int(input("Ingresa un numero entero: "))
calculo = numero % 2

if calculo == 0:
    print("Es un numero par")
else:
    print("Es un numero impar")