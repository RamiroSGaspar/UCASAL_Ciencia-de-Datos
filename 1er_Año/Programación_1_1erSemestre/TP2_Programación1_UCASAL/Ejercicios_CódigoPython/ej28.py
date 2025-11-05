'''
Universidad Católica de Salta
Programación 1 - 1er Semestre
TP1
autor: Gaspar Ramiro Sebastian

ej 28:
Dada una lista de 10 números ingresados por el usuario, calcular y
mostrar:
a) La suma de todos los números múltiplos de 3.
b) El producto de todos los números múltiplos de 5.
'''
i = 1
ac_multiplos3 = 0  
ac_multiplos5 = 1   
contador_multiplos5 = 0 

print("Ingresa 10 números a continuación")

while i <= 10:
    numero = int(input("Ingresa un número: "))
    
    if numero % 3 == 0:
        ac_multiplos3 += numero
    
    elif numero % 5 == 0:
        ac_multiplos5 *= numero
        contador_multiplos5 += 1
    
    i += 1

print("Suma de números múltiplos de 3:", ac_multiplos3)

if contador_multiplos5 > 0:
    print("Producto de números múltiplos de 5:", ac_multiplos5)
else:
    print("No se ingresaron múltiplos de 5")