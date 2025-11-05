'''
Universidad Católica de Salta
Programación 1 - 1er Semestre
TP1
autor: Gaspar Ramiro Sebastian

ej 49:
Dada una lista de 10 números ingresados por el usuario, calcular y
mostrar:
a) La cantidad de números múltiplo de 4.
b) La cantidad de números múltiplo de 2.
c) La cantidad de números positivos.
d) La cantidad de números negativos.
'''
mult4 = []
mult2 = []
positivos = []
negativos = []

print("Ingresa diez numeros acontinuacion: ")
for i in range (1, 11):
    
    numero = int(input("Ingresa un numero: "))
    
    if numero % 4:
        mult4.append(numero)
    if numero % 2:
        mult2.append(numero)
    if numero > 0:
        positivos.append(numero)
    if numero < 0:
        negativos.append(numero)
    
print("Multiplos de 4: ",mult4)
print("Multiplos de 2: ",mult2)
print("Los numeros positivos: ",positivos)
print("Los numeros negativos: ",negativos)