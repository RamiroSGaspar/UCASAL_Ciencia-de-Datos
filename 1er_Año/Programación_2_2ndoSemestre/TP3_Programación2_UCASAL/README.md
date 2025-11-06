# Trabajo Práctico 2 - Programación 2
**Universidad Católica de Salta (UCASAL)**  
**1er Año - 2ndo Semestre**  
**Alumno:** Ramiro Sebastián Gaspar

---

## 📖 Descripción

Trabajo práctico enfocado en **estructuras de control de flujo en Python**. Se desarrollaron 30 ejercicios progresivos que cubren condicionales (`if/elif/else`, `match/case`), bucles (`for`, `while`), listas, validaciones y operadores lógicos. Este TP marca la transición desde programación secuencial hacia programación con control de flujo y estructuras iterativas.

---

## 📂 Estructura del Repositorio
```
TP3_Programación2_UCASAL/
├── TP3_Ejercicio_01.py    # Consumo de combustible (km/litro)
├── TP3_Ejercicio_02.py    # Descuento del 15%
├── TP3_Ejercicio_03.py    # Verificar par/impar
├── TP3_Ejercicio_04.py    # Validar vocales
├── TP3_Ejercicio_05.py    # Operaciones con 3 números
├── TP3_Ejercicio_06.py    # Conversión °F a °C
├── TP3_Ejercicio_07.py    # Examen múltiple choice
├── TP3_Ejercicio_08.py    # Clasificador de notas (match/case)
├── TP3_Ejercicio_09.py    # Comparaciones y validaciones múltiples
├── TP3_Ejercicio_10.py    # Diferencia entre números
├── TP3_Ejercicio_11.py    # Verificar par/impar (3 números)
├── TP3_Ejercicio_12.py    # Temperaturas (máx, mín, promedio)
├── TP3_Ejercicio_13.py    # Números del 1 al 30 (ascendente)
├── TP3_Ejercicio_14.py    # Números del 20 al 1 (descendente)
├── TP3_Ejercicio_15.py    # Números pares entre 10 y 40
├── TP3_Ejercicio_16.py    # Números impares 60-30 (descendente)
├── TP3_Ejercicio_17.py    # Tabla de multiplicar del 6
├── TP3_Ejercicio_18.py    # Múltiplos de 5 (1-100)
├── TP3_Ejercicio_19.py    # Rango entre N y P
├── TP3_Ejercicio_20.py    # Repetir nombre N veces
├── TP3_Ejercicio_21.py    # Todas las tablas del 1 al 10
├── TP3_Ejercicio_22.py    # Suma y producto de 5 números
├── TP3_Ejercicio_23.py    # Promedio de edades
├── TP3_Ejercicio_24.py    # Suma pares y producto impares
├── TP3_Ejercicio_25.py    # Múltiplos de 3 y 5
├── TP3_Ejercicio_26.py    # Contadores múltiples
├── TP3_Ejercicio_27.py    # Promedios (total y positivos)
├── TP3_Ejercicio_28.py    # Contar negativos en rango
├── TP3_Ejercicio_29.py    # Promedio con rango personalizado
└── TP3_Ejercicio_30.py    # Calculadora con bucle infinito
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
git sparse-checkout set "1er_Año/Programación_2_2ndoSemestre/TP3_Programación2_UCASAL"

# 4. Descargar los archivos
git checkout main
```

### Opción 2: Clonar todo el repositorio
```bash
git clone https://github.com/RamiroSGaspar/UCASAL_Ciencia-de-Datos.git
cd UCASAL_Ciencia-de-Datos/1er_Año/Programación_2_2ndoSemestre/TP3_Programación2_UCASAL
```

---

## 🛠️ Tecnologías Utilizadas

- **Python 3.12** - Lenguaje de programación
- **Estructuras condicionales** - if/elif/else, match/case
- **Bucles** - for, while, range()
- **Listas** - Almacenamiento y manipulación de datos
- **Módulo math** - math.prod() para producto de elementos
- **Funciones built-in** - max(), min(), sum(), len()

