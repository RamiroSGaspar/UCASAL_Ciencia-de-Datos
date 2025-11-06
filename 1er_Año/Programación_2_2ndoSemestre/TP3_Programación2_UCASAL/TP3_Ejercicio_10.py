'''
Universidad Católica de Salta
Programación 2 - 2ndo Semestre
TP3
autor: Gaspar Ramiro Sebastian

Ej 10
Realice un programa que solicite 2 números. Calcule la diferencia entre ellos e
informe por pantalla si el resultado es positivo, negativo o cero.
'''
n1 = float(input("Ingresa el primer numero: "))
n2 = float(input("Ingresa el segundo numero: "))

diferencia = n1 - n2
print("La diferencia entre ambos numeros es: ",diferencia)
if diferencia < 0: print(f"La diferencia {diferencia} es negativo")
elif diferencia > 0: print(f"La diferencia {diferencia} es positiva")
elif diferencia == 0: print("Es igual a cero")