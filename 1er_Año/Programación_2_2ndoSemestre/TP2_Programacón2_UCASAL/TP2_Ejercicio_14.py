'''
Universidad Católica de Salta
Programación 2 - 2ndo Semestre
TP2
autor: Gaspar Ramiro Sebastian

Ej. 14
Realice un programa que solicite al usuario el ingreso de un nombre completo.
Luego lo muestre por pantalla en los siguientes formatos:
a. Todas las letras en minúsculas
b. Todas las letras en mayúsculas
c. Solo la primera letra del nombre en mayúscula 
'''
apellido = input("Ingresa tu apelldio: ")
nombre = input("Ingresa tu nombre: ")
a = apellido.lower() + " " + nombre.lower()
b = apellido.upper() + " " + nombre.upper()
c = apellido[0].upper() + apellido[1:].lower() + " " + nombre[0].upper() + nombre[1:].lower()

print(f"""
El Nombre completo con todas las letras en minusculas: {a}
El Nombre completo con todas las letras en mayusculas: {b}
El Nombre completo con las primeras letras en mayusculas: {c} 
      """)