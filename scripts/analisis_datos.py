import pandas as pd
import matplotlib.pyplot as plt

# Cargar el dataset desde la carpeta /datos
df = pd.read_csv("datos/dataset.csv")

# Calcular indicadores estadísticos básicos
print("=== Resumen estadístico ===")
print(df.describe())

# Graficar evolución de ventas
plt.figure(figsize=(10, 5))
plt.plot(df["sales_date"], df["sales_amount"])
plt.title("Evolución de Ventas")
plt.xlabel("Fecha")
plt.ylabel("Monto")
plt.tight_layout()
plt.savefig("resultados/grafico_ventas.png")
print("Gráfico guardado en /resultados")
