"""
Solución Oficial - Taller Semana 03
Ingeniería de IA para el Agro
"""
import numpy as np

def limpiar_datos(datos):
    """
    Tarea 1: Uso de np.clip para sanear sensores.
    Mantiene los valores entre 0 y 100.
    """
    return np.clip(datos, 0, 100)

def calcular_estres_hidrico(datos, umbral=25):
    """
    Tarea 2: Máscara booleana.
    Retorna True donde hay sequía (humedad < umbral).
    """
    return datos < umbral

def simular_riego_variable(datos, umbral_critico=25):
    """
    Tarea 3: np.where para lógica condicional vectorizada.
    Si humedad < 25, suma 30, pero sin pasarse de 100.
    """
    # Aplicamos el riego condicional
    datos_regados = np.where(datos < umbral_critico, datos + 30, datos)
    # Aseguramos que no exceda el 100% (limpieza final)
    return np.clip(datos_regados, 0, 100)

def main():
    # Carga de datos generados por data_generator.py
    try:
        data = np.load('humedad_finca_grande.npy')
        print(f"Dataset cargado correctamente: {data.shape}")
        
        # Ejecución del pipeline de solución
        data_limpia = limpiar_datos(data)
        estres = calcular_estres_hidrico(data_limpia)
        data_final = simular_riego_variable(data_limpia)
        
        print("-" * 30)
        print(f"Promedio humedad inicial: {np.mean(data):.2f}%")
        print(f"Zonas en estrés crítico: {np.sum(estres):,}")
        print(f"Promedio humedad post-riego: {np.mean(data_final):.2f}%")
        print("-" * 30)
        print("✅ Solución ejecutada con éxito.")
        
    except FileNotFoundError:
        print("Error: No se encontró 'humedad_finca_grande.npy'.")

if __name__ == "__main__":
    main()
