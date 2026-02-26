import numpy as np
import time

def calcular_promedio_for(data):
    """Calcula el promedio usando bucles tradicionales de Python"""
    total = 0
    count = 0
    for i in range(data.shape[0]):
        for j in range(data.shape[1]):
            for k in range(data.shape[2]):
                total += data[i, j, k]
                count += 1
    return total / count

def calcular_promedio_numpy(data):
    """Calcula el promedio usando vectorización de NumPy"""
    return np.mean(data)

def main():
    if not np.os.path.exists('humedad_finca_grande.npy'):
        print("Error: Ejecuta primero data_generator.py")
        return

    data = np.load('humedad_finca_grande.npy')
    print(f"Iniciando Benchmark con {data.size:,} puntos de datos...\n")

    # Tiempo con Bucles
    t0 = time.perf_counter()
    res_for = calcular_promedio_for(data)
    t_for = time.perf_counter() - t0
    print(f"Método Loop For: {t_for:.4f} segundos | Resultado: {res_for:.2f}")

    # Tiempo con NumPy
    t0 = time.perf_counter()
    res_np = calcular_promedio_numpy(data)
    t_np = time.perf_counter() - t0
    print(f"Método NumPy:    {t_np:.4f} segundos | Resultado: {res_np:.2f}")

    print(f"\n🚀 ¡NumPy es {int(t_for/t_np)} veces más rápido!")

if __name__ == "__main__":
    main()
