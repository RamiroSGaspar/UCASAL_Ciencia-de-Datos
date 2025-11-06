'''
Universidad Católica de Salta
Programación 2 - 2ndo Semestre
TP3
autor: Gaspar Ramiro Sebastian

Ej1:
Escribir un programa que solicite la cantidad de kilómetros recorridos por un
auto y la cantidad total de litros que consumió en ese recorrido. Luego mostrar
por pantalla cuántos kilómetros hace por litro. 
'''
print("--Programa para calcular km por litro consumido en un auto--")
km_recorridos = float(input("Ingresa la cantidad de km recorridos con el auto: "))
litros_consumidos = float(input("Ingresa la cantidad de litros consumidos: "))

if litros_consumidos == 0: print("Error: no se puede ingresar 0 en litros consumidos.")
else: km_x_litro = km_recorridos/litros_consumidos

print(f"El auto recorrio {km_x_litro:.2f} km por litro")