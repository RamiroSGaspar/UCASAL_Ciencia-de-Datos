'''
Universidad Católica de Salta
Programación 2 - 2ndo Semestre
TP2
autor: Gaspar Ramiro Sebastian

Ej8.
Solicitar al usuario el ingreso de la BASE y la ALTURA de un triángulo, calcular y
mostrar el área del triángulo. 
'''
print("--Programa para calcular el area de un triangulo--")
base = float(input("Ingresa el valor de la base: "))
altura = float(input("Ingresa el valor de la alutra: "))
area = (base * altura) / 2
print("El area del triangulo es: ", area)