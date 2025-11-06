'''
Universidad Católica de Salta
Programación 2 - 2ndo Semestre
TP3
autor: Gaspar Ramiro Sebastian

Ej 29
Realice un programa que pida por consola dos números que representen el
principio y fin de una secuencia numérica. Realizar un bucle "for" que recorra esa
secuencia armada con "range" y cuente cuantos números ingresados hay, y la
sumatoria de todos los números. Al finalizar el bucle, utilice la variable
"cantidad_numeros" y la variable "sumatoria" para calcular el promedio de
todos los números ingresados. Tener en cuenta que "range" no incluye el
número de "fin" en su secuencia, sino que va hasta el anterior.
'''

principio = int(input("Ingresa un numero para el principio: "))
fin = int(input("Ingresa un numero para el final: "))
cantidad_numeros = 0
sumatoria = 0

for i in range (principio, fin + 1):
    num = int(input("Ingresa un numero: "))
    cantidad_numeros += 1
    sumatoria += num

promedio = sumatoria / cantidad_numeros
print(f"""
La cantidad de numeros ingresados son: {cantidad_numeros}
La suma entre todos ellos da: {sumatoria}
Y el promedio es: {promedio}
      """)