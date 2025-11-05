'''
Universidad Católica de Salta
Programación 1 - 1er Semestre
TP1
autor: Gaspar Ramiro Sebastian

ej 47:
Dada la cantidad de alumnos de un curso ingresada por el usuario,
solicitar todas las edades y mostrar el promedio general de edad del
curso.
'''
cantidad = int(input("Ingresa la cantidad de alumnos: "))
ac = 0

for i in range(1, cantidad + 1):
    edades = int(input("Ingresa la edad de un alumno:"))
    ac += edades
    
promedio = ac // cantidad
print("La el promedio de edad es: ",promedio)