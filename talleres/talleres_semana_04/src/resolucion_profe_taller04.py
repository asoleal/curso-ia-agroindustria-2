import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler

print("="*50)
print(" PARTE 2: TRANSICIÓN COMPUTACIONAL (DATOS LIMPIOS)")
print("="*50)

# 1. Cargar datos limpios (asumiendo que ejecutamos desde la carpeta src/)
# Nota: Si ejecutas desde la raíz del taller, cambia la ruta a 'data/01_...'
ruta_limpia = '../data/01_micro_experimento_limpio.csv'
df_limpio = pd.read_csv(ruta_limpia)

# 2. Separar X e y
X_limpio = df_limpio[['Nitrogeno_kg_ha', 'Potasio_kg_ha']]
y_limpio = df_limpio['Rendimiento_ton_ha']

# 3. Entrenar modelo
modelo_limpio = LinearRegression()
modelo_limpio.fit(X_limpio, y_limpio)
y_pred_limpio = modelo_limpio.predict(X_limpio)

# 4. Mostrar resultados
print(f"Intercepto (Base): {modelo_limpio.intercept_:.2f}")
print(f"Coeficiente Nitrógeno: {modelo_limpio.coef_[0]:.4f}")
print(f"Coeficiente Potasio: {modelo_limpio.coef_[1]:.4f}\n")

print("--- Métricas de Error ---")
print(f"MAE:  {mean_absolute_error(y_limpio, y_pred_limpio):.2f} ton/ha")
print(f"RMSE: {np.sqrt(mean_squared_error(y_limpio, y_pred_limpio)):.2f} ton/ha")
print(f"R^2:  {r2_score(y_limpio, y_pred_limpio):.4f}")
print("Conclusión: Un R^2 tan alto indica que el modelo es muy confiable.\n")


print("="*50)
print(" PARTE 3: EL ESCENARIO REAL (PIPELINES Y DATOS SUCIOS)")
print("="*50)

# 1. Cargar datos sucios
ruta_sucia = '../data/02_hacienda_historico_sucio.csv'
df_sucio = pd.read_csv(ruta_sucia)

# 2. Exploración rápida de nulos
print("--- Conteo de Datos Faltantes (NaN) ---")
print(df_sucio.isnull().sum(), "\n")

# 3. Separar X e y (Ignoramos el Lote_ID porque no es predictivo)
X_sucio = df_sucio[['Nitrogeno_kg_ha', 'Riego_mm', 'Radiacion_Solar_horas']]
y_sucio = df_sucio['Rendimiento_ton_ha']

# 4. Construir el Pipeline
# Paso A: Rellenar nulos con la mediana
# Paso B: Escalar variables (para que la radiación en miles no aplaste a las otras)
# Paso C: Regresión Lineal Múltiple
pipeline_agro = Pipeline([
    ('imputador', SimpleImputer(strategy='median')),
    ('escalador', StandardScaler()),
    ('modelo', LinearRegression())
])

# 5. Entrenar TODO el flujo con un solo comando
pipeline_agro.fit(X_sucio, y_sucio)
print("¡Pipeline entrenado exitosamente con datos crudos!\n")

# 6. Predicción para la "nueva parcela"
# Formato: 120 kg/ha Nitrógeno, 30 mm Riego, 1800 horas radiación
nueva_parcela = pd.DataFrame({
    'Nitrogeno_kg_ha': [120],
    'Riego_mm': [30],
    'Radiacion_Solar_horas': [1800]
})

# El pipeline se encarga de escalar automáticamente esta nueva parcela
prediccion_nueva = pipeline_agro.predict(nueva_parcela)
print(f"--- Predicción Final ---")
print(f"Rendimiento estimado para la nueva parcela: {prediccion_nueva[0]:.2f} ton/ha")
print("="*50)
