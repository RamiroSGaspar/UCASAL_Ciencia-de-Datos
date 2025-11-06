'''
Universidad Católica de Salta
Programación 2 - 2ndo Semestre
TP3
autor: Gaspar Ramiro Sebastian

Ej 11
Realice un programa que solicite el ingreso de tres números enteros, y luego en
cada caso informe si el número es par o impar.
'''
print("--Programa para verificar si tres numerso ingresados y verificar si cada uno es par o impar--")
n1 = int(input("Ingresa el primer numero entero: "))
n2 = int(input("Ingresa el segundo numero entero: "))
n3 = int(input("Ingresa el tercer numero entero: "))

numeros = [n1, n2, n3]

for num in numeros:
    if num % 2 == 0: print(f"El numero {num} es par")
    else: print(f"El numero {num} es impar")
    
