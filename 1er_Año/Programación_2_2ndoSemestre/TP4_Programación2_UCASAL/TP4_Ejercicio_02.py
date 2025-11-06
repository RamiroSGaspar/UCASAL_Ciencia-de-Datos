'''
Universidad Católica de Salta
Programación 2 - 2ndo Semestre
TP4
autor: Gaspar Ramiro Sebastian

Ej 2:
Basado en el ejercicio anterior ej1, utilizaremos el diccionario como una base de
datos. Comenzaremos con un diccionario de stock de nuestros productos en cero:
 stock = {'tornillos': 0, 'tuercas': 0, 'arandelas': 0}
Crear un bucle utilizando while que se ejecute de forma infinita while True.....
Dentro de ese bucle consultar al usuario por consola que producto desea agregar al
stock. Si el usuario ingresa "FIN" como producto se debe finalizar el bucle. Si el
usuario ingresa un producto no definido en el stock se debe enviar un mensaje de
error (si desea investigar esto se resuelve muy bien utilizando el operador "in" con
diccionarios).
Luego de haber ingresado el producto se debe ingresar por consola cuanto stock de
ese producto se desea agregar al stock. Si teníamos 20 tornillos y el usuario desea
agregar 10 tornillos más, en nuestro diccionario deben quedar 30 tornillos (debe
acumular). Cuando el usuario ingrese "FIN" y se termine el bucle, debe imprimir en
pantalla con print el diccionario con el stock final. 
'''

def crear_stock():
    stock = {}

    stock["Tornillos"] = 0
    stock["Tuercas"] = 0
    stock["Arandelas"] = 0
    
    return stock

def mostrar_stock(stock):
    print("\nEsta es la lista de productos con su stock")
    for clave in stock.keys():
        print(clave, ":", stock[clave])
    
stock = crear_stock()
mostrar_stock(stock)

print("\n--Programa para agregar stock--")
while True:
    x = input("Ingresa el nombre del producto a sumar stock: ")
    producto = x[0].upper() + x[1:].lower()

    if producto == "Fin":
        print("Saliendo del programa...")
        break
    elif producto not in stock:
        print("Error: El nombre es invalido, ingresa tal cual se mostro arriba")
    elif producto in stock:
        cant = int(input(f"Ingresa la cantidad para aumentar el stock de {producto}: "))
        stock[producto] += cant
    
mostrar_stock(stock)
        
        