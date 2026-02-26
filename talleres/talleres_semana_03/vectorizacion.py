"""
Taller Semana 03 - Ingeniería de IA para el Agro
Objetivo: Procesar datos masivos de humedad sin usar bucles 'for'.
"""
import numpy as np

def limpiar_datos(datos):
    """
    Tarea 1: Los sensores a veces fallan y dan valores locos.
    - Valores > 100 deben ser 100.
    - Valores < 0 deben ser 0.
    Pista: Usa np.clip()
    """
    # TODO: Implementar limpieza vectorizada
    return datos

def calcular_estres_hidrico(datos, umbral=20):
    """
    Tarea 2: Identificar zonas críticas.
    Retorna una matriz booleana donde True significa 'Estrés Hídrico'.
    """
    # TODO: Implementar máscara booleana
    return None

def simular_riego_variable(datos, umbral_critico=25):
    """
    Tarea 3: Aplicar riego de precisión.
    - Si la humedad < umbral_critico, sumar 30% de humedad.
    - Si no, dejar igual.
    - Asegurar que nada supere el 100%.
    Pista: Usa np.where()
    """
    # TODO: Implementar lógica de riego vectorizada
    return datos

def main():
    try:
        data = np.load('humedad_finca_grande.npy')
    except FileNotFoundError:
        print("Error: No se encuentra 'humedad_finca_grande.npy'. Ejecuta data_generator.py primero.")
        return

    print(f"Dataset cargado. Forma: {data.shape}")
    
    # Aquí el alumno llamará a sus funciones para probarlas
    data_limpia = limpiar_datos(data)
    print("✓ Datos limpios (simulado)")
    
    estres = calcular_estres_hidrico(data_limpia)
    if estres is not None:
        print(f"✓ Zonas en estrés detectadas: {np.sum(estres)}")

if __name__ == "__main__":
    main()
