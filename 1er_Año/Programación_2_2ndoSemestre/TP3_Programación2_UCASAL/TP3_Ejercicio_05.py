'''
Universidad Católica de Salta
Programación 2 - 2ndo Semestre
TP3
autor: Gaspar Ramiro Sebastian

Ej 5
 Escribir un programa que solicite el ingreso de 3 números. Luego muestre por
pantalla:
- La suma de los números
- El promedio de los números
- La multiplicación de los 3 números
(Todo en un mismo programa) 
'''

n1 = float(input("Ingresa el primer numero: "))
n2 = float(input("Ingresa el segundo numero: "))
n3 = float(input("Ingresa el tercer numero: "))

suma = n1 + n2 + n3
promedio = suma / 3
multiplicacion = n1 * n2 * n3

print(f"""
La suma entre los numeros es: {suma}
El promedio entre los numeros es: {promedio}
La multiplicacion entre los numeros da como resultado: {multiplicacion}
      """)