'''
Universidad Católica de Salta
Programación 1 - 1er Semestre
TP1
autor: Gaspar Ramiro Sebastian

ej 13:
Escribir un programa que solicite el ingreso de una letra, luego valide si
es una vocal, mostrando el mensaje “Es vocal” o “No es vocal”.
'''
letra = input("Ingresa una letra para saber si es vocal o no: ").strip().upper()

if len(letra) == 0:
    print("No ingresaste nada")
elif len(letra) > 1:
    print("Ingresa solo un carácter")
elif letra in {'A', 'E', 'I', 'O', 'U'}:
    print("Es una vocal")
else:
    print("No es una vocal")