'''
Universidad Católica de Salta
Programación 1 - 1er Semestre
TP1
autor: Gaspar Ramiro Sebastian

ej 11:
Escribir un programa que solicite un número, luego le reste el 15%,
almacenando todo en una única variable. A continuación, mostrar el
resultado final por pantalla.
'''

numero = float(input("Ingrese un número: "))
numero *= 0.85 
print(f"El resultado después de restar el 15% es: {numero:.2f}")