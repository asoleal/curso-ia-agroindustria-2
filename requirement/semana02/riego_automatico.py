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
# Esta función debe retornar una recomendación según la humedad del suelo.
# Entrada: humedad (int) - porcentaje de humedad del suelo
# Salida: string con la recomendación

def evaluar_riego(humedad):
    """
    Evalúa si una parcela necesita riego o drenaje según su humedad.

    Args:
        humedad (int): Porcentaje de humedad del suelo (0-100)

    Returns:
        str: Recomendación ("RIEGO URGENTE", "DRENAJE", "ÓPTIMO")
    """
    #: Completa esta función según las reglas de negocio
    # Pista: usa if/elif/else para verificar los rangos

    # Elimina esta línea y escribe tu código aquí
    if humedad < 40:
        return "RIEGO"
    elif humedad > 75:
        return "DRENAJE"
    else:
        return "ÓPTIMO"

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
    """
    # TODO: Completa esta función
    # Recuerda: pH < 5.5 necesita cal, pH > 7.5 necesita azufre

    if ph < 5.5:
        return "CAL"
    elif ph > 7.5:
        return "AZUFRE"
    else:
        return "ÓPTIMO"


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
    """
    # TODO: Crea un diccionario con las siguientes claves:
    # - 'parcela_id'
    # - 'zona'
    # - 'cultivo'
    # - 'riego' (usa evaluar_riego)
    # - 'ph_accion' (usa evaluar_ph)
    # - 'alerta_termica' (True si temperatura > 30, False si no)

    resultado = {
        'parcela_id':parcela_id,
        'zona': zona,
        'cultivo':cultivo,
        'riego':evaluar_riego(humedad),
        'ph_accion':evaluar_ph,
        'alerta_termica': temperatura > 30
        }
    return resultado

# ============================================================================
# TAREA 4: Leer el archivo CSV y procesar todas las parcelas
# ============================================================================

def main():
    """
    Función principal que lee parcelas.csv y genera el reporte.
    """
    import csv  # Importa módulo para leer archivos CSV

    reportes = []  # Lista vacía para guardar resultados de cada parcela

    # Abre el archivo en modo lectura, se cierra automáticamente al terminar
    with open("parcelas.csv", "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)  # Lee CSV y convierte cada fila en diccionario

        # Recorre cada fila del CSV (cada parcela)
        for fila in reader:
            # Llama a procesar_parcela con los datos de la fila actual
            resultado = procesar_parcela(
                parcela_id=fila['parcela_id'],  # Obtiene el ID (ya es string)
                zona=fila['zona'],  # Obtiene la zona
                cultivo=fila['cultivo'],  # Obtiene el cultivo
                temperatura=float(fila['temperatura_c']),  # Convierte texto a número decimal
                humedad=int(fila['humedad_suelo_pct']),  # Convierte texto a número entero
                ph=float(fila['ph'])  # Convierte pH a decimal
            )
            reportes.append(resultado)  # Agrega el diccionario resultado a la lista

    # Calcula estadísticas después de procesar todas las parcelas
    total = len(reportes)  # Cuenta cuántas parcelas hay
    riego = sum(1 for r in reportes if "RIEGO" in r['riego'])  # Cuenta las que tienen "RIEGO" en recomendación
    drenaje = sum(1 for r in reportes if "DRENAJE" in r['riego'])  # Cuenta las que necesitan drenaje
    alertas = sum(1 for r in reportes if r['alerta_termica'])  # Cuenta las que tienen alerta (True)

    # Imprime el encabezado del reporte
    print("\n" + "="*60)  # Línea decorativa (60 caracteres =)
    print("REPORTE DE ANÁLISIS DE PARCELAS")
    print("="*60)
    print(f"\nTotal: {total} | Riego: {riego} | Drenaje: {drenaje} | Alertas: {alertas}\n")  # f-string inserta variables

    # Recorre cada reporte y lo imprime con formato
    for r in reportes:
        print(f"[{r['parcela_id']}] {r['zona']} - {r['cultivo']}")  # Línea de cabecera de parcela
        print(f"  → Riego: {r['riego']}")  # Muestra recomendación de riego
        print(f"  → pH: {r['ph_accion']}")  # Muestra acción para pH
        print(f"  → Alerta térmica: {'Sí' if r['alerta_termica'] else 'No'}\n")  # Operador ternario: si True muestra "Sí", sino "No"

    print("✓ Análisis completado")  # Mensaje final

# ============================================================================
# EJECUCIÓN DEL PROGRAMA
# ============================================================================

if __name__ == "__main__":
    main()
