'''
Universidad Católica de Salta
Programación 2 - 2ndo Semestre
TP3
autor: Gaspar Ramiro Sebastian

Ej 12
Realice un programa que solicite ingresar tres valores de temperatura. De las
temperaturas ingresadas determinar:
1- ¿Cuáles de ellas es la máxima temperatura ingresada?
2- ¿Cuáles de ellas es la mínima temperatura ingresada?
3- ¿Cuál es el promedio de las temperaturas ingresadas?
'''
t1 = float(input("Ingresa la primera temperatura: "))
t2 = float(input("Ingresa la segunda temperatura: "))
t3 = float(input("Ingresa la tercera temperatura: "))

temperaturas = [t1,t2,t3]
maximo = max(temperaturas)
minimo = min(temperaturas)
promedio = sum(temperaturas) / len(temperaturas)

print(f"""
La temperatura maxima ingresada es {maximo}
La minima temperatura es {minimo}
Y el promedio es {promedio}
      """)