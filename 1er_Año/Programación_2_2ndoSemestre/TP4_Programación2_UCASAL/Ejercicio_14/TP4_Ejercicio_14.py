'''
Universidad Católica de Salta
Programación 2 - 2ndo Semestre
TP4
autor: Gaspar Ramiro Sebastian

Ej 14:
Ejercicio Final Integrador:
Inventar un ejercicio de enunciado propio y desarrollo individual, que contenga
todo lo visto en la materia, al menos una vez cada herramienta vista. Es decir, la
resolución del enunciado debe tener:
- Cálculos secuenciales
- Ingreso de datos por parte del usuario, y mostrarle resultados
- Funciones para el tratamiento de cadenas de texto
- Estructuras de selección
- Bucles
- Diccionario de Datos
- Lectura de un archivo csv
- Gráficos con Matploblib
- Array NumPy
'''

# ENUNCIADO:
'''
Sistema de Análisis de Gastos Mensuales
Desarrollar un programa en Python que analice gastos mensuales a partir de un archivo CSV 
(gastos_mensuales.csv) que contiene: fecha, categoría (luz, supermercado, transporte, etc.), 
descripción y monto. El programa debe presentar un menú interactivo usando while que permita 
al usuario: ver el total de gastos, consultar gastos por categoría específica, y generar 
gráficos. Utilizar un diccionario para agrupar gastos por categoría, funciones para procesar 
y formatear nombres de categorías (eliminar espacios, convertir a mayúsculas/minúsculas), 
estructuras if/elif/else para validar entradas del usuario, NumPy para calcular estadísticas 
(suma total, promedio, máximo, mínimo de montos), y Matplotlib para generar al menos dos 
gráficos: uno de barras mostrando el total gastado por categoría y otro de líneas mostrando la 
evolución temporal de los gastos. El programa debe solicitar input del usuario para navegar el 
menú y seleccionar opciones, y mostrar los resultados de forma clara en pantalla.
'''

import numpy as np
import matplotlib.pyplot as plt
import csv

def analisis_csv():
    # Listas para recolectar datos del .csv
    gastos = []
    meses = []
    años = []
    categorias = []
    
    with open('GastosMensuales.csv','r') as archivo:
        lector = csv.DictReader(archivo)
        
        for fila in lector:
            gastos.append(float(fila['precio'].strip()))
            meses.append(int(fila['mes'].strip()))
            años.append(int(fila['año'].strip()))
            categorias.append(fila['categoria'].strip().lower())
    
    return gastos,meses,años,categorias
    
def grafico_gastos_generales_plot(gastos,meses,años):
    
    datos = {} # Diccionario para el manejo de valores para graficar
    
    try: 
        desicion = input("¿Quieres ver el gráfico 'mensual' o 'anual'? ").strip().lower()
        if desicion == "mensual":
            año_filtro = int(input("Ingresa el año donde quieres ver los gastos mensaules (Formato: 0000): "))
            
            for g, m, a in zip(gastos,meses,años): # Se emparejan en una tupla los valores mediante zip() y se recorren
                if a == año_filtro:
                    if m not in datos: datos[m] = g # Se agrega dentro de el diccionario la clave m (el numero del mes) y se le da como valor el gasto
                    else: datos[m] += g # Se acumula el gasto dentro de una clave ya existente
            
            if datos:
                plt.title("GRAFICO MENSUAL - Grafico Plot")
                plt.plot(datos.keys(),datos.values())
                plt.scatter(datos.keys(),datos.values())
                
                # Para el eje x se muestan los meses exactos, convirtiendo las claves en una lista.
                # Despues se crea una lista comprimida que genera los nombres de los meses con ayuda
                # de el diccionario nombre_meses:
                plt.xticks(list(datos.keys()),[nombres_meses[m] for m in datos.keys()]) 
                
                plt.yticks(list(datos.values()))
                plt.grid(True, alpha=0.3)
                plt.xlabel("Mes")
                plt.ylabel("Gastos")
                plt.show()

        elif desicion == "anual":
            for g, m, a in zip(gastos,meses,años):
                if a not in datos: datos[a] = g
                else: datos[a] += g
            
            if datos:
                plt.title("GRAFICO MENSUAL - Grafico Plot")
                plt.plot(datos.keys(),datos.values())
                plt.scatter(datos.keys(),datos.values())
                plt.xticks(list(datos.keys()))
                plt.yticks(list(datos.values()))
                plt.grid(True, alpha=0.3)
                plt.xlabel("Año")
                plt.ylabel("Gastos")
                plt.show()
        
        else: print("Error. Se ingreso una palabra no valido, vuelve a intentar")
    
    except ValueError: print("Error: Se ingreso un dato invalido, vuelve a intentar")

