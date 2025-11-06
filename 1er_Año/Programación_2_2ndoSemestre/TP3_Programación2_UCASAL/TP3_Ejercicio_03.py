'''
Universidad Católica de Salta
Programación 2 - 2ndo Semestre
TP3
autor: Gaspar Ramiro Sebastian

Ej3:
Escribir un programa que solicite un número entero y luego muestre por pantalla
si el número es par o no. (Usar función resto/modulo) 
'''
print("--Programa para calcular si un numero entero es par o impar--")
num = int(input("Ingresa un numero entero: "))
if num % 2 == 0 : print(f"El numero ingresado {num} es par")
else: print(f"El numero ingresado {num} es impar")
