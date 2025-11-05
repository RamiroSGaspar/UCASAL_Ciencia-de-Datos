'''
Universidad Católica de Salta
Programación 1 - 1er Semestre
TP1
autor: Gaspar Ramiro Sebastian

Ej 6:
Solicitar al usuario el ingreso de su edad. Luego mostrar por pantalla:
“Eres mayor de edad” o “No eres mayor de edad” según la edad ingresada
(18 años cumplidos para ser mayor de edad).
'''
print("Programa para indicar si el usuario es mayor de edad.")
edad = int(input("Ingresa tu edad: "))

if edad > 18:
    print(f"el usuario es mayor de edad con {edad} años")
else:
    print(f"el usuario es menor de edad con {edad} años")