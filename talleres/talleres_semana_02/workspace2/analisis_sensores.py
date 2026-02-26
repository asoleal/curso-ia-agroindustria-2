"""
TALLER 02: Análisis de Datos de Sensores IoT
=============================================

OBJETIVO:
Procesar 1440 lecturas (24 horas) de 5 sensores agrícolas distribuidos en una finca.
Calcular estadísticas, detectar periodos críticos y exportar resultados.

DATASET:
sensores_24h.csv contiene:
- timestamp: fecha y hora de la lectura (2026-01-13 00:00:00)
- sensor_id: identificador del sensor (S001-S005)
- zona: ubicación (Norte, Sur, Este, Oeste, Centro)
- temperatura_c: temperatura en °C
- humedad_pct: porcentaje de humedad
- luz_lux: nivel de luz en lux (0 = noche, >5000 = día)

CADA SENSOR TOMA UNA LECTURA CADA 5 MINUTOS (288 lecturas en 24h)
TOTAL: 5 sensores × 288 lecturas = 1440 registros

TAREAS A COMPLETAR:
"""

# ============================================================================
# TAREA 1: Completar función agrupar_por_sensor
# ============================================================================

def agrupar_por_sensor(lecturas):
    """
    Agrupa todas las lecturas por sensor_id.

    Args:
        lecturas (list): Lista de diccionarios con datos del CSV

    Returns:
        dict: Diccionario donde cada clave es un sensor_id y 
              cada valor es una lista de todas sus lecturas

    Ejemplo de estructura de retorno:
    {
        'S001': [lectura1, lectura2, lectura3, ...],
        'S002': [lectura1, lectura2, ...]
    }

    Instrucciones:
    1. Crea un diccionario vacío llamado 'grupos'
    2. Recorre cada lectura en la lista 'lecturas'
    3. Obtén el sensor_id de la lectura
    4. Si ese sensor_id no está en el diccionario, créalo con una lista vacía
    5. Agrega la lectura completa a la lista del sensor correspondiente
    6. Retorna el diccionario 'grupos'
    """
    pass  # Reemplaza con tu código


# ============================================================================
# TAREA 2: Completar función calcular_estadisticas
# ============================================================================

def calcular_estadisticas(lecturas_sensor):
    """
    Calcula estadísticas básicas de un conjunto de lecturas de un sensor.

    Args:
        lecturas_sensor (list): Lista de lecturas de un solo sensor

    Returns:
        dict: Diccionario con estadísticas calculadas

    Estructura de retorno:
    {
        'total_lecturas': int,
        'temp_promedio': float,
        'temp_maxima': float,
        'temp_minima': float,
        'humedad_promedio': float,
        'horas_luz': int  # Cuántas lecturas con luz_lux > 5000
    }

    Instrucciones:
    1. Extrae todas las temperaturas en una lista
    2. Extrae todas las humedades en una lista
    3. Cuenta cuántas lecturas tienen luz_lux > 5000
    4. Calcula promedios usando sum() y len()
    5. Usa max() y min() para temperatura
    6. Retorna un diccionario con todas las estadísticas

    Nota: Recuerda convertir los valores a float donde sea necesario
    """
    pass  # Reemplaza con tu código


# ============================================================================
# TAREA 3: Completar función detectar_periodos_criticos
# ============================================================================

def detectar_periodos_criticos(lecturas_sensor, sensor_id):
    """
    Identifica periodos donde la temperatura supera 30°C por más de 1 hora.

    Args:
        lecturas_sensor (list): Lecturas de un sensor
        sensor_id (str): ID del sensor (para mensajes)

    Returns:
        list: Lista de strings con alertas encontradas

    Instrucciones:
    1. Crea una lista vacía 'alertas'
    2. Inicializa un contador de lecturas críticas en 0
    3. Recorre cada lectura
    4. Si temperatura_c > 30, incrementa el contador
    5. Si temperatura_c <= 30, verifica si el contador >= 12 (1 hora)
       - Si es así, agrega una alerta a la lista
       - Resetea el contador a 0
    6. Al final del bucle, verifica una última vez el contador
    7. Retorna la lista de alertas

    Formato de alerta sugerido:
    f"[{sensor_id}] Temperatura crítica sostenida por {horas} horas"
    """
    pass  # Reemplaza con tu código


