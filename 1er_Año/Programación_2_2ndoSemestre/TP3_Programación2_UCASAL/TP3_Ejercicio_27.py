'''
Universidad Católica de Salta
Programación 2 - 2ndo Semestre
TP3
autor: Gaspar Ramiro Sebastian

Ej 27
Dada una lista de 10 números ingresados por el usuario, calcular y mostrar:
a) El promedio de todos los números ingresados.
b) El promedio de los números positivos
'''
numeros = []
numeros_positivos = []

print("Ingresa 10 numeros:")
for i in range(1, 11):
    num = int(input("Ingresa un numero: "))
    numeros.append(num)
    
    if num > 0: numeros_positivos.append(num)
    else: numeros_positivos.append(0)
    
promedio = sum(numeros) / len(numeros)
promedio_positivos = sum(numeros_positivos) / len(numeros_positivos)

print(f"""
El promedio de los numeros es: {promedio}
Y el promedio de los positivos es: {promedio_positivos}
      """)