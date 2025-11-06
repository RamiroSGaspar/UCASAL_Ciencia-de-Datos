'''
Universidad Católica de Salta
Programación 2 - 2ndo Semestre
TP4
autor: Gaspar Ramiro Sebastian

Ej 3
Realice un programa que abra el archivo 'stock.csv' (se adjunta) en modo lectura y
cuente el stock total de tornillos a lo largo de todo el archivo, sumando el stock en
cada fila del archivo. Para eso debe leer los datos del archivo con "csv.DictReader", y
luego recorrer los datos dentro de un bucle y solo acceder a la columna "tornillos"
para cumplir con el enunciado del ejercicio.
'''

import csv

stock = {
    'Tornillos': 0,
    'Tuercas': 0,
    'Arandelas': 0
}

total_tornillos = 0

# Consigna:
'''
with open('stock.csv','r') as archivo:
    lector = csv.DictReader(archivo)
        
    for fila in lector:
        total_tornillos += int(fila['tornillos'])

print("El total de los tornillos es: ",total_tornillos)
'''

# Alternaiva:
with open('stock.csv','r') as archivo:
    lector = csv.DictReader(archivo)
        
    for fila in lector:
        print(fila)
        stock['Tornillos'] += int(fila['tornillos'])
        stock['Tuercas'] += int(fila['tuercas'])
        stock['Arandelas'] += int(fila['arandelas'])
        
print("Los productos mas el stock disponible: ")
for producto in stock.keys():
    print(f"{producto} : {stock[producto]}")