# Procesamiento y análisis temporal de gases en Hermetia illucens

## Descripción

Este proyecto organiza, depura y analiza una base de datos de emisiones gaseosas medidas durante el proceso de *Hermetia illucens*. El enfoque se centra exclusivamente en las variables de concentración en **ppm** para CO2 y CH4, con separación por días, alineación temporal por jornada, generación de gráficos diarios, cálculo de pendientes y documentación técnica de cada transformación aplicada.

## Objetivo general

Construir un flujo de trabajo reproducible para:

- depurar la base de datos original,
- conservar únicamente las variables analíticas de interés en ppm,
- separar los datos por día,
- alinear temporalmente cada jornada,
- generar gráficos comparables,
- calcular pendientes de las curvas,
- y documentar la interpretación técnica de cada día analizado.

## Objetivos específicos

- Preservar intacto el archivo fuente.
- Crear una copia de trabajo para procesamiento.
- Conservar únicamente `created_at`, `entry_id`, `field2` y `field4`.
- Renombrar `field2` y `field4` como variables analíticas.
- Derivar una columna de fecha para segmentación diaria.
- Derivar una variable de tiempo relativo para comparación entre días.
- Generar salidas organizadas por carpeta.
- Mantener trazabilidad completa del proceso.

## Fuente de datos

- Archivo original: `datosbase.csv`
- Naturaleza de los datos: serie temporal de gases.
- Unidad de trabajo seleccionada: ppm.
- Variables de interés:
  - `field2`: CO2_ppm
  - `field4`: CH4_ppm

## Criterio de depuración

Se conservarán únicamente las siguientes columnas:

- `created_at`
- `entry_id`
- `field2`
- `field4`

Se eliminarán las siguientes columnas:

- `field1`
- `field3`
- `field5`
- `field6`
- `field7`
- `field8`
- `latitude`
- `longitude`
- `elevation`
- `status`

## Renombrado de variables

Las columnas conservadas deben renombrarse de la siguiente forma:

- `field2` -> `co2_ppm`
- `field4` -> `ch4_ppm`

## Estructura del proyecto

```text
proyecto_gases_hi/
├── README.md
├── data/
│   ├── raw/
│   │   └── datosbase.csv
│   ├── interim/
│   │   └── datos_filtrados_ppm.csv
│   └── processed/
│       ├── datos_limpios.csv
│       ├── datos_por_dia/
│       │   ├── 2025-08-10.csv
│       │   ├── 2025-08-18.csv
│       │   ├── 2025-08-19.csv
│       │   └── ...
│       └── resumen_pendientes.csv
├── reports/
│   ├── bitacora_limpieza.md
│   ├── analisis_por_dia.md
│   └── incidencias.md
├── figures/
│   ├── diarios/
│   │   ├── 2025-08-10_co2.png
│   │   ├── 2025-08-10_ch4.png
│   │   ├── 2025-08-10_conjunto.png
│   │   └── ...
│   └── comparativos/
│       ├── co2_todos_los_dias.png
│       └── ch4_todos_los_dias.png
└── scripts/
    ├── 01_preparacion_datos.py
    ├── 02_segmentacion_diaria.py
    ├── 03_graficos_diarios.py
    ├── 04_calculo_pendientes.py
    └── 05_reporte_analitico.py
```

## Convención de carpetas

### `data/raw/`
Contiene el archivo original sin modificaciones. Esta carpeta no debe alterarse durante ninguna etapa del proceso.

### `data/interim/`
Contiene archivos intermedios resultantes de la depuración inicial, antes de la separación por días.

### `data/processed/`
Contiene los archivos finales listos para análisis, incluyendo la base limpia general, los archivos separados por fecha y los resúmenes numéricos.

### `reports/`
Contiene la documentación del proceso, la bitácora de limpieza, el análisis técnico por jornada y el registro de incidencias.

### `figures/`
Contiene los gráficos diarios y comparativos generados a partir de las series temporales.

