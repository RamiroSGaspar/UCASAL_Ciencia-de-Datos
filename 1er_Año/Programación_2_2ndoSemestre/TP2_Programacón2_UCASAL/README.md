# Trabajo Práctico 2 - Programación 2
**Universidad Católica de Salta (UCASAL)**  
**1er Año - 2ndo Semestre**  
**Alumno:** Ramiro Sebastián Gaspar

---

## 📖 Descripción

Trabajo práctico enfocado en los **fundamentos de programación en Python**. Se desarrollaron 15 ejercicios que cubren conceptos básicos como variables, operadores aritméticos, entrada de datos, manipulación de strings y conversión de tipos de datos.


---

## 📂 Estructura del Repositorio
```
TP2_Programacón2_UCASAL/
├── TP2_Ejercicio_01.py    # Suma de dos números
├── TP2_Ejercicio_02.py    # Resta de dos números
├── TP2_Ejercicio_03.py    # Operaciones aritméticas básicas
├── TP2_Ejercicio_04.py    # Concatenación de strings (nombre y apellido)
├── TP2_Ejercicio_05.py    # Concatenación avanzada
├── TP2_Ejercicio_06.py    # Cálculo de promedio
├── TP2_Ejercicio_07.py    # Contar letras de una palabra
├── TP2_Ejercicio_08.py    # Cálculo de área de triángulo
├── TP2_Ejercicio_09.py    # Generador de acrónimos
├── TP2_Ejercicio_10.py    # Cálculo de porcentajes
├── TP2_Ejercicio_11.py    # Slicing y combinación de strings
├── TP2_Ejercicio_12.py    # Calculadora completa
├── TP2_Ejercicio_13.py    # Sistema de datos personales
├── TP2_Ejercicio_14.py    # Transformación de texto (mayúsculas/minúsculas)
└── TP2_Ejercicio_15.py    # Generador de apellidos compuestos
```

---

## 📥 Cómo Obtener Este Proyecto

### Opción 1: Clonar carpeta específica (recomendado)
```bash
# 1. Clonar el repositorio sin descargar archivos
git clone --no-checkout https://github.com/RamiroSGaspar/UCASAL_Ciencia-de-Datos.git
cd UCASAL_Ciencia-de-Datos

# 2. Configurar sparse-checkout
git sparse-checkout init --cone

# 3. Seleccionar solo esta carpeta
git sparse-checkout set "1er_Año/Programación_2_2ndoSemestre/TP2_Programacón2_UCASAL"

# 4. Descargar los archivos
git checkout main
```

### Opción 2: Clonar todo el repositorio
```bash
git clone https://github.com/RamiroSGaspar/UCASAL_Ciencia-de-Datos.git
cd UCASAL_Ciencia-de-Datos/1er_Año/Programación_2_2ndoSemestre/TP2_Programacón2_UCASAL
```

---

## 🛠️ Tecnologías Utilizadas

- **Python 3.12** - Lenguaje de programación
- **input()** - Función para entrada de datos
- **Operadores aritméticos** - +, -, *, /, //, %, **
- **String methods** - upper(), lower(), split(), slicing

---

## 🚀 Cómo Ejecutar los Ejercicios
```bash
# Navegar a la carpeta del TP2
cd 1er_Año/Programación_2_2ndoSemestre/TP2_Programacón2_UCASAL

# Ejecutar cualquier ejercicio
python TP2_Ejercicio_01.py
python TP2_Ejercicio_12.py
# ... etc
```

**Requisitos:**
- Python 3.x instalado en tu sistema
- No se requieren librerías externas

---

## 📝 Ejercicios Realizados

### **Ejercicio 1** - Suma de Dos Números
Dados dos números enteros almacenados en variables, calcular su suma e imprimir el resultado.
```python
n1 = 2
n2 = 5
print(n1 + n2)  # Output: 7
```

### **Ejercicio 2** - Resta de Dos Números
Solicitar al usuario dos números enteros, calcular la resta y mostrar el resultado con un mensaje descriptivo.

### **Ejercicio 3** - Calculadora Básica
Solicitar dos números y realizar todas las operaciones básicas: suma, resta, multiplicación y división. Mostrar cada resultado con un mensaje descriptivo.

### **Ejercicio 4** - Mensaje de Bienvenida
Solicitar nombre y apellido por separado, luego mostrar un mensaje de bienvenida personalizado.
```python
# Ejemplo: "¡¡Bienvenido Julián Alvarez!!"
```

