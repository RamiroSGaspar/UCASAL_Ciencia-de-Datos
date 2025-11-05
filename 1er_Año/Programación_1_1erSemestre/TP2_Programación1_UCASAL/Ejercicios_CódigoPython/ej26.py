'''
Universidad Católica de Salta
Programación 1 - 1er Semestre
TP1
autor: Gaspar Ramiro Sebastian

ej 26:
Dada la cantidad de alumnos de un curso ingresada por el usuario,
solicitar todas las edades y mostrar el promedio general de edad del
curso.
'''
cantidad = int(input("Ingresa la cantidad de alumnos: "))
i = 1
ac_edades = 0

while i <= cantidad:
    
    edad = int(input("Ingresa un la edad de un alumno: "))
    ac_edades += edad
    i += 1

if cantidad > 0:
    promedio = ac_edades // cantidad
    print("Pormedio de edades de los alumnos: ",promedio)
else:
    print("No se pueda calcular el promedio")

