'''
Universidad Católica de Salta
Programación 2 - 2ndo Semestre
TP2
autor: Gaspar Ramiro Sebastian

Ej.9
Solicitar al usuario el ingreso de 3 palabras y armar un acrónimo con ellas. De
cada palabra debe tomar la primera letra y armar el acrónimo. Ejemplo: Qatar,
Argentina y Mundial --> QAM. Mostrar el resultado por pantalla.
'''
print("--Programa para realizar acronimos--")
p1 = input("Ingresa una palabra: ")
p2 = input("Ingresa la segunda palabra: ")
p3 = input("Ingrese la ultima palabra: ")
acronimo = p1[0] + p2[0] + p3[0]
print("El acronimo de las palabras ingresadas es: ", acronimo.upper())