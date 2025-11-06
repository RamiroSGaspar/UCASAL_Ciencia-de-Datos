'''
Universidad Católica de Salta
Programación 2 - 2ndo Semestre
TP4
autor: Gaspar Ramiro Sebastian

Realizar un gráfico “multi line plot”. A partir de los siguientes datos:
Mes: 3, 4, 5, 6
gasto_carne: 1650, 2600, 3100, 4000
gasto_verdura: 2500, 2200, 1800, 600
Calcular el gasto total como la suma de las listas gasto_carne y gasto_verdura.
Realizar un gráfico "plot" con: mes como "x"; gasto_carne como "y1”;
gasto_verdura como "y2"; gasto_total como "y3".
'''
import matplotlib.pyplot as plt

mes = [3,4,5,6]
gasto_carne = [1650, 2600, 3100, 4000]
gasto_verdura = [2500, 2200, 1800, 600]

gasto_total_por_mes = []

for i in range(len(mes)):
    suma = gasto_verdura[i] + gasto_carne[i]
    gasto_total_por_mes.append(suma)
    
plt.title("Gastos por Mes")
plt.xlabel("Mes")
plt.ylabel("Dinero")
plt.plot(mes, gasto_carne, label = "Carne")
plt.plot(mes, gasto_verdura, label = "Verdura")
plt.plot(mes, gasto_total_por_mes, label = "Total")
plt.xticks(mes) # Se muestra en el eje x solo los valores dentro de la lista "mes"
plt.legend()
plt.show()