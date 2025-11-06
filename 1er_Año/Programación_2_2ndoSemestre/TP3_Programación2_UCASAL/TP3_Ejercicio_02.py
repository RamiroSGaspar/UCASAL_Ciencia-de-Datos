'''
Universidad Católica de Salta
Programación 2 - 2ndo Semestre
TP3
autor: Gaspar Ramiro Sebastian

Ej2:
Escribir un programa que solicite un número, luego le reste el 15%, almacenando
todo en una única variable. A continuación, mostrar el resultado final por
pantalla. 
'''
print("--Programa para restar el 15% a un numero ingresado--")
num = float(input("Ingresa un numero: "))
print("Numero Ingresado: ",num)

num = num - (15 / 100)* num
print("Resultado: ",num)
