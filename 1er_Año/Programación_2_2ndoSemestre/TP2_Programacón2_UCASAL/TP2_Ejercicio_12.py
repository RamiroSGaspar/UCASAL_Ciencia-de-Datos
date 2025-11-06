'''
Universidad Católica de Salta
Programación 2 - 2ndo Semestre
TP2
autor: Gaspar Ramiro Sebastian

Ej. 12
Realice una calculadora, el usuario ingresará dos números reales y se deberán
calcular todas las operaciones entre ellos: A) Suma; B) Resta; C) Multiplicación;
D) División; E) Exponente/Potencia. Para todos los casos se debe imprimir en
pantalla el resultado aclarando la operación realizada en cada caso y con que
números se ha realizado la operación. Por ej: “La suma entre 14.1 y 6.4 es 20.5”  
'''
print("--Calculo de dos numeros con varias operaciones--")
n1 = float(input("Ingresa un numero: "))
n2 = float(input("Ingresa otro numero: "))

suma = n1 + n2
resta = n1 - n2
multiplicacion = n1 * n2
division = n1 / n2 if n2 != 0 else "Error: división por cero"
potencia = n1 ** n2

print(f"La suma entre {n1} y {n2} es {suma}")
print(f"La resta entre {n1} y {n2} es {resta}")
print(f"La multiplicación entre {n1} y {n2} es {multiplicacion}")
print(f"La división entre {n1} y {n2} es {division}")
print(f"La potencia de {n1} elevado a {n2} es {potencia}")

# Version de calculadora simple:
'''
print("--Calculadora Simple--")
n1 = float(input("Ingresa un numero: "))
n2 = float(input("Ingresa otro numero: "))

print("""
Para poder realizar calculos tienes que ingresar un numero que peretenece a una opcion:
Estas son las opciones en la calculadora:
1 - Suma (+)
2 - Resta (-)
3 - Multiplicacion (x)
4 - Division (/)
5 - Potencia (^)
      """)
opcion = int(input("Ingresa que quieres hacer: "))

if opcion == 1: salida = n1 + n2
elif opcion == 2: salida = n1 - n2
elif opcion == 3: salida = n1 * n2
elif opcion == 4: salida = n1 / n2
elif opcion == 5: salida = n1 ** n2
else: None

print(salida)
'''