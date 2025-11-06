'''
Universidad Católica de Salta
Programación 2 - 2ndo Semestre
TP2
autor: Gaspar Ramiro Sebastian

Ej6.
Solicitar al usuario el ingreso de dos números, calcular y mostrar el promedio de
ambos valores. 
'''
print("--Programa para calcular el promedio entre dos numeros--")
n1 = float(input("Ingresa el primer numero: "))
n2 = float(input("Ingresa el segundo numero: "))

suma = n1 + n2
promedio = suma / 2
print("El promedio entre los dos numeros ingresados es: ", promedio)