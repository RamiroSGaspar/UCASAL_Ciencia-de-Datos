'''
Universidad Católica de Salta
Programación 2 - 2ndo Semestre
TP4
autor: Gaspar Ramiro Sebastian

ej 10:
Realizar el código necesario para visualizar este gráfico (**2 y **3):
'''

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-4, 40,400)
y2 = x ** 2
y3 = x ** 3

def grafico(x,y2,y3):

    plt.plot(x, y2, label='**2')
    plt.plot(x, y3, label='**3')
    plt.xlim(-4, 4)
    plt.ylim(-70, 70)
    plt.grid(True, alpha=0.3)
    plt.legend()
    plt.show()
    
grafico(x,y2,y3)