def grafico_gastos_generales_barra(gastos,meses,años):
    
    datos = {}
    
    try:
        desicion = input("¿Quieres ver el gráfico 'mensual' o 'anual'? ").strip().lower()
        if desicion == "mensual":
            año_filtro = int(input("Ingresa el año donde quieres ver los gastos mensaules (Formato: 0000): "))
            
            for g,m,a in zip(gastos,meses,años):
                if a == año_filtro:
                    if m not in datos: datos[m] = g
                    else: datos[m] += g
            
            if datos:
                plt.title("GRAFICO MENSUAL - Grafico de Barras")
                plt.bar(datos.keys(),datos.values())
                plt.xticks(list(datos.keys()),[nombres_meses[m] for m in datos.keys()])
                plt.yticks(list(datos.values()))
                plt.grid(True, alpha=0.3)
                plt.xlabel("Mes")
                plt.ylabel("Gastos")
                plt.show()
        
        elif desicion == "anual":
            for g,m,a in zip(gastos,meses,años):
                if a not in datos: datos[a] = g
                else: datos[a] += g
            
            if datos:
                plt.title("GRAFICO MENSUAL - Grafico de Barras")
                plt.bar(datos.keys(),datos.values())
                plt.xticks(list(datos.keys()))
                plt.yticks(list(datos.values()))
                plt.grid(True, alpha=0.3)
                plt.xlabel("Año")
                plt.ylabel("Gastos")
                plt.show()
            
        else: print("Error. Se ingreso una palabra no valido, vuelve a intentar")
        
    except ValueError: print("Error: Se ingreso un dato no valido, vuelve a intentar")
    
def calculos_generales(gastos,meses,años):
    
    lista_gastos = []
    
    print("--CALCULOS GENERALES--")
    desicion = input("¿Quieres realizar los calculos de forma 'mensual' o 'anual'? ").strip().lower()
    
    try: 
        if desicion == "mensual":
            print("\n--CALCULOS GENERALES (de forma mensual)--")
            año_filtro = int(input("Ingresa el año donde quieres ver los gastos mensaules (Formato: 0000): "))
            
            # Creacion del array, que solo sigue los meses dentro de un solo año    
            for g,m,a in zip(gastos,meses,años):
                if a == año_filtro:
                    lista_gastos.append(g)
        
            array_gastos = np.array(lista_gastos)
            
            print("\n¿Qué quieres revisar?")
            print("- Ingresa 'total' para ver el total de gastos")
            print("- Ingresa 'promedio' para ver el resultado")
            print("- Ingresa 'maximo' para ver el gasto maximo")
            print("- Ingresa 'minimo' para ver el gasto minimo")
            print("- Ingresa 'todo' para ver todas las opciones")
            
            desicion_2 = input("Ingresa la opcion: ").strip().lower()
            
            if desicion_2 == "total": print("\nEl total de los gastos: ",np.sum(array_gastos))
            elif desicion_2 == "promedio": print("\nEl promedio de los gastos: ", np.average(array_gastos))
            elif desicion_2 == "maximo": print("\nEl gasto maximo es: ",np.max(array_gastos))
            elif desicion_2 == "minimo": print("\nEl gasto minimo es: ",np.min(array_gastos))
            elif desicion_2 == "todo":
                print("\n--Todos los calculos--")
                print("El total de los gastos: ",np.sum(array_gastos))
                print("El promedio de los gastos: ", np.average(array_gastos))
                print("El gasto maximo es: ",np.max(array_gastos))
                print("El gasto minimo es: ",np.min(array_gastos))
            
        elif desicion == "anual":
            print("\n--CALCULOS GENERALES (de forma anual)--")
            for g,m,a in zip(gastos,meses,años):
                lista_gastos.append(g)
        
            array_gastos = np.array(lista_gastos)
            
            print("\n¿Qué quieres revisar?")
            print("- Ingresa 'total' para ver el total de gastos")
            print("- Ingresa 'promedio' para ver el resultado")
            print("- Ingresa 'maximo' para ver el gasto maximo")
            print("- Ingresa 'minimo' para ver el gasto minimo")
            print("- Ingresa 'todo' para ver todas las opciones")
            
            desicion_2 = input("Ingresa la opcion: ").strip().lower()
            
            if desicion_2 == "total": print("\nEl total de los gastos: ",np.sum(array_gastos))
            elif desicion_2 == "promedio": print("\nEl promedio de los gastos: ", np.average(array_gastos))
            elif desicion_2 == "maximo": print("\nEl gasto maximo es: ",np.max(array_gastos))
            elif desicion_2 == "minimo": print("\nEl gasto minimo es: ",np.min(array_gastos))
            elif desicion_2 == "todo":
                print("\n--Todos los calculos--")
                print("El total de los gastos: ",np.sum(array_gastos))
                print("El promedio de los gastos: ", np.average(array_gastos))
                print("El gasto maximo es: ",np.max(array_gastos))
                print("El gasto minimo es: ",np.min(array_gastos))
            else: print("Error. Ingreso no valido")
        else: print("Error: Se ingreso una palabra no valida, vuelve a intentar") 
        
    except ValueError: print("Error: Se ingreso un dato no valido, vuelve a intentar")

