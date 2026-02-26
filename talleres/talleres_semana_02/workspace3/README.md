# Taller Semana 2.3 — Introducción a NumPy y Vectorización

## Qué vas a hacer (en 15 segundos)

Vas a comparar el rendimiento de Python nativo vs NumPy para:

1. Procesar una matriz de humedad (365 días × 100 zonas)
2. Medir speedup con benchmark
3. Aplicar máscaras booleanas y np.where
4. Generar tu primer reporte en LaTeX

## Dónde vas a trabajar

`talleres_semana_02/workspace3/`

## Pasos (hazlos en orden)

### 1. Genera el dataset NumPy

```bash
cd talleres_semana_02/workspace3
python -c "import numpy as np; np.save('humedad_finca.npy', np.random.rand(365, 100))"
```

### ¿Qué es el archivo .npy?

Es un archivo binario de NumPy que almacena matrices de forma eficiente.
Para este taller, simulas 1 año de datos de humedad con:

- `np.random.rand(365, 100)`: Genera números aleatorios [0,1]
- `* 100`: Convierte a porcentajes [0,100]
- `np.save()`: Guarda en disco (más rápido que CSV para arrays grandes)

### 2. Ejecuta el benchmark

```bash
python benchmark.py
```

Deberías ver el speedup (cuántas veces más rápido es NumPy).

### 3. Completa vectorizacion.py

```bash
vectorizacion.py
```

Busca los `# TODO:` y completa las funciones.

### 4. Valida tu código

```bash
python check_03.py
```

### 5. Compila el reporte LaTeX

```bash
cd reporte
bash compile.sh
```

### 6. Haz commit

```bash
git add talleres_semana_02/workspace3/
git commit -m "feat: completar taller 02.3 NumPy y vectorización"
git push
```

## Criterios de éxito (DoD)

- [x] `check_03.py` pasa sin errores
- [x] `reporte/reporte.pdf` se genera correctamente
- [x] Entiendes la diferencia entre loop y vectorización
