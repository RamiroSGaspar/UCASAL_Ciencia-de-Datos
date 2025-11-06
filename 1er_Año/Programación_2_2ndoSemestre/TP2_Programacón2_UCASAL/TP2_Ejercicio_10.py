'''
Universidad Católica de Salta
Programación 2 - 2ndo Semestre
TP2
autor: Gaspar Ramiro Sebastian

Ej. 10
Solicitar al usuario el ingreso del total de alumnos del curso, luego la cantidad de
mujeres y la cantidad de varones. Calcular y mostrar el porcentaje de varones y
mujeres de la clase. 
'''
print("--Programa para calcular el porcentaje de hombres y mujeres en el aula--")
total = int(input("Ingresa el total de alumnos en el curso: "))
m = int(input("Ingresa la cantidad de hombres: "))
f = int(input("Ingresa la cantidad de mujeres: "))

if m > total or f > total: print("Error, verifique la cantidad de hombres o mujeres ingresados")
else:
    porcentaje_m = (m * 100) / total
    porcentaje_f = (f * 100) / total
    print(f"El porcentaje de hombres en el aula es: {porcentaje_m}%")
    print(f"El porcentaje de mujeres en el aula es: {porcentaje_f}%")  
    