# ============================================================================
# TAREA 4: Completar función exportar_resumen
# ============================================================================

def exportar_resumen(estadisticas_por_sensor, nombre_archivo='resumen_sensores.csv'):
    """
    Exporta las estadísticas calculadas a un archivo CSV.

    Args:
        estadisticas_por_sensor (dict): Diccionario con sensor_id como clave
                                        y estadísticas como valor
        nombre_archivo (str): Nombre del archivo de salida

    Instrucciones:
    1. Importa csv
    2. Define las columnas del CSV: 
       ['sensor_id', 'zona', 'total_lecturas', 'temp_promedio', 
        'temp_maxima', 'temp_minima', 'humedad_promedio', 'horas_luz']
    3. Abre el archivo en modo escritura con encoding utf-8
    4. Crea un csv.DictWriter con las columnas definidas
    5. Escribe el encabezado con writeheader()
    6. Recorre estadisticas_por_sensor y escribe cada fila con writerow()
    7. Imprime mensaje de confirmación

    Nota: Cada valor del diccionario debe tener la clave 'zona' además 
    de las estadísticas
    """
    pass  # Reemplaza con tu código


# ============================================================================
# FUNCIÓN PRINCIPAL
# ============================================================================

def main():
    """
    Función principal que orquesta todo el análisis.

    Flujo del programa:
    1. Leer sensores_24h.csv
    2. Agrupar lecturas por sensor
    3. Calcular estadísticas de cada sensor
    4. Detectar periodos críticos
    5. Exportar resumen a CSV
    6. Imprimir reporte en consola
    """
    import csv

    print("="*70)
    print("ANÁLISIS DE SENSORES IoT - 24 HORAS")
    print("="*70)

    # PASO 1: Leer el CSV
    print("\n[1/5] Leyendo datos...")
    lecturas = []

    with open('sensores_24h.csv', 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for fila in reader:
            lecturas.append(fila)

    print(f"  ✓ {len(lecturas)} lecturas cargadas")

    # PASO 2: Agrupar por sensor
    print("\n[2/5] Agrupando por sensor...")
    grupos = agrupar_por_sensor(lecturas)
    print(f"  ✓ {len(grupos)} sensores identificados")

    # PASO 3: Calcular estadísticas
    print("\n[3/5] Calculando estadísticas...")
    estadisticas = {}

    for sensor_id, lecturas_sensor in grupos.items():
        stats = calcular_estadisticas(lecturas_sensor)
        stats['sensor_id'] = sensor_id
        stats['zona'] = lecturas_sensor[0]['zona']  # Toma la zona de la primera lectura
        estadisticas[sensor_id] = stats

    print(f"  ✓ Estadísticas calculadas para {len(estadisticas)} sensores")

    # PASO 4: Detectar periodos críticos
    print("\n[4/5] Detectando periodos críticos...")
    todas_alertas = []

    for sensor_id, lecturas_sensor in grupos.items():
        alertas = detectar_periodos_criticos(lecturas_sensor, sensor_id)
        todas_alertas.extend(alertas)

    if todas_alertas:
        print(f"  ⚠ {len(todas_alertas)} alertas detectadas:")
        for alerta in todas_alertas:
            print(f"    {alerta}")
    else:
        print("  ✓ No se detectaron periodos críticos")

    # PASO 5: Exportar resumen
    print("\n[5/5] Exportando resumen...")
    exportar_resumen(estadisticas)

    # REPORTE FINAL
    print("\n" + "="*70)
    print("RESUMEN POR SENSOR")
    print("="*70)

    for sensor_id, stats in estadisticas.items():
        print(f"\n[{sensor_id}] {stats['zona']}")
        print(f"  Lecturas: {stats['total_lecturas']}")
        print(f"  Temperatura: {stats['temp_promedio']:.1f}°C (min: {stats['temp_minima']:.1f}°C, max: {stats['temp_maxima']:.1f}°C)")
        print(f"  Humedad promedio: {stats['humedad_promedio']:.1f}%")
        print(f"  Horas con luz solar: {stats['horas_luz'] / 12:.1f}h")  # Convertir lecturas a horas

    print("\n" + "="*70)
    print("✓ Análisis completado - Revisa resumen_sensores.csv")
    print("="*70)


if __name__ == "__main__":
    main()
