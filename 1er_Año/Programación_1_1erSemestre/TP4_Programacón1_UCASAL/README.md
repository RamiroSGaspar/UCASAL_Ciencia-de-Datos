# Trabajo Práctico 4 - Programación 1
**Universidad Católica de Salta (UCASAL)**  
**1er Año - 1er Semestre**  
**Alumno:** Ramiro Sebastián Gaspar

[![Java](https://img.shields.io/badge/Java-21-orange.svg)](https://www.oracle.com/java/)
[![POO](https://img.shields.io/badge/POO-Herencia-blue.svg)](https://github.com/RamiroSGaspar/UCASAL_Ciencia-de-Datos)
[![Status](https://img.shields.io/badge/Status-Completed-success.svg)](https://github.com/RamiroSGaspar/UCASAL_Ciencia-de-Datos)

---

## 📖 Descripción

Trabajo práctico enfocado en **Programación Orientada a Objetos (POO)** utilizando Java. Se desarrollaron ejercicios progresivos que cubren desde la creación básica de clases hasta conceptos avanzados como herencia, encapsulamiento y manejo de arrays de objetos.

**Autor:** Ramiro Sebastian Gaspar  
**Materia:** Programación 1  
**Institución:** Universidad Católica de Salta (UCASAL)

---

## 📂 Estructura del Repositorio
```
TP4_Programacón1_UCASAL/
├── src/
│   ├── ej1/          # Creación básica de clase Persona
│   ├── ej2/          # Instanciación de múltiples objetos
│   ├── ej3/          # Arrays de objetos Persona
│   ├── ej4/          # Recorrido de arrays con for
│   ├── ej5/          # Métodos personalizados (IMC, info, esMayorDeEdad)
│   ├── ej6/          # Entrada de datos con Scanner
│   ├── ej7/          # Herencia - Clase Profesor
│   ├── ej8/          # Arrays de objetos Profesor
│   ├── ej9/          # Filtrado de datos con condicionales
│   └── ej10/         # Integración completa con Scanner
├── .idea/            # Configuración de IntelliJ IDEA
├── .gitignore
└── Programacion1-tp4-Java.iml
```

---

## 📥 Instalación

### Opción 1: Clonar carpeta específica (recomendado)
```bash
# 1. Clonar el repositorio sin descargar archivos
git clone --no-checkout https://github.com/RamiroSGaspar/UCASAL_Ciencia-de-Datos.git
cd UCASAL_Ciencia-de-Datos

# 2. Configurar sparse-checkout
git sparse-checkout init --cone

# 3. Seleccionar solo esta carpeta
git sparse-checkout set "1er_Año/Programación_1_1erSemestre/TP4_Programacón1_UCASAL"

# 4. Descargar los archivos
git checkout main
```

### Opción 2: Clonar todo el repositorio
```bash
git clone https://github.com/RamiroSGaspar/UCASAL_Ciencia-de-Datos.git
cd UCASAL_Ciencia-de-Datos/1er_Año/Programación_1_1erSemestre/TP4_Programacón1_UCASAL
```

---

## 🛠️ Tecnologías Utilizadas

- **Java 21** - Lenguaje de programación
- **IntelliJ IDEA** - IDE de desarrollo
- **Scanner** - Entrada de datos por consola
- **POO** - Programación Orientada a Objetos

---

## 🚀 Cómo Ejecutar los Ejercicios

### Compilar y ejecutar desde terminal:
```bash
# Navegar al directorio src
cd src

# Compilar un ejercicio específico (ejemplo: ejercicio 1)
javac ej1/Persona.java ej1/Main.java

# Ejecutar
java ej1.Main
```

### Ejecutar desde IntelliJ IDEA:

1. Abrir el proyecto en IntelliJ IDEA
2. Navegar a la clase `Main` del ejercicio deseado
3. Click derecho → "Run 'Main.main()'"

**Requisitos:**
- JDK 21 o superior instalado
- IntelliJ IDEA (recomendado) o cualquier IDE compatible con Java

---

## 📝 Ejercicios Realizados

### **Ejercicio 1** - Creación de la Clase Persona
Crear una clase `Persona` con atributos: idPersona, dni, apellido, nombre, edad, género, peso, altura y domicilio. Implementar constructores vacío y completo, además de getters/setters.

### **Ejercicio 2** - Instanciación de Objetos
Crear 5 objetos de la clase `Persona` utilizando diferentes formas de inicialización (constructor completo y constructor vacío + setters).

### **Ejercicio 3** - Arrays de Objetos
Instanciar 10 objetos de la clase `Persona` y almacenarlos en un array. Practicar la inicialización masiva de objetos.

### **Ejercicio 4** - Recorrido con Bucle For
Recorrer el array de personas con un bucle `for` y mostrar todos los datos de cada objeto por pantalla de forma estructurada.

### **Ejercicio 5** - Métodos Personalizados
Implementar métodos en la clase `Persona`:
- **`info()`**: Devuelve cadena con DNI, Apellido, Nombre y Domicilio
- **`IMC()`**: Calcula el Índice de Masa Corporal y clasifica el resultado (peso ideal, bajo peso, sobrepeso)
- **`esMayorDeEdad()`**: Determina si la persona es mayor de 18 años (retorna boolean)

### **Ejercicio 6** - Entrada de Datos con Scanner
Crear programa que solicite al usuario el ingreso de datos de 3 personas mediante `Scanner`. Para cada persona:
- Mostrar información básica con `info()`
- Calcular y mostrar el IMC
- Verificar si es mayor de edad
- Incluir validaciones de entrada (DNI de 8 dígitos, edad 0-120, peso/altura positivos)

### **Ejercicio 7** - Herencia: Clase Profesor
Crear la clase `Profesor` que hereda de `Persona` y agrega:
- Atributo `materia` (String)
- Atributo `cargaHoraria` (int)
- Sobrescritura del método `info()` para incluir datos específicos de profesor

### **Ejercicio 8** - Arrays de Profesores
Instanciar 10 objetos de la clase `Profesor` y almacenarlos en un array. Mostrar información completa de cada profesor utilizando métodos heredados y propios.

### **Ejercicio 9** - Filtrado de Datos
Recorrer el array de profesores y mostrar únicamente aquellos que tienen una carga horaria superior a 10 horas semanales. Incluir resumen estadístico.

### **Ejercicio 10** - Sistema Completo con Scanner
Crear un sistema de registro de profesores que:
- Solicita datos de 3 profesores mediante `Scanner`
- Incluye validaciones robustas (DNI 8 dígitos, edad 18-70, peso/altura en rangos válidos)
- Permite filtrar profesores por carga horaria mínima
- Muestra información completa incluyendo IMC y estado de mayoría de edad
- Maneja excepciones con mensajes claros

---

## 🎯 Conceptos de POO Abordados

### Encapsulamiento
- ✅ Atributos privados con modificador `private`
- ✅ Acceso controlado mediante getters y setters
- ✅ Validaciones en setters (edad no negativa, peso/altura positivos)

### Constructores
- ✅ Constructor vacío `Persona()`
- ✅ Constructor completo con todos los parámetros
- ✅ Uso de `super()` en clases derivadas

### Herencia
- ✅ Clase `Profesor` extiende `Persona` usando `extends`
- ✅ Herencia de atributos y métodos
- ✅ Llamada al constructor padre con `super()`

### Polimorfismo
- ✅ Sobrescritura de métodos con `@Override`
- ✅ Método `toString()` personalizado
- ✅ Método `info()` extendido en clase hija

### Abstracción
- ✅ Métodos con lógica de negocio (IMC, esMayorDeEdad)
- ✅ Ocultamiento de detalles de implementación
- ✅ Interfaces claras mediante métodos públicos

---

## 💡 Aprendizajes Clave

Este trabajo práctico me permitió:

- Comprender los **4 pilares de la POO**: Encapsulamiento, Herencia, Polimorfismo y Abstracción
- Dominar la creación y uso de **constructores** en Java
- Implementar **herencia** para reutilizar código y extender funcionalidades
- Trabajar con **arrays de objetos** y su manipulación
- Utilizar la clase **Scanner** para entrada de datos con validaciones
- Aplicar **buenas prácticas** de programación (validaciones, manejo de excepciones)
- Desarrollar sistemas completos integrando múltiples conceptos

---

## 🔄 Progresión del Aprendizaje

| Ejercicio | Concepto Principal |
|-----------|-------------------|
| 1-2 | Creación básica de clases y objetos |
| 3-4 | Trabajo con arrays y estructuras de control |
| 5 | Métodos personalizados y lógica de negocio |
| 6 | Entrada de datos y validaciones |
| 7 | Herencia y extensión de clases |
| 8-9 | Manipulación de arrays de objetos heredados |
| 10 | Integración completa de todos los conceptos |

---

## 📊 Comparación con TPs Anteriores

| Aspecto | TP2 (Python) | TP3 (Básico Java) | TP4 (POO Java) |
|---------|--------------|-------------------|----------------|
| **Paradigma** | Estructurado | Estructurado | Orientado a Objetos |
| **Complejidad** | Baja | Media | Alta |
| **Conceptos** | Variables, ciclos | Sintaxis Java | Clases, herencia |
| **Entrada datos** | `input()` | `BufferedReader` | `Scanner` |
| **Estructuras** | Simples | Arrays básicos | Arrays de objetos |

---