def calculos_especificos(gastos,meses,años,categorias):
    
    diccionario = {}
    
    print("\n--CALCULOS ESPECIFICOS--")
    desicion = input("¿Quieres realizar los calculos de forma 'mensual' o 'anual'? ").strip().lower()
    
    try:
        if desicion == "mensual":
            print("\n--CALCULOS POR CATEGORIA (de forma mensual)--")
            año_filtro = int(input("Ingresa el año donde quieres ver los gastos mensaules (Formato: 0000): "))
            
            for g,m,a,c in zip(gastos,meses,años,categorias):
                if a == año_filtro:
                    if c not in diccionario: 
                        diccionario[c] = []
                    diccionario[c].append(g)
            
            print("\nEstas son las categorias disponibles: ")
            for elemento in diccionario.keys():
                print(f"- '{elemento}', ingresa esa palbra para revisar las opciones de calculo")
            
            desicion_2 = input("Ingresa la categoria: ").strip().lower()
            if desicion_2 in diccionario:
                
                array_gastos = np.array(diccionario[desicion_2])
            
                print("\n¿Qué quieres revisar?")
                print("- Ingresa 'total' para ver el total de gastos por categoria")
                print("- Ingresa 'promedio' para ver el promedio de gastos por categoria")
                print("- Ingresa 'maximo' para ver el gasto maximo por categoria")
                print("- Ingresa 'minimo' para ver el gasto minimo por categoria")
                print("- Ingresa 'todo' para ver todas las opciones")
                
                desicion_3 = input("Ingresa la opcion: ").strip().lower()
                
                if desicion_3 == "total":print(f"\nEl total de la categoria '{desicion_2}': ",np.sum(array_gastos))
                elif desicion_3 == "promedio": print(f"\nEl promedio de la categoria '{desicion_2}': ",np.average(array_gastos))
                elif desicion_3 == "maximo": print(f"\nEl gasto maximo de la categoria '{desicion_2}': ",np.max(array_gastos))
                elif desicion_3 == "minimo": print(f"\nEl gasto minimo de la categoria '{desicion_2}': ",np.min(array_gastos))
                elif desicion_3 == "todo":
                    print(f"\n--Todos los calculos sobre {desicion_2}--")
                    print(f"El promedio de la categoria '{desicion_2}': ",np.average(array_gastos))
                    print(f"El gasto maximo de la categoria '{desicion_2}': ",np.max(array_gastos))
                    print(f"El gasto minimo de la categoria '{desicion_2}': ",np.min(array_gastos))
                else: print("Error. Ingreso no valido")
                    
            else: print("Error. No se encontro la categoria")

        elif desicion == "anual":
            print("\n--CALCULOS POR CATEGORIA (de forma anual)--")
            
            for g,m,a,c in zip(gastos,meses,años,categorias):
                if c not in diccionario: 
                    diccionario[c] = []
                diccionario[c].append(g)
            
            print("\nEstas son las categorias disponibles: ")
            for elemento in diccionario.keys():
                print(f"- '{elemento}', ingresa esa palbra para revisar las opciones de calculo")
            
            desicion_2 = input("Ingresa la categoria: ").strip().lower()
            if desicion_2 in diccionario:
                
                array_gastos = np.array(diccionario[desicion_2])
            
                print("\n¿Qué quieres revisar?")
                print("- Ingresa 'total' para ver el total de gastos por categoria")
                print("- Ingresa 'promedio' para ver el promedio de gastos por categoria")
                print("- Ingresa 'maximo' para ver el gasto maximo por categoria")
                print("- Ingresa 'minimo' para ver el gasto minimo por categoria")
                print("- Ingresa 'todo' para ver todas las opciones")
            
                desicion_3 = input("Ingresa la opcion: ").strip().lower()
                
                if desicion_3 == "total":print(f"\nEl total de la categoria '{desicion_2}': ",np.sum(array_gastos))
                elif desicion_3 == "promedio": print(f"\nEl promedio de la categoria '{desicion_2}': ",np.average(array_gastos))
                elif desicion_3 == "maximo": print(f"\nEl gasto maximo de la categoria '{desicion_2}': ",np.max(array_gastos))
                elif desicion_3 == "minimo": print(f"\nEl gasto minimo de la categoria '{desicion_2}': ",np.min(array_gastos))
                elif desicion_3 == "todo":
                    print(f"\n--Todos los calculos sobre {desicion_2}--")
                    print(f"El promedio de la categoria '{desicion_2}': ",np.average(array_gastos))
                    print(f"El gasto maximo de la categoria '{desicion_2}': ",np.max(array_gastos))
                    print(f"El gasto minimo de la categoria '{desicion_2}': ",np.min(array_gastos))
                else: print("Error. Ingreso no valido")
            
            else: print("Error. No se encontro la categoria")   
        else: print("Error. Se ingreso una palabra no valida, vuelve a intentar")
        
    except ValueError: print("Error: Se ingreso un dato no valido, vuelve a intentar")
    
