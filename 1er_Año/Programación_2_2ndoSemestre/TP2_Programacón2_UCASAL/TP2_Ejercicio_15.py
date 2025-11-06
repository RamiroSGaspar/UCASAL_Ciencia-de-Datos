'''
Universidad Católica de Salta
Programación 2 - 2ndo Semestre
TP2
autor: Gaspar Ramiro Sebastian

Ej. 15
Realice un programa que determine cual sería el apellido de una persona al
ingresar los dos nombres completos de sus padres. Es decir, se solicita crear una
variable nueva que reúna los apellidos. Primero el programa debe consultar el
nombre completo del padre_1, luego el programa debe consultar el nombre
completo del padre_2, luego debe consultar el nombre del hijo/a. Debe extraer
los apellidos de los padres (ver la nota al final). Luego formar el nombre completo
del hijo/a utilizando los apellidos de sus padres y el nombre ingresado de dicha
persona. Mostrar por pantalla el resultado.
NOTA: Para extraer el apellido del nombre completo recomiendo usar el
método "split". Por ejemplo:
direccion_completa = 'Mitre 465'
calle, altura = direccion_completa.split(' ') 
'''
# opcion 1, con diccionarios
print("--Programa para determinar el apellido de un hijo/a--")
papá = {
    "apellido": input("Ingresa el apellido del padre: "),
    "nombre": input("Ingresa el nombre del padre: ")
}
mamá ={
    "apellido": input("Ingresa el apellido de la madre: "),
    "nombre": input("Ingresa el nombre de la madre: ")
}

hijo = input("Ingresa el nombre del hijo/a: ")
print(f"El nombre completo del hijo/a es: {hijo} {papá['apellido']} {mamá['apellido']}")

# opcion 2, con split
'''
print("--Programa para determinar el apellido de un hijo/a--")
padre = input("Ingresa el nombre completo del padre: ")
madre = input("Ingresa el nombre completo de la madre: ")
hijo = input("Ingresa el nombre del hijo/a: ")

nombre_padre, apellido_padre = padre.split(" ")
nombre_madre, apellido_madre = madre.split(" ")

print(f"El nombre completo del hijo/a es: {hijo} {apellido_padre} {apellido_madre}")
'''