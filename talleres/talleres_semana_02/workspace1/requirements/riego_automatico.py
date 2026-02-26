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
    # TODO: Completa esta función según las reglas de negocio
    # Pista 1: Usa if/elif/else para verificar los rangos
    # Pista 2: Ejemplo de estructura:
    #   if humedad < 40:
    #       return "RIEGO URGENTE"
    #   elif humedad > 75:
    #       return "DRENAJE"
    #   else:
    #       return "ÓPTIMO"

    pass  # Elimina esta línea y escribe tu código aquí


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
    # Pista: pH < 5.5 necesita cal, pH > 7.5 necesita azufre, el resto es óptimo
    # Estructura similar a evaluar_riego pero con diferentes condiciones

    pass


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
    # - 'parcela_id': debe contener el parámetro parcela_id
    # - 'zona': debe contener el parámetro zona
    # - 'cultivo': debe contener el parámetro cultivo
    # - 'riego': llama a evaluar_riego(humedad) y guarda el resultado
    # - 'ph_accion': llama a evaluar_ph(ph) y guarda el resultado
    # - 'alerta_termica': True si temperatura > 30, False si no

    # Pista: La estructura del diccionario es:
    # resultado = {
    #     'parcela_id': parcela_id,
    #     'zona': zona,
    #     'cultivo': cultivo,
    #     'riego': evaluar_riego(humedad),
    #     'ph_accion': evaluar_ph(ph),
    #     'alerta_termica': temperatura > 30
    # }
    # return resultado

    pass


# ============================================================================
# TAREA 4: Leer el archivo CSV y procesar todas las parcelas
# ============================================================================

def main():
    """
    Función principal que lee parcelas.csv y genera el reporte.
    """
    import csv

    # PASO 1: Crear lista para guardar resultados
    # TODO: Crea una lista vacía llamada 'reportes'
    # Pista: reportes = []


    # PASO 2: Abrir y leer el archivo CSV
    # TODO: Usa with open() para abrir parcelas.csv
    # Pista: with open("parcelas.csv", "r", encoding="utf-8") as f:
    #            reader = csv.DictReader(f)
    #            # aquí va el bucle for (debe estar DENTRO del with)


        # PASO 3: Recorrer cada fila del CSV
        # TODO: Usa un bucle for para recorrer el reader
        # Pista: for fila in reader:


            # PASO 4: Procesar cada parcela
            # TODO: Llama a procesar_parcela() con los datos de la fila
            # Pista: resultado = procesar_parcela(
            #            parcela_id=fila['parcela_id'],
            #            zona=fila['zona'],
            #            cultivo=fila['cultivo'],
            #            temperatura=float(fila['temperatura_c']),  # Convierte texto a número
            #            humedad=int(fila['humedad_suelo_pct']),
            #            ph=float(fila['ph'])
            #        )


            # PASO 5: Guardar resultado
            # TODO: Agrega el resultado a la lista reportes
            # Pista: reportes.append(resultado)


    # PASO 6: Calcular estadísticas (después del with, fuera de la indentación)
    # TODO: Calcula el total de parcelas
    # Pista: total = len(reportes)

    # TODO: Cuenta cuántas parcelas necesitan riego
    # Pista: riego = sum(1 for r in reportes if "RIEGO" in r['riego'])

    # TODO: Cuenta cuántas necesitan drenaje
    # Pista: drenaje = sum(1 for r in reportes if "DRENAJE" in r['riego'])

    # TODO: Cuenta cuántas tienen alerta térmica
    # Pista: alertas = sum(1 for r in reportes if r['alerta_termica'])


    # PASO 7: Imprimir reporte
    print("\n" + "="*60)
    print("REPORTE DE ANÁLISIS DE PARCELAS")
    print("="*60)

    # TODO: Imprime el resumen con las estadísticas
    # Pista: print(f"\nTotal: {total} | Riego: {riego} | Drenaje: {drenaje} | Alertas: {alertas}\n")


    # TODO: Recorre la lista 'reportes' e imprime cada parcela
    # Pista: for r in reportes:
    #            print(f"[{r['parcela_id']}] {r['zona']} - {r['cultivo']}")
    #            print(f"  → Riego: {r['riego']}")
    #            print(f"  → pH: {r['ph_accion']}")
    #            print(f"  → Alerta térmica: {'Sí' if r['alerta_termica'] else 'No'}\n")


    print("\n✓ Análisis completado")


# ============================================================================
# EJECUCIÓN DEL PROGRAMA
# ============================================================================

if __name__ == "__main__":
    main()
