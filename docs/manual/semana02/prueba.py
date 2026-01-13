import os # Importa comandos del sistema
import numpy as np
import matplotlib.pyplot as plt

os.makedirs("reports", exist_ok=True) # Verifica que exista la carpeta reports

humedad = np.random.rand(50, 50)

plt.imshow(humedad, cmap="viridis", interpolation="nearest")
plt.colorbar()
plt.title("Mapa de humedad (50x50)")

plt.savefig("reports/mapa_humedad.png", dpi=150, bbox_inches="tight")  # Guarda la figura con el nombre mapa_humedad.png
