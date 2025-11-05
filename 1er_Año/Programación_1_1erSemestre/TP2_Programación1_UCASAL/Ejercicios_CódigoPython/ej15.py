'''
Universidad Católica de Salta
Programación 1 - 1er Semestre
TP1
autor: Gaspar Ramiro Sebastian

ej 15:
Escribir un programa que funcione como un examen tipo múltiple de
Choice. Pregunte al usuario: “¿Qué color se genera mezclando azul y
amarillo?” y muestre las opciones “1- Rojo; 2- Violeta; 3- Verde; 4- Negro”.
Luego de recibida la respuesta muestre el mensaje de “Respuesta
Correcta” o “Respuesta incorrecta” según corresponda. (Utilice la
estructura Según - de Selección Múltiple).
'''
print("¿Qué color se genera mezclando azul y amarillo?")
print("1- Rojo\n2- Violeta\n3- Verde\n4- Negro")

opcion = int(input("Ingrese el número de la opción correcta: "))

if opcion == 3:
    print("Respuesta Correcta")
else:
    print("Respuesta incorrecta")