---

## 🚀 Cómo Ejecutar los Ejercicios
```bash
# Navegar a la carpeta del TP3
cd 1er_Año/Programación_2_2ndoSemestre/TP3_Programación2_UCASAL

# Ejecutar cualquier ejercicio
python TP3_Ejercicio_01.py
python TP3_Ejercicio_30.py
# ... etc
```

**Requisitos:**
- Python 3.12 instalado en tu sistema
- Módulo `math` (incluido en Python estándar)

---

## 📝 Ejercicios Realizados

Este trabajo práctico consta de 30 ejercicios organizados en tres bloques temáticos:

### **BLOQUE 1: Condicionales Básicos (Ejercicios 1-12)**
Ejercicios enfocados en el uso de estructuras condicionales simples y múltiples. Se trabajan conceptos como validación de datos, comparaciones numéricas, conversión de unidades, clasificación de valores y toma de decisiones. Destacan ejercicios como el clasificador de notas usando `match/case`, el examen múltiple choice con validaciones, y análisis de temperaturas usando funciones como `max()`, `min()` y `sum()`.

### **BLOQUE 2: Bucles For Básicos (Ejercicios 13-21)**
Introducción al uso de bucles `for` con la función `range()` en sus diferentes variantes (ascendente, descendente, con paso). Se practican patrones de iteración para generar secuencias numéricas, filtrar números pares/impares, calcular múltiplos, y generar tablas de multiplicar. El ejercicio 21 integra bucles anidados para crear todas las tablas del 1 al 10.

### **BLOQUE 3: Bucles con Listas y Acumuladores (Ejercicios 22-30)**
Ejercicios avanzados que combinan bucles, listas, acumuladores y funciones de agregación. Se trabajan patrones como filtrado de datos, contadores, cálculo de promedios selectivos, y análisis estadístico de conjuntos de números. El ejercicio final (30) es una calculadora interactiva completa que integra todos los conceptos: bucles infinitos, validaciones, operadores aritméticos y control de flujo con `break`.

---

## 🎯 Conceptos de Python Abordados

### Estructuras Condicionales
- ✅ `if/elif/else` para decisiones múltiples
- ✅ `match/case` para selección estructurada
- ✅ Operadores de comparación: `==`, `!=`, `<`, `>`, `<=`, `>=`
- ✅ Operadores lógicos: `and`, `or`, `not`
- ✅ Condicionales anidados

### Bucles y Estructuras Iterativas
- ✅ `for` con `range()` en diferentes formas
- ✅ `while` para validaciones y bucles condicionales
- ✅ Bucles anidados
- ✅ `break` para salir de bucles

### Listas y Manipulación de Datos
- ✅ Crear y manipular listas: `[]`, `.append()`
- ✅ Iterar sobre listas: `for elemento in lista`
- ✅ Funciones de agregación: `sum()`, `len()`, `max()`, `min()`
- ✅ `math.prod()` para producto de elementos

### Validaciones y Manejo de Errores
- ✅ Validación de entrada de datos
- ✅ Manejo de división por cero
- ✅ Bucles de validación con `while True`
- ✅ Validación de rangos numéricos

---

## 💡 Aprendizajes Clave

Este trabajo práctico me permitió:

- Dominar el uso de **estructuras condicionales** para control de flujo
- Implementar **bucles for** con diferentes configuraciones de `range()`
- Trabajar con **listas** para almacenar y procesar múltiples datos
- Usar **acumuladores** para cálculos iterativos (sumas, productos)
- Aplicar **validaciones robustas** de entrada de usuario
- Combinar **múltiples conceptos** en programas complejos
- Desarrollar **lógica algorítmica** para resolver problemas
- Usar **bucles anidados** para procesos bidimensionales

---