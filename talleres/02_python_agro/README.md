
# Taller 01 – Automatización de decisiones agronómicas 🌱

**Rol:** Ingeniero de Datos Agroindustrial
**Objetivo:** Construir un sistema simple que lea datos de parcelas desde un archivo CSV y genere recomendaciones de riego, drenaje y ajuste de pH.

---

## 1. Contexto del problema

Trabajas en una finca con sensores que registran temperatura, humedad del suelo y pH en diferentes parcelas.
Tu tarea es **automatizar las decisiones básicas** que hoy se toman “a mano”:

- ¿Qué parcelas necesitan riego?
- ¿Dónde hay exceso de agua y se requiere drenaje?
- ¿Qué suelos necesitan corrección de pH?

Para esto usarás **Python puro** (sin NumPy) y un archivo CSV con 20 parcelas.

---

## 2. Archivos del taller

Dentro de esta carpeta deberías tener:

```text
talleres/02_python_agro/
├── README.md              # Este archivo
├── check_01.py            # Validador automático
└── workspace/
    ├── parcelas.csv       # Dataset con 20 parcelas
    └── riego_automatico.py# Script base con TODOs y pistas
```

- `parcelas.csv`: contiene `parcela_id`, `zona`, `cultivo`, `temperatura_c`, `humedad_suelo_pct`, `ph`.
- `riego_automatico.py`: aquí vas a escribir TODO tu código.
- `check_01.py`: comprueba que tus funciones estén bien implementadas.

Trabaja **solo dentro de `workspace/`**, sin cambiar los nombres de los archivos.

---

## 3. Reglas de negocio

Estas son las reglas que tu código debe implementar:

1. **Riego**
    - Si `humedad < 40` → necesita riego.
2. **Drenaje**
    - Si `humedad > 75` → necesita drenaje.
3. **pH**
    - Si `ph < 5.5` → aplicar cal.
    - Si `ph > 7.5` → aplicar azufre.
    - En otro caso → pH óptimo.
4. **Alerta térmica**
    - Si `temperatura > 30` → alerta de estrés térmico.

Estas reglas ya están descritas en la cabecera de `riego_automatico.py` para que puedas consultarlas mientras programas.

---

## 4. Tareas paso a paso

Abre `workspace/riego_automatico.py`. Verás las tareas numeradas.

### 4.1 Tarea 1 – `evaluar_riego(humedad)`

- Completa la función `evaluar_riego` usando `if / elif / else`.
- Debe devolver uno de estos textos:
  - `"RIEGO URGENTE"`
  - `"DRENAJE"`
  - `"ÓPTIMO"`

Dentro del archivo tienes una pista con la estructura del condicional.

### 4.2 Tarea 2 – `evaluar_ph(ph)`

- Completa la función `evaluar_ph`.
- Debe devolver:
  - `"APLICAR CAL"` si `ph < 5.5`.
  - `"APLICAR AZUFRE"` si `ph > 7.5`.
  - `"PH ÓPTIMO"` en otro caso.

### 4.3 Tarea 3 – `procesar_parcela(...)`

- Debe construir y devolver un **diccionario** con las claves:
  - `'parcela_id'`
  - `'zona'`
  - `'cultivo'`
  - `'riego'` (usando `evaluar_riego(humedad)`)
  - `'ph_accion'` (usando `evaluar_ph(ph)`)
  - `'alerta_termica'` (`True` si `temperatura > 30`, si no `False`)

En el archivo ya tienes comentado un ejemplo de diccionario listo para copiar y adaptar.

### 4.4 Tarea 4 – `main()`

En la función `main()` debes:

1. Crear una lista vacía `reportes`.
2. Abrir `parcelas.csv` con `with open(...):`.
3. Crear un `csv.DictReader(f)` para leer cada fila como diccionario.
4. Recorrer las filas con `for fila in reader:`.
5. Para cada fila:
    - Convertir tipos:
        - `temperatura = float(fila['temperatura_c'])`
        - `humedad = int(fila['humedad_suelo_pct'])`
        - `ph = float(fila['ph'])`
    - Llamar a `procesar_parcela(...)`.
    - Agregar el resultado a `reportes`.
6. Calcular:
    - `total = len(reportes)`
    - `riego = sum(1 for r in reportes if "RIEGO" in r['riego'])`
    - `drenaje = sum(1 for r in reportes if "DRENAJE" in r['riego'])`
    - `alertas = sum(1 for r in reportes if r['alerta_termica'])`
7. Imprimir:
    - Un resumen con totales.
    - Las recomendaciones por parcela

---

## 5. Cómo probar tu solución

Desde la carpeta del taller:

```bash
cd talleres/02_python_agro/workspace
python riego_automatico.py
```

Deberías ver un **reporte de análisis** con todas las parcelas y sus recomendaciones.

Luego, ejecuta el validador:

```bash
cd ..
python check_01.py
```

- Si todo está bien, verás algo como:
`✓ APROBADO: 4/4 pruebas exitosas`
- Si falla, lee el mensaje de error, corrige tu código y vuelve a ejecutar.

---

## 6. Cómo entregar

1. Asegúrate de que el validador pase sin errores.
2. Desde la raíz del repo:

```bash
git add talleres/02_python_agro/01_decisiones/workspace/riego_automatico.py
git commit -m "Completo Taller 01: automatización de decisiones de riego"
git push
```

Con esto, el taller queda entregado y versionado como trabajo de un **ingeniero de datos agroindustrial**.
<span style="display:none">[^1]</span>

<div align="center">⁂</div>
