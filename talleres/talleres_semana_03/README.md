# Taller Semana 03: Computación de Alto Rendimiento (HPC) en el Agro

## 🎯 Objetivo
Aprender a procesar grandes volúmenes de datos agrícolas de forma eficiente. En este taller compararás el rendimiento de Python "puro" frente a la **vectorización con NumPy** y generarás un reporte técnico profesional.

## 📂 Archivos del Taller
- `data_generator.py`: Crea el dataset binario de humedad (`.npy`).
- `benchmark.py`: Compara tiempos de ejecución (Loop vs. NumPy).
- `vectorizacion.py`: **Tu área de trabajo** para implementar la lógica.
- `check_03.py`: Validador automático de tus ejercicios.
- `reporte/`: Carpeta con la plantilla LaTeX para tu informe.

## 🚀 Guía de Actividades

### 1. Generar la "Finca Digital"
Crea el archivo de datos que simularemos procesar:
```bash
python data_generator.py

```

### 2. Comprobar el Speedup

Ejecuta el benchmark para ver la diferencia de velocidad. **Anota el factor de aceleración** (ej. 50x más rápido) para tu reporte:

```bash
python benchmark.py

```

### 3. Implementar Soluciones

Abre `vectorizacion.py` y completa las tareas:

* **Tarea 1:** Limpieza de datos con `np.clip`.
* **Tarea 2:** Detección de sequía con máscaras booleanas.
* **Tarea 3:** Aplicación de riego con `np.where`.

### 4. Validar tu Código

Corre el script de pruebas para verificar que no usaste bucles `for` y que los resultados son correctos:

```bash
python check_03.py

```

### 5. Generar Reporte Técnico

Entra a la carpeta `reporte`, completa tus datos y resultados en el `.tex` y compila:

```bash
cd reporte && bash compile.sh

```

---

**Nota:** Este taller es parte del curso "IA para Agroindustria". ¡Asegúrate de hacer commit de tus avances!