### `scripts/`
Contiene los scripts del flujo de trabajo, numerados según el orden de ejecución.

## Flujo de trabajo

### 1. Preservación del archivo fuente
El archivo original debe copiarse a `data/raw/` y mantenerse sin cambios durante todo el proyecto.

### 2. Depuración inicial
Se debe crear una copia de trabajo y eliminar las columnas que no forman parte del objetivo analítico. En esta etapa también debe verificarse que `created_at` tenga formato correcto de fecha-hora y que `entry_id` permanezca como identificador de referencia.

### 3. Estandarización de variables
Las variables `field2` y `field4` deben renombrarse a `co2_ppm` y `ch4_ppm`, respectivamente, para facilitar la interpretación y el análisis posterior.

### 4. Segmentación diaria
A partir de `created_at`, debe generarse una columna `fecha` que permita separar los registros por jornada. Cada día debe almacenarse como un archivo independiente en `data/processed/datos_por_dia/`.

### 5. Alineación temporal
Para cada día, debe calcularse un tiempo relativo con respecto al primer registro de la jornada. Esto permite comparar días distintos bajo un mismo origen temporal.

### 6. Generación de gráficos
Para cada jornada se deben producir gráficos de CO2, CH4 y, si es útil, una figura conjunta. Los nombres de los archivos deben seguir una convención consistente basada en la fecha y la variable.

### 7. Cálculo de pendientes
Para cada día deben calcularse pendientes de las curvas de CO2 y CH4. Estas pendientes pueden calcularse de manera global o por tramos, dependiendo del comportamiento de la señal.

### 8. Interpretación técnica
Cada jornada debe acompañarse de una nota técnica que describa el comportamiento observado, posibles picos, zonas estables, cambios bruscos y una hipótesis de relación con la dieta o con condiciones del proceso.

## Criterio de análisis

Durante la interpretación de resultados debe considerarse que:

- los valores bajos en una señal pueden coincidir con valores altos en la otra dentro del mismo día,
- estas variaciones pueden estar asociadas a la dieta aplicada,
- la dinámica diaria debe analizarse como respuesta del sistema biológico y no solo como una serie numérica.

## Productos esperados

Al finalizar el proceso, deben estar disponibles los siguientes productos:

- una base de datos limpia en ppm,
- archivos separados por día,
- gráficos diarios por variable,
- resumen de pendientes por jornada,
- bitácora de limpieza,
- reporte técnico diario,
- registro de incidencias y decisiones metodológicas.

## Trazabilidad

Toda modificación debe registrarse en `reports/bitacora_limpieza.md` indicando:

- fecha de ejecución,
- archivo afectado,
- transformación aplicada,
- columnas involucradas,
- criterio de decisión,
- justificación técnica,
- responsable del cambio.

## Archivo de bitácora sugerido

La bitácora debe registrar al menos:

- conservación del archivo original,
- eliminación de columnas,
- renombrado de variables,
- validación del formato temporal,
- separación por días,
- alineación de tiempo relativo,
- método usado para pendientes,
- incidencias encontradas durante el análisis.

## Convenciones de nombres

Se recomienda usar nombres consistentes y legibles:

- archivos diarios: `YYYY-MM-DD.csv`
- gráficos diarios: `YYYY-MM-DD_co2.png`, `YYYY-MM-DD_ch4.png`
- resumen de pendientes: `resumen_pendientes.csv`
- reporte técnico: `analisis_por_dia.md`

## Consideraciones metodológicas

- No modificar el archivo fuente.
- No eliminar registros sin justificación documentada.
- No mezclar limpieza de datos con interpretación biológica en un mismo paso.
- No calcular conclusiones antes de separar y alinear las series por día.
- Toda decisión debe quedar escrita para asegurar reproducibilidad.

## Resultado final

La salida del proyecto debe permitir un análisis técnico y reproducible del comportamiento diario de CO2 y CH4 en ppm, con series comparables entre jornadas, soporte gráfico, métricas de pendiente y documentación suficiente para auditoría metodológica.
