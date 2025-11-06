'''
Universidad Católica de Salta
Programación 2 - 2ndo Semestre
TP3
autor: Gaspar Ramiro Sebastian

Ej 26
Dada una lista de 10 números ingresados por el usuario, calcular y mostrar:
a) La cantidad de números múltiplo de 4.
b) La cantidad de números múltiplo de 2.
c) La cantidad de números positivos.
d) La cantidad de números negativos.
'''
numeros = []
mult_4 = []
mult_2 = []
num_positivos = []
num_negativos = []

print("Ingresa 10 numeros: ")
for i in range (1, 11):
    num = int(input("Ingresa un numero: "))
    if num % 4 == 0: mult_4.append(num)
    if num % 2 == 0: mult_2.append(num)
    if num > 0: num_positivos.append(num)
    if num < 0: num_negativos.append(num)

cant_mult4 = len(mult_4)
cant_mult2 = len(mult_2)
cant_positivos = len(num_positivos)
cant_negativos = len(num_negativos)

print(f"""
Esta es la cantidad de numeros multipos de 4: {cant_mult4}
Esta es la cantidad de numeros multiplos de 2: {cant_mult2}
Esta es la cantidad de positivos: {cant_positivos}
Esta es la cantidad de negativos: {cant_negativos}
      """)