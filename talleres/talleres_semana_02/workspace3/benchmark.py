import time
import numpy as np


def procesar_con_loop(humedad):
    """
    Procesa matriz con bucles Python (LENTO).
    Calcula: sin(humedad/100) para simular procesamiento.
    """
    resultado = np.empty_like(humedad)
    filas, cols = humedad.shape

    for i in range(filas):
        for j in range(cols):
            resultado[i, j] = np.sin(humedad[i, j] / 100.0)

    return resultado


def procesar_con_numpy(humedad):
    """
    Procesa matriz con NumPy vectorizado (RÁPIDO).
    Misma operación, pero sin bucles explícitos.
    """
    return np.sin(humedad / 100.0)


def main():
    print("=" * 60)
    print("BENCHMARK: Loop Python vs NumPy Vectorizado")
    print("=" * 60)

    # Cargar dataset (365 días × 100 zonas)
    print("\n[1/3] Cargando humedad_finca.npy...")
    humedad = np.load("humedad_finca.npy")
    print(f"  ✓ Shape: {humedad.shape}")
    print(f"  ✓ Tamaño: {humedad.size:,} valores")

    # Benchmark con loop
    print("\n[2/3] Midiendo loop Python...")
    t0 = time.perf_counter()
    resultado_loop = procesar_con_loop(humedad)
    tiempo_loop = time.perf_counter() - t0
    print(f"  ⏱ Tiempo: {tiempo_loop:.4f} s")

    # Benchmark con NumPy
    print("\n[3/3] Midiendo NumPy vectorizado...")
    t0 = time.perf_counter()
    resultado_numpy = procesar_con_numpy(humedad)
    tiempo_numpy = time.perf_counter() - t0
    print(f"  ⏱ Tiempo: {tiempo_numpy:.4f} s")

    # Resultados
    speedup = tiempo_loop / tiempo_numpy
    diferencia_max = np.max(np.abs(resultado_loop - resultado_numpy))

    print("\n" + "=" * 60)
    print("RESULTADOS")
    print("=" * 60)
    print(f"Speedup: {speedup:.2f}x más rápido con NumPy")
    print(f"Diferencia numérica: {diferencia_max:.2e} (debe ser ~0)")
    print("\n✓ Benchmark completado")


if __name__ == "__main__":
    main()
