# Trabajo Práctico 4 - Programación 2
**Universidad Católica de Salta (UCASAL)**  
**1er Año - 2ndo Semestre**  
**Alumno:** Ramiro Sebastián Gaspar

---

## 📖 Descripción

Trabajo práctico enfocado en **estructuras de datos avanzadas, visualización de datos y análisis con Python**. Se desarrollaron 14 ejercicios progresivos que cubren diccionarios, lectura/procesamiento de archivos CSV, visualización con Matplotlib y análisis numérico con NumPy. Este TP representa la culminación del curso, integrando todos los conceptos aprendidos en un proyecto final de análisis de gastos mensuales.

---

## 📂 Estructura del Repositorio
```
TP4_Programación2_UCASAL/
├── TP4_Ejercicio_01.py        # Diccionarios básicos (stock)
├── TP4_Ejercicio_02.py        # Diccionarios con bucle infinito
├── TP4_Ejercicio_03.py        # Lectura CSV con DictReader
├── TP4_Ejercicio_04.py        # CSV con validaciones (propiedades)
├── TP4_Ejercicio_05.py        # Gráfico plot básico (población)
├── TP4_Ejercicio_06.py        # Multi line plot (gastos)
├── TP4_Ejercicio_07.py        # Plot + scatter con CSV ordenado
├── TP4_Ejercicio_08.py        # Gráfico de barras con filtrado
├── TP4_Ejercicio_09.py        # Gráfico con funciones matemáticas
├── TP4_Ejercicio_10.py        # Potencias con numpy
├── TP4_Ejercicio_11.py        # Operaciones básicas numpy
├── TP4_Ejercicio_12.py        # np.where para filtrado
├── TP4_Ejercicio_13.py        # Máscaras booleanas numpy
├── Ejercicio_14/              # Proyecto integrador final
│   ├── TP4_Ejercicio_14.py    # Sistema de análisis de gastos
│   └── GastosMensuales.csv    # Dataset de gastos
├── stock.csv                  # Datos para ejercicios 3
├── propiedades.csv            # Datos para ejercicio 4
└── poblacion.csv              # Datos para ejercicios 7-8
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
git sparse-checkout set "1er_Año/Programación_2_2ndoSemestre/TP4_Programación2_UCASAL"

# 4. Descargar los archivos
git checkout main
```

### Opción 2: Clonar todo el repositorio
```bash
git clone https://github.com/RamiroSGaspar/UCASAL_Ciencia-de-Datos.git
cd UCASAL_Ciencia-de-Datos/1er_Año/Programación_2_2ndoSemestre/TP4_Programación2_UCASAL
```

---

## 🛠️ Tecnologías Utilizadas

- **Python 3.12** - Lenguaje de programación
- **Diccionarios** - Estructura de datos clave-valor
- **CSV Module** - Lectura y procesamiento de archivos CSV
- **Matplotlib** - Visualización de datos (plot, scatter, bar)
- **NumPy** - Análisis numérico y operaciones con arrays
- **Funciones built-in** - zip(), sorted(), sum(), len(), max(), min()

---

## 🚀 Cómo Ejecutar los Ejercicios

**Requisitos:**
- Python 3.12 instalado en tu sistema
- Librerías: `matplotlib`, `numpy` (instalar con pip)
```bash
# Instalar dependencias
pip install matplotlib numpy

# Navegar a la carpeta del TP4
cd 1er_Año/Programación_2_2ndoSemestre/TP4_Programación2_UCASAL

# Ejecutar ejercicios básicos
python TP4_Ejercicio_01.py
python TP4_Ejercicio_05.py

# Ejecutar proyecto integrador
cd Ejercicio_14
python TP4_Ejercicio_14.py
```

---

## 📝 Ejercicios Realizados

Este trabajo práctico consta de 14 ejercicios organizados en cuatro bloques temáticos:

### **BLOQUE 1: Diccionarios y Estructuras de Datos (Ejercicios 1-2)**
Introducción a diccionarios como estructura de datos clave-valor. Se trabajan operaciones básicas (crear, agregar, acceder), métodos especiales (`.keys()`, `.values()`, `.items()`), y bucles infinitos con validaciones. El ejercicio 2 implementa un sistema de gestión de stock interactivo que acumula valores y valida entradas del usuario usando el operador `in`.

### **BLOQUE 2: Procesamiento de Archivos CSV (Ejercicios 3-4)**
Manejo de archivos CSV usando el módulo `csv` y la clase `DictReader`. Se practican patrones de lectura, iteración sobre filas, acumulación de valores numéricos, y validación de datos faltantes. El ejercicio 4 introduce manejo de errores con validaciones de campos vacíos y conversión segura de tipos de datos.

### **BLOQUE 3: Visualización con Matplotlib (Ejercicios 5-10)**
Creación de gráficos estadísticos profesionales usando Matplotlib. Se trabajan gráficos de línea simples y múltiples (`plot`), gráficos de dispersión (`scatter`), gráficos de barras (`bar`), personalización de ejes, títulos, etiquetas y leyendas. Los ejercicios integran lectura de CSV, ordenamiento de datos con `sorted()` y `zip()`, y visualización de funciones matemáticas usando NumPy.

