'''
Universidad Católica de Salta
Programación 2 - 2ndo Semestre
TP2
autor: Gaspar Ramiro Sebastian

Ej. 11
Solicitar al usuario el ingreso de dos palabras y armar combinaciones con ellas.
De la primera palabra tome las primeras tres letras, utilice el operador “:”. De la 
segunda palabra tome las primeras dos letras, utilice el operador “:”. Formar una
nueva palabra con los recortes solicitados y mostrarlo por pantalla. 
'''
palabra1 = input("Ingresa una palabra: ")
palabra2 = input("Ingresa la segunda palabra: ")
porcion1 = palabra1[:3]
porcion2 = palabra2[:2]

print("La combinacion entre las porciones es da :",porcion1 + porcion2)