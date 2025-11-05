'''
Universidad Católica de Salta
Programación 1 - 1er Semestre
TP1
autor: Gaspar Ramiro Sebastian

Ej 5:
Solicitar al usuario el ingreso del total de alumnos del aula, luego la
cantidad de mujeres y la cantidad de varones. Calcular y mostrar el
porcentaje de varones y mujeres de la clase.
'''

total = int(input("Ingresa la cantidad de alumnos en el aula: "))

if total > 0:
    alumnos = int(input(f"Ingresa la cantidad de alumnos hombres, el limite es {total}, ingresa: "))
    if 0 <= alumnos <= total:
        alumnas = total - alumnos
        
        porcentaje_alumnos = (alumnos / total) * 100
        porcentaje_alumnas = (alumnas / total) * 100
        
        print("el porcentaje de los alumnos hombres es de: ", porcentaje_alumnos, "%")
        print("el porcenteje de las alumnas mujeres es de: ", porcentaje_alumnas, "%")
    else:
        print(f"la cantidad de alumnos varoes, tiene que estar entre 0 y {total}")