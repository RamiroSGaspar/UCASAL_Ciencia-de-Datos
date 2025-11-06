'''
Universidad Católica de Salta
Programación 2 - 2ndo Semestre
TP3
autor: Gaspar Ramiro Sebastian

Ej 9
Solicitar el ingreso de dos números y mostrar:
a. Cuál de los dos números es mayor.
b. Verifique si el primer número es positivo, negativo o cero.
c. Verifique si el segundo número es mayor a 0 y menor a 100.
'''

n1 = float(input("Ingresa el primer numero: "))
n2 = float(input("Ingresa el segundo numero: "))

print("¿Cual es el mayor entre los dos numeros?")
if n1 < n2: print(f"El segundo numero {n2} es el mayor")
elif n1 == n2: print("Ambos numeros son iguales")
else: print(f"El primer numero {n1} es el mayor")

print("\n¿El primer numero es positivo, negativo o cero?")
if n1 < 0: print(f"El primer numero {n1} es negativo")
elif n1 > 0: print(f"El primer numero {n1} es positivo")
elif n1 == 0: print("Es igual a cero el primer numero")

print("¿El segundo numero es mayor que 0 y menor que 100?")
if n2 > 0 and n2 < 100: print(f"El segundo numero {n2} es mayor a 0 y menor que 100")
else: print(f"{n2} No cumple con las dos condiciones")
