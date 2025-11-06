'''
Universidad Católica de Salta
Programación 2 - 2ndo Semestre
TP2
autor: Gaspar Ramiro Sebastian

Ej5.
Ídem ejercicio 4 pero una vez ingresados nombres y apellidos, almacenarlos en
una sola variable y mostrar el mensaje de bienvenida. 
'''
nombre = input("Ingresa tu nombre: ")
apellido = input("Ingresa tu apellido: ")
usuario = nombre + " " + apellido
print(f"¡¡Bienvenido {usuario}!!")
