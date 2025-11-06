'''
Universidad Católica de Salta
Programación 2 - 2ndo Semestre
TP4
autor: Gaspar Ramiro Sebastian

Ej 8:
Realizar un gráfico de barras. Utilizar los datos del archivo población.csv (adjunto).
Year como “x” y población como “y”. Título del gráfico “Población Histórica Mundial”.
Visualizar solo los datos de los años 2000, 2005, 2010, 2015, 2020. Es decir, partiendo
del csv mencionado, recorrerlo creando la estructura de datos necesaria para luego
graficar la población de los años mencionados.
'''
import matplotlib.pyplot as plt
import csv

años_especificos = [2000,2005,2015,2010,2020]

def analisis_csv():
    años = []
    poblacion = []
    
    with open('poblacion.csv','r') as archivo:
        lector = csv.DictReader(archivo)
        
        for fila in lector:
            años.append(int(fila['year']))
            poblacion.append(int(fila['poblacion']))

    datos_ordenados = sorted(zip(años,poblacion))
    return datos_ordenados

def grafico_de_barras(años,poblacion):
    plt.title("Poblacion Mundial Historica")
    plt.bar(años,poblacion)
    plt.xlabel("Años")
    plt.ylabel("Población")
    plt.show()

def datos_especificos(datos, años_especificos):
    años_filtrados = []
    poblacion_filtrada = []
    
    for años, poblacion in datos:
        if años in años_especificos:
            años_filtrados.append(años)
            poblacion_filtrada.append(poblacion)
    
    return años_filtrados, poblacion_filtrada
    

datos = analisis_csv()
años_filtrados, poblacion_filtrada = datos_especificos(datos, años_especificos)

grafico_de_barras(años_filtrados,poblacion_filtrada)
