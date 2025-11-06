'''
Universidad Católica de Salta
Programación 2 - 2ndo Semestre
TP3
autor: Gaspar Ramiro Sebastian

Ej 23
Dada la cantidad de alumnos de un curso ingresada por el usuario, solicitar todas
las edades y mostrar el promedio general de edad del curso.
'''
print("--Promedio de edades en el curso--")
cant = int(input("Ingresa la cantidad de alumnos: "))
ac = 0

for i in range (1, cant + 1):
    edad = int(input(f"Ingresa la edad de el alumno n°{i}: "))
    ac = ac + edad

promedio = ac // cant
print("El promedio de edad en el curso es de: ",promedio, "años")