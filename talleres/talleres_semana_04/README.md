# Taller Semana 04: De la Parcela al Pipeline 🚜💻

Bienvenidos al taller práctico de Regresión Lineal Múltiple y Pipelines de Procesamiento de Datos. En este taller ensuciaremos nuestras manos pasando del cálculo matricial puro a la construcción de flujos de trabajo profesionales en Python, aplicados a la toma de decisiones en la agroindustria.

## 📁 Estructura del Directorio

* **`data/`**: Contiene los conjuntos de datos.
  * `01_micro_experimento_limpio.csv`: Datos de invernadero listos para procesar.
  * `02_hacienda_historico_sucio.csv`: Datos reales de campo con valores nulos y escalas desajustadas.
* **`docs/`**: Enunciado formal del taller (LaTeX y PDF).
* **`src/`**: Carpeta destinada para que guardes tus scripts de solución en Python.

## 🛠️ Prerrequisitos del Entorno

Para ejecutar la Fase 2 y 3 del taller, asegúrate de tener instalado Python 3.8+ y las siguientes librerías de ciencia de datos. Puedes instalarlas ejecutando:

```bash
pip install numpy pandas scikit-learn
```
🎯 Misiones del Taller

Este taller está dividido en tres etapas progresivas:

    Parte 1: El Cimiento Matemático (Manual)
    Demuestra que la IA no es magia. Deberás calcular a mano (o con calculadora) 
    las matrices XTX y XTY para encontrar los coeficientes predictivos de un 
    experimento de 4 macetas.

    Parte 2: Transición Computacional (Python Básico)
    Cargarás el dataset limpio (01_micro_experimento_limpio.csv) 
    usando pandas y aplicarás LinearRegression de scikit-learn 
    para calcular las métricas de error (MAE, RMSE, R2).

    Parte 3: El Escenario Real (Pipelines)
    Te enfrentarás al dataset 02_hacienda_historico_sucio.csv, 
    el cual simula fallos en sensores de campo. 
    Deberás construir un Pipeline que ensamble SimpleImputer, 
    StandardScaler y LinearRegression para automatizar la 
    limpieza de datos y la predicción en un solo flujo.

¡Muchos éxitos en la resolución! Recuerden que el agro del futuro necesita datos limpios y modelos robustos.
