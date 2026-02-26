"""
Taller 02.3 - Ejercicios de Vectorización con NumPy
Practica máscaras booleanas y np.where para decisiones espaciales.
"""

import numpy as np


def detectar_sequia(humedad, umbral=30):
    """
    Detecta zonas en sequía usando máscaras booleanas.

    Args:
        humedad (ndarray): Matriz de humedad (365, 100)
        umbral (float): Porcentaje bajo el cual hay sequía

    Returns:
        dict: Estadísticas de sequía

    Instrucciones:
    1. Crea una máscara booleana: humedad < umbral
    2. Cuenta cuántas celdas están en sequía (np.sum de la máscara)
    3. Calcula el porcentaje: (celdas_sequia / total_celdas) * 100
    4. Retorna dict con 'celdas_sequia', 'porcentaje'
    """
    # TODO: Completa esta función
    # Crea la máscara
    mascara = humedad < umbral

    #Contar celdas en sequía
    celdas_sequia = np.sum(mascara)

    #Calcula el porcentaje
    total_celdas = humedad.size
    porcentaje = (celdas_sequia / total_celdas )*100

    #Retornar el diccionario
    return {
        "celdas_sequia": celdas_sequia,
        "porcentaje":porcentaje
        }


def aplicar_riego(humedad, umbral=30, cantidad=20):
    """
    Aplica riego solo donde hay sequía usando np.where.

    Args:
        humedad (ndarray): Matriz de humedad actual
        umbral (float): Umbral de sequía
        cantidad (float): Cantidad de agua a aplicar

    Returns:
        ndarray: Matriz con humedad actualizada

    Instrucciones:
    1. Usa np.where(humedad < umbral, humedad + cantidad, humedad)
    2. Asegúrate de que la humedad no supere 100 (usa np.clip)
    3. Retorna la matriz ajustada
    """
    # TODO: Completa esta función
    humedad_ajustada = np.where(humedad < umbral, humedad + cantidad, humedad)
    return humedad_ajustada


def clasificar_zonas(humedad):
    """
    Clasifica cada celda en 3 categorías: SEQUIA, EXCESO, NORMAL.

    Args:
        humedad (ndarray): Matriz de humedad

    Returns:
        ndarray: Matriz de strings con clasificaciones

    Instrucciones:
    1. Usa np.where anidado:
       - "SEQUIA" si humedad < 30
       - "EXCESO" si humedad > 80
       - "NORMAL" en otro caso
    2. Retorna matriz del mismo shape que humedad pero con strings

    Pista: np.where(cond1, val1, np.where(cond2, val2, val3))
    """
    # TODO: Completa esta función
    humedad_nueva = np.where(humedad < 30, "SEQUIA", np.where(humedad > 80, "EXCESO","NORMAL"))
    return humedad_nueva


def main():
    """
    Función principal para probar las funciones.
    """
    print("=" * 60)
    print("EJERCICIOS DE VECTORIZACIÓN")
    print("=" * 60)

    # Cargar datos
    print("\n[1/4] Cargando datos...")
    humedad = np.load("humedad_finca.npy")
    print(f"  ✓ Shape: {humedad.shape}")

    # Ejercicio 1: Detectar sequía
    print("\n[2/4] Detectando sequía...")
    stats_sequia = detectar_sequia(humedad)
    if stats_sequia:
        print(f"  Celdas en sequía: {stats_sequia['celdas_sequia']}")
        print(f"  Porcentaje: {stats_sequia['porcentaje']:.2f}%")
    else:
        print("  ⚠ Función detectar_sequia() aún no implementada")

    # Ejercicio 2: Aplicar riego
    print("\n[3/4] Aplicando riego...")
    humedad_ajustada = aplicar_riego(humedad)
    if humedad_ajustada is not None:
        print(f"  Humedad promedio antes: {humedad.mean():.2f}%")
        print(f"  Humedad promedio después: {humedad_ajustada.mean():.2f}%")
    else:
        print("  ⚠ Función aplicar_riego() aún no implementada")

    # Ejercicio 3: Clasificar zonas
    print("\n[4/4] Clasificando zonas...")
    clasificacion = clasificar_zonas(humedad)
    if clasificacion is not None:
        unique, counts = np.unique(clasificacion, return_counts=True)
        for zona, count in zip(unique, counts):
            pct = (count / clasificacion.size) * 100
            print(f"  {zona}: {count} celdas ({pct:.2f}%)")
    else:
        print("  ⚠ Función clasificar_zonas() aún no implementada")

    print("\n✓ Ejercicios completados")


if __name__ == "__main__":
    main()