### **Ejercicio 5** - Concatenación de Strings
Similar al ejercicio 4, pero almacenando nombre y apellido en una sola variable antes de mostrar el mensaje.

### **Ejercicio 6** - Cálculo de Promedio
Solicitar dos números y calcular el promedio aritmético entre ellos.

### **Ejercicio 7** - Contador de Letras
Solicitar una palabra y mostrar cuántas letras tiene utilizando un bucle `for`.

### **Ejercicio 8** - Área de Triángulo
Solicitar la base y altura de un triángulo, calcular y mostrar su área usando la fórmula: `área = (base × altura) / 2`

### **Ejercicio 9** - Generador de Acrónimos
Solicitar 3 palabras y crear un acrónimo tomando la primera letra de cada una.
```python
# Ejemplo: Qatar, Argentina, Mundial → QAM
```

### **Ejercicio 10** - Cálculo de Porcentajes
Solicitar el total de alumnos, cantidad de mujeres y varones. Calcular y mostrar el porcentaje de cada género en el curso. Incluye validación de datos.

### **Ejercicio 11** - Slicing de Strings
Solicitar dos palabras y crear una nueva combinación:
- Tomar las primeras 3 letras de la primera palabra
- Tomar las primeras 2 letras de la segunda palabra
- Combinar ambas porciones

### **Ejercicio 12** - Calculadora Completa
Programa que realiza todas las operaciones aritméticas entre dos números: suma, resta, multiplicación, división y potencia. Incluye manejo de división por cero.

### **Ejercicio 13** - Sistema de Datos Personales
Solicitar nombre completo, DNI, edad y altura. Mostrar la información en dos líneas:
- Línea 1: Nombre completo y DNI
- Línea 2: Nombre completo, edad y altura

Incluye validaciones (DNI de 8 dígitos, edad válida) y formateo automático de mayúsculas.

### **Ejercicio 14** - Transformación de Texto
Solicitar un nombre completo y mostrarlo en tres formatos:
- Todas las letras en minúsculas
- Todas las letras en mayúsculas
- Solo la primera letra de cada palabra en mayúscula

### **Ejercicio 15** - Generador de Apellidos Compuestos
Solicitar los nombres completos de ambos padres y el nombre del hijo/a. Extraer los apellidos de los padres y formar el nombre completo del hijo/a con apellido compuesto.

**Técnica utilizada:** Método `split()` para separar strings y estructuras de datos (diccionarios).

---

## 🎯 Conceptos de Python Abordados

### Variables y Tipos de Datos
- ✅ Variables numéricas: `int`, `float`
- ✅ Variables de texto: `str`
- ✅ Conversión de tipos: `int()`, `float()`, `str()`

### Operadores Aritméticos
- ✅ Suma (`+`), Resta (`-`), Multiplicación (`*`)
- ✅ División (`/`), División entera (`//`), Módulo (`%`)
- ✅ Potencia (`**`)

### Entrada y Salida de Datos
- ✅ `input()` para solicitar datos al usuario
- ✅ `print()` para mostrar resultados
- ✅ f-strings para formateo de texto: `f"El resultado es {variable}"`

### Manipulación de Strings
- ✅ Concatenación de strings con `+`
- ✅ Slicing: `palabra[0:3]`, `palabra[:2]`
- ✅ Métodos: `.upper()`, `.lower()`, `.split()`
- ✅ Indexing: `palabra[0]` para acceder a caracteres

### Estructuras de Control Básicas
- ✅ Condicionales `if/elif/else` para validaciones
- ✅ Bucles `for` para iterar sobre strings

### Buenas Prácticas
- ✅ Validación de entrada de datos
- ✅ Mensajes descriptivos al usuario
- ✅ Comentarios explicativos en el código
- ✅ Manejo de casos especiales (división por cero)

---

## 💡 Aprendizajes Clave

Este trabajo práctico me permitió:

- Comprender el uso de **variables** para almacenar diferentes tipos de datos
- Dominar los **operadores aritméticos** y su aplicación en cálculos
- Practicar la **entrada de datos** del usuario con `input()`
- Aplicar **conversión de tipos** (casting) correctamente
- Manipular **strings** usando métodos y slicing
- Implementar **validaciones básicas** de datos
- Usar **f-strings** para formateo elegante de salidas
- Desarrollar lógica de programación secuencial

---