### **BLOQUE 4: Análisis Numérico con NumPy (Ejercicios 11-13)**
Operaciones avanzadas con arrays de NumPy: creación de arrays, funciones de agregación (`sum()`, `average()`, `sort()`, `max()`, `min()`), filtrado condicional con `np.where()`, y máscaras booleanas para selección de datos. Estos ejercicios sientan las bases para análisis de datos científicos y estadísticos.

### **BLOQUE 5: Proyecto Integrador Final (Ejercicio 14)**
Sistema completo de análisis de gastos mensuales que integra todos los conceptos del curso. Incluye menú interactivo, lectura de CSV, diccionarios para agrupación de datos, múltiples tipos de gráficos (plot, scatter, bar), análisis estadístico con NumPy, y navegación por opciones usando estructuras `if/elif/else`. El proyecto demuestra dominio completo de programación procedural, análisis de datos y visualización.

---

## 🎯 Conceptos de Python Abordados

### Diccionarios y Estructuras de Datos
- ✅ Creación y manipulación de diccionarios
- ✅ Métodos: `.keys()`, `.values()`, `.items()`
- ✅ Operador `in` para verificar claves
- ✅ Acumulación de valores en diccionarios
- ✅ Diccionarios anidados

### Archivos CSV
- ✅ Módulo `csv` y clase `DictReader`
- ✅ Lectura de archivos con `open()` y `with`
- ✅ Iteración sobre filas de CSV
- ✅ Acceso a columnas por nombre
- ✅ Validación de campos vacíos (`.strip()`)
- ✅ Manejo de errores con validaciones

### Matplotlib - Visualización de Datos
- ✅ Gráficos de línea: `plt.plot()`
- ✅ Gráficos de dispersión: `plt.scatter()`
- ✅ Gráficos de barras: `plt.bar()`
- ✅ Multi-line plots con múltiples series
- ✅ Personalización: títulos, etiquetas, leyendas
- ✅ Configuración de ejes: `plt.xticks()`, `plt.yticks()`
- ✅ Grid y transparencia: `plt.grid(True, alpha=0.3)`
- ✅ Rotación de etiquetas: `rotation=45`
- ✅ Ajuste de diseño: `plt.tight_layout()`

### NumPy - Análisis Numérico
- ✅ Creación de arrays: `np.array()`, `np.linspace()`
- ✅ Operaciones matemáticas: `np.sqrt()`, potencias (`**`)
- ✅ Funciones de agregación: `np.sum()`, `np.average()`, `np.max()`, `np.min()`
- ✅ Ordenamiento: `np.sort()`
- ✅ Filtrado condicional: `np.where()`
- ✅ Máscaras booleanas para selección de datos

### Funciones Avanzadas de Python
- ✅ `zip()` - Emparejar múltiples listas
- ✅ `sorted()` - Ordenamiento con claves personalizadas
- ✅ `list()` - Conversión de iterables
- ✅ Listas por comprensión: `[nombres_meses[m] for m in datos.keys()]`
- ✅ Desempaquetado: `años, poblacion = zip(*datos)`

---

## 💡 Aprendizajes Clave

Este trabajo práctico me permitió:

- Dominar **diccionarios** como estructura de datos fundamental para agrupación y análisis
- Implementar **lectura y procesamiento de archivos CSV** de forma robusta
- Crear **visualizaciones profesionales** con Matplotlib (gráficos de línea, barras, dispersión)
- Aplicar **NumPy** para análisis numérico y operaciones con arrays
- Usar **funciones avanzadas** como `zip()`, `sorted()` y comprensiones de listas
- Desarrollar un **proyecto integrador completo** que combina todos los conceptos
- Implementar **menús interactivos** con navegación por opciones
- Manejar **validaciones robustas** con try-except y condicionales
- Aplicar **buenas prácticas** de organización de código en funciones
- Trabajar con **múltiples fuentes de datos** y análisis temporal

---

## 🏆 Proyecto Destacado: Sistema de Análisis de Gastos (Ejercicio 14)

El ejercicio integrador final es un **sistema completo de análisis financiero** que incluye:

### Características Principales:
- 📊 **Análisis Temporal**: Gastos mensuales y anuales
- 📈 **Múltiples Visualizaciones**: Gráficos de línea, barras y dispersión
- 🔍 **Análisis por Categorías**: Agrupación de gastos (Alimentación, Transporte, etc.)
- 📉 **Estadísticas Avanzadas**: Total, promedio, máximo, mínimo con NumPy
- 🎮 **Menú Interactivo**: Navegación intuitiva con 6 opciones
- 💾 **Persistencia de Datos**: Lectura de CSV con validaciones

### Tecnologías Integradas:
- Diccionarios para agrupación de datos por mes/año/categoría
- CSV para carga de dataset de gastos
- Matplotlib para 3 tipos de gráficos diferentes
- NumPy para análisis estadístico completo
- Bucles while para menú interactivo
- Funciones modulares para organización de código
- Manejo de errores con try-except

Este proyecto demuestra la capacidad de **integrar múltiples tecnologías** para crear una aplicación real de análisis de datos, preparándome para proyectos más complejos en Ciencia de Datos.

---