'''
Universidad Católica de Salta
Programación 1 - 1er Semestre
TP1
autor: Gaspar Ramiro Sebastian

ej 50:
Dada una lista de 10 números ingresados por el usuario, calcular y
mostrar:
a) El promedio de todos los números ingresados.
b) El promedio de los números positivos.
'''
ac = 0
ac_positivo = 0  
contador_positivos = 0  

print("Ingresa diez números a continuación:")

for i in range(1, 11):
    numero = int(input("Ingresa un número: "))
    ac += numero  
    
    if numero > 0:
        ac_positivo += numero  
        contador_positivos += 1  

promedio_total = ac / 10

if contador_positivos > 0:
    promedio_positivos = ac_positivo / contador_positivos
else:
    promedio_positivos = 0  

print("\nEl promedio de todos los números:", promedio_total)
print("El promedio de los números positivos:", promedio_positivos)