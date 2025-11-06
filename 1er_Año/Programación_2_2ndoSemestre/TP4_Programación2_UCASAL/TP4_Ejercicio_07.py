'''
Universidad Católica de Salta
Programación 2 - 2ndo Semestre
TP4
autor: Gaspar Ramiro Sebastian

Ej 7
Realizar dos gráficos conjuntos “plot” y “scatter” (dentro de un mismo figure). Utilizar
los datos del archivo población.csv (adjunto). Year como “x” y población como “y”.
Título del gráfico “Población Histórica Mundial”. Plot con líneas verdes; Scatter con
puntos rojos.
'''

import matplotlib.pyplot as plt
import csv
años = []
poblacion = []

with open('poblacion.csv','r') as archivo:
    lector = csv.DictReader(archivo)
    
    for fila in lector:
        años.append(int(fila['year']))
        poblacion.append(int(fila['poblacion']))
      
# nota: se usa la funcion zip() para crear pares entre los valores de ambas listas
datos_ordenados = sorted(zip(años,poblacion)) # devuelve lista con los pares en tuplas
años_ordenados, poblacion_ordenada = zip(*datos_ordenados) # se desempaqueta y devuelve una tupla ordenada  
# devuelve una tupla en vez de lista pero en este caso no afecta, sino se usa la funcion list()

def grafico(años,poblacion):
    plt.title("Población Historica Mundial")
    plt.plot(años,poblacion,color = "green")
    plt.scatter(años,poblacion, color = "red")
    plt.xlabel("Años")
    plt.ylabel("Población")
    plt.show()

grafico(años_ordenados,poblacion_ordenada)