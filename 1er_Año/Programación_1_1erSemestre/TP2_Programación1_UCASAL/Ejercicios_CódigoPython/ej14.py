'''
Universidad Católica de Salta
Programación 1 - 1er Semestre
TP1
autor: Gaspar Ramiro Sebastian

ej 14:
Escribir un programa que solicite al usuario el ingreso de una
temperatura en escala Fahrenheit (debe permitir decimales), y luego por
pantalla el equivalente en grados Celsius. La fórmula de conversión que se
usa para este cálculo es: Celsius = (5/9) * (Fahrenheit-32).
'''

F = int(input("Ingresa temperatura en escala Fahrenheit: "))
C = (5/9) * (F-32)

print(f"Los conversion de Fahrenheit {F} a celisius da {C}")