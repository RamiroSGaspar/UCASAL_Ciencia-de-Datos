'''
Universidad Católica de Salta
Programación 1 - 1er Semestre
TP1
autor: Gaspar Ramiro Sebastian

Ej 7:
Solicitar al usuario el ingreso de los Nombres, Apellidos y Edades de 2
personas distintas (es decir en total tiene que pedir 6 datos). Luego
mostrar los datos completos por pantalla cuál de ellas tiene más edad o si
son de la misma edad. El mensaje de salida tiene que ser por ejemplo:
“Ana Sánchez tiene mayor edad que Carolina Pérez”; “Carolina Pérez tiene
mayor edad que Ana Sánchez”; “Ana Sánchez y Carolina Pérez tienen la
misma edad”
'''

print("Ingresa los datos de dos personas")

#persona 1
print("--Datos de la primera persona--")
nombre_p1 = input("Ingresa el nombre de la persona: ")
apellido_p1 = input("Ingresa el apellido de la persona: ")
edad_p1 = int(input("Ingresa la edad de la persona: "))

#persona2
print("--Datos de la segunda persona--")
nombre_p2 = input("Ingresa el nombre de la persona: ")
apellido_p2 = input("Ingresa el apellido de la segunda persona: ")
edad_p2 = int(input("Ingresa la edad de la persona:"))

if edad_p1 < edad_p2:
    print(f"{nombre_p2} {apellido_p2} tiene mayor edad que {nombre_p1} {apellido_p1}")
elif edad_p1 == edad_p2:
    print(f"{nombre_p1} {apellido_p1} y {nombre_p2} {apellido_p2} tienen la misma edad")
else:
    print(f"{nombre_p1} {apellido_p1} tiene mayor edad que {nombre_p2} {apellido_p2}")
    