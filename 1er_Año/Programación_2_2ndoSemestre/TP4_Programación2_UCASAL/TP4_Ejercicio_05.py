'''
Universidad Católica de Salta
Programación 2 - 2ndo Semestre
TP4
autor: Gaspar Ramiro Sebastian

Ej 5:
Realizar un gráfico "plot" con: years como "x" y poblacion como "y"; con los siguientes
datos:
Years: 1900, 1970, 1990, 2000, 2020
Población: 1650, 3692, 5263, 6070, 7800
'''

import matplotlib.pyplot as plt

años = (1900, 1970, 1990, 2000, 2020)
poblacion = (1650, 3692, 5263, 6070, 7800)

plt.title("Grafico de Población")
plt.plot(años, poblacion)
plt.xlabel("año") 
plt.ylabel("población")
plt.show()