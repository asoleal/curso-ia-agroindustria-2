"""
TALLER 01: Automatización de Decisiones Agronómicas
====================================================

OBJETIVO:
Crear un sistema de evaluación automatizada que procese datos de 20 parcelas
y genere recomendaciones de riego, drenaje y ajuste de pH.

DATASET:
parcelas.csv contiene las siguientes columnas:
- parcela_id: identificador único (P001, P002, ...)
- zona: ubicación geográfica (Norte, Sur, Este, Oeste, Centro)
- cultivo: tipo de cultivo (Café, Cacao, Plátano, Yuca, Maíz)
- temperatura_c: temperatura del suelo en grados Celsius
- humedad_suelo_pct: porcentaje de humedad del suelo (0-100)
- ph: nivel de pH del suelo (4.5-8.0)

REGLAS DE NEGOCIO:
1. RIEGO: humedad < 40% → necesita riego
2. DRENAJE: humedad > 75% → necesita drenaje
3. pH BAJO: ph < 5.5 → necesita cal (encalado)
4. pH ALTO: ph > 7.5 → necesita azufre
5. TEMPERATURA CRÍTICA: temp > 30°C → alerta de estrés térmico

TAREAS A COMPLETAR:
"""

# ============================================================================
# TAREA 1: Completar la función evaluar_riego
# ============================================================================

def evaluar_riego(humedad):
    """
    Evalúa si una parcela necesita riego o drenaje según su humedad.

    Args:
        humedad (int): Porcentaje de humedad del suelo (0-100)

    Returns:
        str: Recomendación ("RIEGO URGENTE", "DRENAJE", "ÓPTIMO")

    Instrucciones:
    - Si la humedad es menor a 40%, retorna "RIEGO URGENTE"
    - Si la humedad es mayor a 75%, retorna "DRENAJE"
    - En cualquier otro caso, retorna "ÓPTIMO"
    - Usa condicionales if/elif/else
    """
    pass  # Reemplaza este pass con tu código


# ============================================================================
# TAREA 2: Completar la función evaluar_ph
# ============================================================================

def evaluar_ph(ph):
    """
    Evalúa si el suelo necesita ajuste de pH.

    Args:
        ph (float): Nivel de pH del suelo

    Returns:
        str: Recomendación ("APLICAR CAL", "APLICAR AZUFRE", "PH ÓPTIMO")

    Instrucciones:
    - Si el pH es menor a 5.5, retorna "APLICAR CAL"
    - Si el pH es mayor a 7.5, retorna "APLICAR AZUFRE"
    - En cualquier otro caso, retorna "PH ÓPTIMO"
    - Usa la misma estructura que evaluar_riego
    """
    pass  # Reemplaza este pass con tu código


# ============================================================================
# TAREA 3: Completar la función procesar_parcela
# ============================================================================

def procesar_parcela(parcela_id, zona, cultivo, temperatura, humedad, ph):
    """
    Procesa una parcela completa y genera un diccionario con recomendaciones.

    Args:
        parcela_id (str): ID de la parcela
        zona (str): Zona geográfica
        cultivo (str): Tipo de cultivo
        temperatura (float): Temperatura en °C
        humedad (int): Humedad en %
        ph (float): Nivel de pH

    Returns:
        dict: Diccionario con todas las recomendaciones

    Instrucciones:
    - Crea un diccionario con las siguientes claves:
      * 'parcela_id': asigna el parámetro parcela_id
      * 'zona': asigna el parámetro zona
      * 'cultivo': asigna el parámetro cultivo
      * 'riego': llama a evaluar_riego(humedad) y asigna el resultado
      * 'ph_accion': llama a evaluar_ph(ph) y asigna el resultado
      * 'alerta_termica': evalúa si temperatura > 30 (True/False)
    - Retorna el diccionario creado
    """
    pass  # Reemplaza este pass con tu código


# ============================================================================
# TAREA 4: Leer el archivo CSV y procesar todas las parcelas
# ============================================================================

def main():
    """
    Función principal que lee parcelas.csv y genera el reporte.

    Instrucciones:

    PARTE A - Lectura del CSV:
    1. Importa el módulo csv
    2. Crea una lista vacía llamada 'reportes'
    3. Abre el archivo 'parcelas.csv' en modo lectura con encoding utf-8
    4. Usa csv.DictReader para leer el archivo
    5. Recorre cada fila del CSV con un bucle for

    PARTE B - Procesamiento:
    6. Para cada fila, extrae los siguientes valores:
       - parcela_id (string, tal como viene)
       - zona (string)
       - cultivo (string)
       - temperatura_c (convierte a float)
       - humedad_suelo_pct (convierte a int)
       - ph (convierte a float)
    7. Llama a procesar_parcela() pasando estos 6 valores
    8. Agrega el resultado devuelto a la lista 'reportes'

    PARTE C - Estadísticas:
    9. Calcula el total de parcelas: len(reportes)
    10. Cuenta cuántas necesitan riego (busca "RIEGO" en r['riego'])
    11. Cuenta cuántas necesitan drenaje (busca "DRENAJE" en r['riego'])
    12. Cuenta cuántas tienen alerta térmica (r['alerta_termica'] == True)

    PARTE D - Impresión del reporte:
    13. Imprime un encabezado decorativo
    14. Imprime el resumen con los totales calculados
    15. Recorre la lista 'reportes' e imprime cada parcela con formato:
        [ID] Zona - Cultivo
          → Riego: recomendación
          → pH: acción
          → Alerta térmica: Sí/No
    16. Imprime mensaje de finalización
    """
    pass  # Reemplaza este pass con tu código


# ============================================================================
# EJECUCIÓN DEL PROGRAMA
# ============================================================================

if __name__ == "__main__":
    main()
