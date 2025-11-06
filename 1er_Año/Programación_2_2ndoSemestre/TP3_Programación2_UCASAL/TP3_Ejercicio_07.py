'''
Universidad Católica de Salta
Programación 2 - 2ndo Semestre
TP3
autor: Gaspar Ramiro Sebastian

Ej 7
Escribir un programa que funcione como un examen tipo múltiple de Choice.
Pregunte al usuario: “¿Qué color se genera mezclando azul y amarillo?” y
muestre las opciones “1- Rojo; 2- Violeta; 3- Verde; 4- Negro”. Luego de recibida
la respuesta muestre el mensaje de “Respuesta Correcta” o “Respuesta
incorrecta” según corresponda.
'''
print("--Examen Multiplechoice--")

print("""
1- ¿Qué color se genera mezclando azul y amarillo?

a) Rojo
b) Violeta
c) Verde
d) Negro

      """)
while True:
    eleccion = input("Ingrese la letra de cada opcion para elegir la respuesta correcta (a,b,c,d): ").lower()
    if eleccion in ("a", "b", "c", "d"):
        if eleccion == "c": print("Respuesta Correcta")
        else: print("Eleccion Incorrecta")
        break
    else: print("Error: Opcion ingresada no valida\nPrueba otra vez\n")
    

