'''
Universidad Católica de Salta
Programación 2 - 2ndo Semestre
TP2
autor: Gaspar Ramiro Sebastian

Ej7.
Solicitar al usuario el ingreso de una palabra cualquiera, y mostrarle por pantalla
cuántas letras tiene la palabra ingresada.  
'''
palabra = input("Ingresa cualquier palabra: ")
letras = 0
for i in palabra: letras += 1
print(f"Esa palabra tiene {letras} letras")
