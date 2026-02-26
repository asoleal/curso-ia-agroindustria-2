import numpy as np

def generar_datos():
    # Simulamos una finca de 100x100 parcelas durante 180 días (un ciclo)
    # Dimensiones: (Tiempo, Latitud, Longitud)
    shape = (180, 100, 100)
    print(f"Generando matriz de sensores de {shape}...")
    
    # Generamos valores de humedad aleatorios entre 10% y 90%
    # Usamos float32 para optimizar memoria
    datos = np.random.uniform(10, 90, size=shape).astype(np.float32)
    
    # Guardamos en formato binario nativo de NumPy
    np.save('humedad_finca_grande.npy', datos)
    print("✓ Archivo 'humedad_finca_grande.npy' creado (aprox. 7MB).")

if __name__ == "__main__":
    generar_datos()
