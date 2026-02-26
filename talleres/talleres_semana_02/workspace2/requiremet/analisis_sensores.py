"""
TALLER 02: Análisis de Datos de Sensores IoT
=============================================

OBJETIVO:
Procesar 1440 lecturas (24 horas) de 5 sensores agrícolas distribuidos en una finca.
Calcular estadísticas, detectar periodos críticos y exportar resultados.
"""

import csv  # Importamos csv al inicio para que esté disponible globalmente

# ============================================================================
# TAREA 1: Completar función agrupar_por_sensor
# ============================================================================

def agrupar_por_sensor(lecturas):
    """
    Agrupa todas las lecturas por sensor_id.
    """
    grupos = {}

    for lectura in lecturas:
        sensor_id = lectura['sensor_id']

        # Si el sensor no existe en el diccionario, creamos su lista
        if sensor_id not in grupos:
            grupos[sensor_id] = []

        # Agregamos la lectura completa a la lista del sensor correspondiente
        grupos[sensor_id].append(lectura)

    return grupos


# ============================================================================
# TAREA 2: Completar función calcular_estadisticas
# ============================================================================

def calcular_estadisticas(lecturas_sensor):
    """
    Calcula estadísticas básicas de un conjunto de lecturas de un sensor.
    """
    # 1 y 2. Extraemos listas convirtiendo a float para poder calcular
    temps = [float(x['temperatura_c']) for x in lecturas_sensor]
    humedades = [float(x['humedad_pct']) for x in lecturas_sensor]

    # 3. Cuenta cuántas lecturas tienen luz_lux > 5000
    # Nota: Convertimos a float porque a veces el CSV trae '5000.0'
    conteo_luz = sum(1 for x in lecturas_sensor if float(x['luz_lux']) > 5000)

    cantidad = len(lecturas_sensor)

    # 4, 5 y 6. Cálculos y retorno
    return {
        'total_lecturas': cantidad,
        'temp_promedio': sum(temps) / cantidad if cantidad > 0 else 0,
        'temp_maxima': max(temps) if cantidad > 0 else 0,
        'temp_minima': min(temps) if cantidad > 0 else 0,
        'humedad_promedio': sum(humedades) / cantidad if cantidad > 0 else 0,
        'horas_luz': conteo_luz  # Retornamos el conteo crudo (lecturas)
    }


# ============================================================================
# TAREA 3: Completar función detectar_periodos_criticos
# ============================================================================

def detectar_periodos_criticos(lecturas_sensor, sensor_id):
    """
    Identifica periodos donde la temperatura supera 30°C por más de 1 hora.
    Nota: 1 hora = 12 lecturas (ya que son cada 5 minutos)
    """
    alertas = []
    contador_critico = 0

    for lectura in lecturas_sensor:
        temp = float(lectura['temperatura_c'])

        if temp > 30:
            contador_critico += 1
        else:
            # Si se rompe la racha, verificamos si duró más de 1 hora (12 lecturas)
            if contador_critico >= 12:
                horas = (contador_critico * 5) / 60
                alertas.append(f"[{sensor_id}] Temperatura crítica sostenida por {horas:.1f} horas")
            contador_critico = 0 # Reseteamos contador

    # Verificación final por si el periodo crítico termina justo al final del archivo
    if contador_critico >= 12:
        horas = (contador_critico * 5) / 60
        alertas.append(f"[{sensor_id}] Temperatura crítica sostenida por {horas:.1f} horas")

    return alertas


# ============================================================================
# TAREA 4: Completar función exportar_resumen
# ============================================================================

def exportar_resumen(estadisticas_por_sensor, nombre_archivo='resumen_sensores.csv'):
    """
    Exporta las estadísticas calculadas a un archivo CSV.
    """
    columnas = [
        'sensor_id', 'zona', 'total_lecturas', 'temp_promedio',
        'temp_maxima', 'temp_minima', 'humedad_promedio', 'horas_luz'
    ]

    try:
        # 'newline=""' es importante en Windows para evitar líneas en blanco extra
        with open(nombre_archivo, 'w', encoding='utf-8', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=columnas)

            writer.writeheader()

            # Escribimos las filas. .values() nos da la lista de diccionarios internos
            writer.writerows(estadisticas_por_sensor.values())

        print(f"  ✓ Archivo '{nombre_archivo}' generado exitosamente.")

    except IOError as e:
        print(f"  Error al escribir el archivo: {e}")


# ============================================================================
# FUNCIÓN PRINCIPAL
# ============================================================================

def main():
    """
    Función principal que orquesta todo el análisis.
    """
    print("="*70)
    print("ANÁLISIS DE SENSORES IoT - 24 HORAS")
    print("="*70)

    # PASO 1: Leer el CSV
    print("\n[1/5] Leyendo datos...")
    lecturas = []

    try:
        with open('sensores_24h.csv', 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for fila in reader:
                lecturas.append(fila)
    except FileNotFoundError:
        print("Error: No se encuentra el archivo 'sensores_24h.csv'. Asegúrate de estar en la carpeta correcta.")
        return

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
        # Aquí dividimos por 12 porque cada lectura son 5 minutos (60/5 = 12 lecturas por hora)
        print(f"  Horas con luz solar: {stats['horas_luz'] / 12:.1f}h")

    print("\n" + "="*70)
    print("✓ Análisis completado - Revisa resumen_sensores.csv")
    print("="*70)


if __name__ == "__main__":
    main()
