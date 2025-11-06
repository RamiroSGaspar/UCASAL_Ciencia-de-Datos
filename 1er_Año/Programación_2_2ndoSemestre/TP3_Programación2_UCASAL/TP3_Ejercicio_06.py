'''
Universidad Católica de Salta
Programación 2 - 2ndo Semestre
TP3
autor: Gaspar Ramiro Sebastian

Ej 6
Escribir un programa que solicite al usuario el ingreso de una temperatura en
escala Fahrenheit (debe permitir decimales), y luego muestre por pantalla el
equivalente en grados Celsius. La fórmula de conversión que se usa para este
cálculo es: Celsius = (5/9) * (Fahrenheit-32). 
'''
print("--Programa para sacar el equivalente de °F a °C--")

Fahrenheit = float(input("Ingresa la temperatura en Fahrenheit:  "))
Celsius = (5/9) * (Fahrenheit -32)

print(f"La temperatura en {Fahrenheit}°F es equivalente a {Celsius}°C ")