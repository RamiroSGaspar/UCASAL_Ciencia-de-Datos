'''
Universidad Católica de Salta
Programación 2 - 2ndo Semestre
TP4
autor: Gaspar Ramiro Sebastian

Ej 4:
Realice un programa que abra el archivo CSV "propiedades.csv" (se adjunta) en modo
lectura. Recorrer dicho archivo y contar la cantidad de departamentos de 2ambientes y 
la cantidad de departamentos de 3 ambientes disponibles. Al finalizar el
proceso, imprima en pantalla los resultados. Tener cuidado que hay departamentos
que no tienen definidos la cantidad de ambientes, verifique que el texto no esté vacío
antes de convertirlo a entero con "int( .. )". Si desea investigar puede evitar que el
programa explote utilizando "try except".
'''
import csv

cant_ambientes2 = 0
cant_ambientes3 = 0

with open('propiedades.csv','r') as archivo:
    lector = csv.DictReader(archivo)
    
    for fila in lector:
        if fila['tipo_propiedad'] == "Departamento":
            
            ambientes_texto = fila['ambientes'].strip() # metodo en caso de que haya un " "
            
            if ambientes_texto:
                cant_ambientes = int(ambientes_texto)
                if cant_ambientes == 2: cant_ambientes2 += 1
                elif cant_ambientes == 3: cant_ambientes3 += 1
            
print(f"""
La cantidad de departamentos con 3 ambientes es: {cant_ambientes3}
Y la cantidad de departamentos con 2 ambientes es de: {cant_ambientes2}
      """)