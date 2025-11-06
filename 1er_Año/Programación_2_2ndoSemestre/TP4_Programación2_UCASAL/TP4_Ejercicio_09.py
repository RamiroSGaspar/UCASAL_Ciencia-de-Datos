'''
Universidad Católica de Salta
Programación 2 - 2ndo Semestre
TP4
autor: Gaspar Ramiro Sebastian

Ej 9:
Realizar el código necesario para visualizar este gráfico (**2):
'''


import matplotlib.pyplot as plt

# Version 1
'''
eje_x = [100,80,60,40,20,0,20,40,60,80,100]
eje_y = [-10,-9,-7.55,-5.5,-2.7,0,2.7,5.5,7.55,9,10]

def grafico(x,y):
    plt.title("Valores x e y")
    plt.plot(x,y,color = "green")
    plt.scatter(x,y, color = "red")
    plt.grid(True, alpha=0.3)
    plt.show()
    
grafico(eje_x,eje_y)
'''

# Version 2
import numpy as np

x = np.linspace(0,100,50)
y_positivos = np.sqrt(x)
y_negativos = -(np.sqrt(x))

def grafico(x,y_positivos,y_negativos):
    plt.title("Valores x e y")
    plt.plot(x, y_positivos, color = "red",label = "ej9")
    plt.plot(x,y_negativos, color = "red")
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.show()
    
grafico(x,y_positivos,y_negativos)