'''
Universidad Católica de Salta
Programación 2 - 2ndo Semestre
TP3
autor: Gaspar Ramiro Sebastian

Ej 30
Realice una calculadora: Dentro de un bucle se debe ingresar por línea de
comando dos números. Luego se ingresará como tercera entrada al programa el
símbolo de la operación que se desea ejecutar:
Suma (+)
Resta (-)
Multiplicación (*)
División (/)
Exponente/Potencia (**)
Se debe efectuar el cálculo correcto según la operación ingresada por consola.
Imprimir en pantalla la operación realizada y el resultado. El programa se debe
repetir dentro del bucle hasta que como operador se ingrese la palabra "FIN", en
ese momento debe terminar el programa. Se debe mostrar un mensaje de error
si el operador ingresado no es alguno de lo soportados o no es la palabra "FIN".
'''
print("--Calculadora Simple--")
print("""
Elige que operacion quieres hacer ingresando el simbolo del operador
    
Para la Suma ingresa: +
Resta : -
Nultiplicacion: *
Division: /
Exponente o Potencia : **
    
IMPORTANTE: Para salir de la calculadora escriba FIN en vez de ingresar un operador
        """)

while True:
    num1 = int(input("Ingresa un numero: "))
    num2 = int(input("Ingresa otro numero: "))
    operador = input("Ingresa un operador: ")
    
    if operador == "FIN":
        print("\nMENSAJE: Salida de la calculadora lograda")
        break
    elif operador == "+": print(f"{num1} + {num2} = {num1 + num2}\n") 
    elif operador == "-": print(f"{num1} - {num2} = {num1 - num2}\n") 
    elif operador == "*": print(f"{num1} * {num2} = {num1 * num2}\n")
    elif operador == "/":
        if num2 == 0:
            print("ERROR: División por cero no permitida\n")
        else:
            print(f"{num1} / {num2} = {num1 / num2}\n")
    elif operador == "**": print(f"{num1} ** {num2} = {num1 ** num2}\n")
    else: print("ERROR: Operador o ingreso no valido, vuelva a intentar\n")