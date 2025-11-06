'''
Universidad Católica de Salta
Programación 2 - 2ndo Semestre
TP4
autor: Gaspar Ramiro Sebastian

Ej 1:
Crear un diccionario vacío. El diccionario debe llamarse "stock". Luego de crear el
diccionario complételo con el siguiente stock:

tornillos = 100
tuercas = 150
arandelas = 300

Los nombres tornillos, tuercas y arandelas son las claves (keys) del diccionario
mientras que las cantidades son los valores (values). Una vez armado el diccionario
imprimirlo en pantalla con print. 
'''

stock = {}

stock["Tornillos"] = 100
stock["Tuercas"] = 150
stock["Arandelas"] = 300

# Impresion simple
print("Impresion simple:")
print(stock)

# Impresion mas clara
print("\nImpresion mas clara: ")
for clave in stock.keys():
    print(clave, ":", stock[clave])

'''
Aunque un diccionario no pertenece a una secuencia como una lista o tupla
hay varias formas de poder recorrer la misma mediante metodos como:
kesy() -> que devuelve una lista de las keys del diccionario
value() -> que devuelve una lista de vuales del diccionario
items() -> que devuelve una lista de tuplas que guardan el par de key : value
'''
print("\nMostrar lista de keys")
print(stock.keys())

print("\nMostrar lista de values")
print(stock.values())


print("\nMostrar lista de tupla con ambos pares")
print(stock.items())