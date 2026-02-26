# Taller Semana 1 — Linux + Bash + Git (modo simple)

## Qué vas a hacer (en 15 segundos)

Vas a ejecutar un script Bash que:

1) Crea/valida estructura de proyecto.
2) Genera un CSV pequeño de ejemplo (si no existe).
3) Produce un reporte en `reports/validacion_inicial.txt`.
4) Lo subes a GitHub con commits.

## Dónde vas a trabajar

Todo el trabajo es en esta carpeta:

`talleres/talleres_semana_01/workspace/`

No copies nada a la raíz del repo.

## Pasos (hazlos en orden)

1) Abre este repo en **Codespaces** (botón Code → Codespaces → Create codespace).
2) En la terminal, entra al workspace:

   ```bash
   cd talleres/talleres_semana_01/workspace
   ```

## Ejecuta el script

```bash
bash scripts/setup_proyecto.sh
```

## Revisa el reporte

```bash
cat reports/validacion_inicial.txt
```

## Haz commit y push

```bash
git add talleres/taller_semana_01/workspace
git commit -m "feat: semana1 reporte validacion inicial"
git push
```

## Criterios de éxito (DoD)

* Existe talleres/taller_semana_01/workspace/reports/validacion_inicial.txt.

* El script corre 2 veces seguidas sin fallar (idempotente).

* El repo tiene al menos 1 commit tuyo con el resultado.

# Bonus (opcional)

Edita scripts/setup_proyecto.sh y agrega al reporte:

Top 3 sensores con más registros (usa cut | sort | uniq -c | sort -nr | head -n 3).

# Ejercicio

Realiza los ejercicios propuestos en el pdf, y deja evidencia del trabajo en tu git en la carpeta `talleres/taller_semana_01/workspace`
