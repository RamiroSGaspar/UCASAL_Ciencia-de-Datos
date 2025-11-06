'''
Universidad Católica de Salta
Programación 2 - 2ndo Semestre
TP2
autor: Gaspar Ramiro Sebastian

Ej2:
Solicitar al usuario el ingreso de dos números enteros. Calcular (utilizando
distintas variables), su suma, resta, multiplicación y división. Mostrar por
pantalla el resultado de cada una de las operaciones realizadas. Por ej. si el
usuario ingresó 4 y 7. Mostrar “El resultado de multiplicar 4 x 7 es 28”.
'''
print("--Programa para probar los operadores aritmetico basicos--")
n1 = int(input("Ingresa un numero entero: "))
n2 = int(input("Ingresa el siguiente numero entero: "))

suma = n1 + n2
resta = n1 - n2
multiplicacion = n1 * n2
division = n1 / n2
# division_entera = n1 // n2
# moduulo_o_resto = n1 % n2
# exponente = n1 ** n2

print(f""" 
El resultado de la suma {n1} + {n2} es {suma} 
El resultado de la resta {n1} - {n2} es {resta}
El resultado de multiplicar {n1} x {n2} es {multiplicacion}
El resultado de dividir {n1} / {n2} es {division}
      """)
