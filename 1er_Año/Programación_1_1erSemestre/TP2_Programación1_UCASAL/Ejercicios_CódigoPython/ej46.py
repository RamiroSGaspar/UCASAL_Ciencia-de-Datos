'''
Universidad Católica de Salta
Programación 1 - 1er Semestre
TP1
autor: Gaspar Ramiro Sebastian

ej 46:
Solicitar 5 números al usuario. Luego mostrar: la suma total de todos
los números y el producto de todos los números.
'''
ac = 0
print("Ingresa cinco numeros acontinuacion:")

for i in range (1, 6):
   numero = int(input("Ingresa un numero: "))
   ac += numero
   
print("La suma total de todos los numeros es: ",ac)