def grafico_gastos_por_categoria(gastos, meses, años, categorias):
    
    datos = {}
    
    try:
        desicion = input("¿Quieres ver el gráfico por categoría 'mensual' o 'anual'? ").strip().lower()
        if desicion == "mensual":
            año_filtro = int(input("Ingresa el año donde quieres ver los gastos por categoría (Formato: 0000): "))
            
            for g, m, a, c in zip(gastos, meses, años, categorias):
                if a == año_filtro:
                    if c not in datos: datos[c] = g
                    else: datos[c] += g
            
            if datos:
                plt.title(f"GASTOS POR CATEGORÍA - Año {año_filtro} - Gráfico de Barras")
                plt.bar(datos.keys(), datos.values())
                plt.xticks(rotation=45)
                plt.grid(True, alpha=0.3)
                plt.xlabel("Categorías")
                plt.ylabel("Total Gastado")
                plt.tight_layout()
                plt.show()
                
        elif desicion == "anual":
            # Se encuentra el rango de años para mostrarlo en el título
            año_min = min(años)
            año_max = max(años)
            
            for g, m, a, c in zip(gastos, meses, años, categorias):
                if c not in datos: datos[c] = g
                else: datos[c] += g
            
            if datos:
                if año_min == año_max:
                    plt.title(f"GASTOS POR CATEGORÍA - Año {año_min} - Gráfico de Barras")
                else:
                    plt.title(f"GASTOS POR CATEGORÍA - Período {año_min}-{año_max} - Gráfico de Barras")
                
                plt.bar(datos.keys(), datos.values())
                plt.xticks(rotation=45)
                plt.grid(True, alpha=0.3)
                plt.xlabel("Categorías")
                plt.ylabel("Total Gastado")
                plt.tight_layout()
                plt.show()
                
        else: print("Error. Se ingresó una palabra no válida, vuelve a intentar")
            
    except ValueError: print("Error: Se ingresó un dato no válido, vuelve a intentar")
        
# diccionario util para graficar 
nombres_meses = {1:"Enero", 2:"Febrero", 3:"Marzo", 4:"Abril", 5:"Mayo",
    6:"Junio", 7:"Julio", 8:"Agosto", 9:"Septiembre",
    10:"Octubre", 11:"Noviembre", 12:"Diciembre"}
            
def main():
    gastos, meses, años, categorias = analisis_csv()

    while True:
        print("\n-- MENÚ DE OPCIONES --")
        print("1. Ver gráfico de gastos mensuales o anuales (gráfico plot)")
        print("2. Ver gráfico de gastos mensuales o anuales (gráfico de barras)")
        print("3. Ver gráfico de gastos por categoría")
        print("4. Ver opciones de cálculos más generales")
        print("5. Ver opciones de cálculos más específicos (categorías)")
        print("6. Salir")
        opcion = input("Selecciona una opción: ").strip()
        
        if opcion == "1": grafico_gastos_generales_plot(gastos, meses, años)
        elif opcion == "2": grafico_gastos_generales_barra(gastos, meses, años)
        elif opcion == "3": grafico_gastos_por_categoria(gastos, meses, años, categorias)
        elif opcion == "4": calculos_generales(gastos, meses, años)
        elif opcion == "5": calculos_especificos(gastos, meses, años, categorias)
        elif opcion == "6":
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida: Por favor, intenta de nuevo.")

if __name__ == "__main__":
    main()