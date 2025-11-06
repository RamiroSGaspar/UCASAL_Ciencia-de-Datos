'''
Universidad Católica de Salta
Programación 2 - 2ndo Semestre
TP3
autor: Gaspar Ramiro Sebastian

Ej 28
Pedir por consola dos números que representen el principio y fin de una
secuencia numérica. Realizar un bucle "for" que recorra esa secuencia armada
con "range" y cuente cuantos números son negativos y cuantos números son
mayor o igual a cero. Tener en cuenta que "range" no incluye el número de "fin"
en su secuencia, sino que va hasta el anterior.
'''

principio = int(input("Ingresa un numero para el principio: "))
fin = int(input("Ingresa un numero para el final: "))
negativos = []
mayor_igual_0 = []

for i in range(principio, fin + 1):
    if i < 0: negativos.append(i)
    elif i >= 0: mayor_igual_0.append(i)

cant_negativos = len(negativos)
cant_0_mayor = len(mayor_igual_0)    

print(f"""
Entre el principio {principio} y el final {fin}
Los numeros negativos que hay son: {cant_negativos}
Y los numeros mayor o igual a cero son: {cant_0_mayor}
      """)

