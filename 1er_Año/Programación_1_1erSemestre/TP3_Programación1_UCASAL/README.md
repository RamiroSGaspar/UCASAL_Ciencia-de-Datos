# Trabajo Práctico 3 - Programación 1
**Universidad Católica de Salta (UCASAL)**  
**1er Año - 1er Semestre**  
**Alumno:** Ramiro Sebastián Gaspar

---

## 📋 Descripción

Este trabajo práctico forma parte de la materia **Programación 1** y se enfoca en la introducción a **Java** como lenguaje de programación. Los ejercicios abordan conceptos fundamentales de programación estructurada implementados en Java.

---

## 📂 Contenido del Repositorio
```
TP3_Programación1_UCASAL/
├── src/                           # Código fuente Java
│   ├── Main.java                  # Archivo principal
│   ├── ej1.java a ej20.java      # 20 ejercicios resueltos
├── .idea/                         # Configuración IntelliJ IDEA
├── Programacion1-tp3-Java.iml     # Archivo de módulo IntelliJ
├── .gitignore                     # Archivos ignorados por Git
└── README.md                      # Este archivo
```

---

## 📥 Instalación

### Opción 1: Clonar solo este TP (Recomendado)

Si solo querés descargar este trabajo práctico sin clonar todo el repositorio:
```bash
# 1. Clonar el repositorio sin descargar archivos
git clone --no-checkout https://github.com/TU_USUARIO/UCASAL_Ciencia-de-Datos.git
cd UCASAL_Ciencia-de-Datos

# 2. Configurar sparse-checkout
git sparse-checkout init --cone

# 3. Seleccionar solo esta carpeta
git sparse-checkout set "1er_Año/Programación_1_1erSemestre/TP3_Programación1_UCASAL"

# 4. Descargar los archivos
git checkout main
```

### Opción 2: Clonar todo el repositorio
```bash
git clone https://github.com/TU_USUARIO/UCASAL_Ciencia-de-Datos.git
cd UCASAL_Ciencia-de-Datos/1er_Año/Programación_1_1erSemestre/TP3_Programación1_UCASAL
```

---

## 🛠️ Tecnologías Utilizadas

- **Java 21** - Lenguaje de programación
- **IntelliJ IDEA** - Entorno de desarrollo integrado (IDE)
- **BufferedReader** - Lectura de entrada de usuario

---

## 🚀 Cómo ejecutar los ejercicios

### Desde la terminal:
```bash
# Navegar a la carpeta src
cd src

# Compilar un ejercicio específico
javac ej1.java

# Ejecutar el ejercicio compilado
java ej1
```

### Desde IntelliJ IDEA:

1. Abrí el proyecto con IntelliJ IDEA
2. Navegá al archivo que querés ejecutar
3. Click derecho → "Run 'ejX.main()'"

**Requisitos:**
- Java Development Kit (JDK) 21 o superior
- IntelliJ IDEA (opcional, recomendado)

---

## 📝 Ejercicios Resueltos

### **Ejercicios 1-8: Fundamentos**
- **ej1**: Suma de dos números enteros
- **ej2**: Promedio de dos números
- **ej3**: Cálculo del área de un triángulo
- **ej4**: Verificación de mayoría de edad
- **ej5**: Sistema de calificaciones (Promocionado/Regular/Libre)
- **ej6**: Sistema de login con usuario y contraseña
- **ej7**: Aplicación de descuento (15%)
- **ej8**: Verificación de número par/impar

### **Ejercicios 9-15: Bucles FOR**
- **ej9**: Imprimir números del 1 al 30
- **ej10**: Imprimir números del 30 al 1 (descendente)
- **ej11**: Números pares entre 10 y 40
- **ej12**: Números impares entre 60 y 30 (descendente)
- **ej13**: Tabla de multiplicar del 6
- **ej14**: Múltiplos de 5 hasta 100
- **ej15**: Suma y producto de 5 números ingresados

### **Ejercicios 16-20: Bucles WHILE**
- **ej16**: Imprimir números del 1 al 30 con while
- **ej17**: Imprimir números del 30 al 1 con while
- **ej18**: Números impares entre 60 y 30 con while
- **ej19**: Tabla de multiplicar del 6 con while
- **ej20**: Imprimir números desde P hasta N (descendente)

---

## 📚 Conceptos Aplicados

- ✅ Entrada y salida de datos con `BufferedReader`
- ✅ Estructuras condicionales (`if`, `else if`, `else`)
- ✅ Operador ternario (`? :`)
- ✅ Bucles `for` y `while`
- ✅ Operadores aritméticos y lógicos
- ✅ Manejo de excepciones (`throws IOException`)
- ✅ Conversión de tipos de datos (`parseInt`, `parseDouble`)

---

## 💡 Aprendizajes Clave

Este trabajo práctico me permitió:
- Comprender la sintaxis básica de Java
- Dominar el uso de `BufferedReader` para entrada de datos
- Aplicar estructuras de control de flujo
- Diferenciar entre bucles `for` y `while`
- Implementar lógica condicional para resolver problemas

---

## 🔄 Diferencias con Python (TP2)

| Aspecto | Python | Java |
|---------|--------|------|
| **Entrada de datos** | `input()` | `BufferedReader.readLine()` |
| **Tipado** | Dinámico | Estático |
| **Declaración** | `variable = valor` | `tipo variable = valor;` |
| **Bloques** | Indentación | Llaves `{}` |
| **Impresión** | `print()` | `System.out.println()` |

---