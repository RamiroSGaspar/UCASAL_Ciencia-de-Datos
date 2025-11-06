'''
Universidad Católica de Salta
Programación 2 - 2ndo Semestre
TP2
autor: Gaspar Ramiro Sebastian

Ej. 13
-Realice un programa que solicite al usuario el nombre completo de la persona,
el DNI de la persona, la edad de la persona y la altura de la persona. Luego el
programa debe mostrar por pantalla dos líneas de texto por separado:

a. En una línea imprimir el nombre completo y el DNI, aclarando de que
campo se trata cada uno. Por ej.: Nombre Completo: Elena Lobo, DNI:
38041532.

b. En la segunda línea se debe imprimir el nombre completo, edad y altura
de la persona. Nuevamente debe aclarar el campo de cada uno, para el
que lo lea entienda de que se está hablando.
'''
print("--Datos Personales--")
a = input("Ingresa tu apellido: ")
n = input("Ingresa tu nombre: ")
dni = input("Ingresa tu DNI sin puntos y todo junto: ")
edad = int(input("Ingresa tu edad: "))
altura = float(input("Ingresa tu altura (ej: 1.60 , 1.20): "))

# Mayusculas en el nombre completo
apellido = a[0].upper() + a[1:]
nombre = n[0].upper() + n[1:]

if (len(dni) == 8) and (edad < 130 and edad > 0):
    # Salida 1:
    print(f"Nombre Completo {apellido} {nombre}, DNI: {dni}")
    print()
    # Salida 2:
    print(f"Nombre Completo {apellido} {nombre}, Edad: {edad}, Altura: {altura}")
else: print("Error, Alguno de los datos ingresados no son validos")