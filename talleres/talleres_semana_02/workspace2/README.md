# Taller Semana 2.2 — Análisis de Sensores IoT

## 🎯 Qué vas a hacer (en 15 segundos)

Vas a procesar **1440 lecturas** de 5 sensores agrícolas (24 horas de datos) para:

1.  **Agrupar** lecturas por sensor usando diccionarios.
2.  **Calcular estadísticas** (promedio, máximos, mínimos, horas de luz).
3.  **Detectar periodos críticos** (temperatura > 30°C por más de 1 hora continua).
4.  **Exportar un resumen** consolidado a CSV.

---

## 📂 Dónde vas a trabajar

Todo el trabajo se realiza en esta carpeta:

`talleres/taller_semana_02/workspace2/`

Archivos clave:
*   `analisis_sensores.py` → **Tu código va aquí**
*   `sensores_24h.csv` → Los datos crudos (no modificar)
*   `check_02.py` → Script de validación automática

---

## 📝 Pasos (hazlos en orden)

### 1. Preparación

Abre la terminal en la carpeta correcta:

```bash
cd talleres/taller_semana_02/workspace2
```


### 2. Completa las 4 funciones

Abre `analisis_sensores.py`, busca los comentarios `# TODO` o `# TAREA X` y completa la lógica:

* **`agrupar_por_sensor(lecturas)`**
    * *Objetivo:* Convertir una lista plana en un diccionario `{ 'S001': [lecturas...], 'S002': ... }`.
* **`calcular_estadisticas(lecturas_sensor)`**
    * *Objetivo:* Calcular promedios y máximos/mínimos.
    * *Ojo:* Recuerda convertir los strings del CSV a `float`.
    * *Horas Luz:* Cuenta cuántas lecturas tienen `luz_lux > 5000`.
* **`detectar_periodos_criticos(...)`**
    * *Objetivo:* Detectar si la temperatura supera 30°C durante **más de 1 hora seguida**.
    * *Pista:* Como las lecturas son cada 5 minutos, 1 hora equivale a **12 lecturas consecutivas**.
* **`exportar_resumen(...)`**
    * *Objetivo:* Usar `csv.DictWriter` para guardar el archivo `resumen_sensores.csv`.


### 3. Ejecuta tu solución

Prueba tu código para ver si funciona y genera el reporte en pantalla:

```bash
python analisis_sensores.py
```

Deberías ver un output similar a:

```text
[4/5] Detectando periodos críticos...
  ⚠ 2 alertas detectadas:
    [S003] Temperatura crítica sostenida por 1.2 horas
    ...
[5/5] Exportando resumen...
  ✓ Archivo 'resumen_sensores.csv' generado exitosamente.
```


### 4. Valida tu código

Usa el validador automático para asegurarte de que cumples todos los requisitos:

```bash
python check_02.py
```

Si todo está correcto, verás: `✓ APROBADO: 4/4 pruebas exitosas`.

### 5. Entrega (Git)

```bash
git add analisis_sensores.py resumen_sensores.csv
git commit -m "feat: completar taller 02.2 análisis de sensores"
git push
```


---

## ✅ Criterios de Éxito (DoD)

* [ ] `check_02.py` pasa sin errores (4/4 pruebas).
* [ ] Se genera el archivo `resumen_sensores.csv` con 5 filas (una por sensor).
* [ ] El programa detecta y muestra las alertas de temperatura en la consola.
* [ ] Tu código está subido al repositorio.


## 💡 Tips para no atascarse

* **KeyError:** Verifica que estés usando las claves exactas del CSV: `sensor_id`, `temperatura_c`, `humedad_pct`, `luz_lux`.
* **TypeError:** El CSV lee todo como texto. ¡Usa `float()` antes de sumar o comparar!
* **CSV Vacío:** ¿Llamaste a `writer.writeheader()` antes de `writer.writerows()`?

```
<span style="display:none">[^1][^2]</span>

<div align="center">⁂</div>

[^1]: manual02.pdf
[^2]: sensores_24h.csv```

