
# Taller Semana 2.1 — Automatización de Decisiones Agronómicas

## Qué vas a hacer (en 15 segundos)

Vas a completar un script Python que:

1. Lee un CSV con 20 parcelas agrícolas
2. Evalúa condiciones de riego, pH y temperatura
3. Genera recomendaciones automatizadas por parcela
4. Valida tu código con un script automático

## Dónde vas a trabajar

Todo el trabajo es en esta carpeta:

`talleres/taller_semana_02/workspace1/`

No modifiques archivos fuera de esta carpeta.

## Pasos (hazlos en orden)

### 1. Abre el archivo base

```bash
cd talleres/taller_semana_02/workspace1
```

 Debes ver el archivo `riego_automatico.py`

### 2. Completa las 4 funciones

Busca los comentarios `# TODO:` y completa:

* `evaluar_riego(humedad)` → Retorna "RIEGO URGENTE", "DRENAJE" o "ÓPTIMO"
* `evaluar_ph(ph)` → Retorna "APLICAR CAL", "APLICAR AZUFRE" o "PH ÓPTIMO"
* `procesar_parcela(...)` → Retorna diccionario con recomendaciones
* `main()` → Lee CSV, procesa y genera reporte

**Pistas:** Revisa el archivo `requirements/riego_automatico.py` si necesitas ayuda.

### 3. Ejecuta tu solución

Una vez hayas terminado de completar las actividades:

```bash
python riego_automatico.py
```

Deberías ver un reporte con 20 parcelas analizadas.

### 4. Valida con el checker

El archivo `check_01` permite evaluar que hayas avanzado en el programa:

```bash
python check_01.py
```

Si todo está bien, verás: `✓ APROBADO: 4/4 pruebas exitosas`

### 5. Haz commit

```bash
git add talleres/taller_semana_02/workspace1/riego_automatico.py
git commit -m "Completar taller 2.1 automatización de riego"
git push
```

## Criterios de éxito (DoD)

* [x] `check_01.py` pasa sin errores (4/4 pruebas)
* [x] `python riego_automatico.py` genera reporte completo
* [x] Al menos 1 commit con tu código en GitHub

## Conceptos clave practicados

* Condicionales `if/elif/else`
* Funciones con argumentos y retorno
* Diccionarios (estructuras de datos)
* Lectura de CSV con `csv.DictReader`
* Conversión de tipos (`float()`, `int()`)

## Si tienes errores

**Error de indentación:** Verifica que uses 4 espacios (no tabs)
**Error de import:** Asegúrate de estar en `workspace1/` al ejecutar
**Validador falla:** Lee el mensaje de error, te indica exactamente qué está mal

<div align="center">⁂</div>
