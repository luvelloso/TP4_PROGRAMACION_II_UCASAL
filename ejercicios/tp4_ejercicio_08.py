# Lucia Velloso
# TP4_Ejercicio_08.py

import pandas as pd
import matplotlib.pyplot as plt

# Leer el archivo población.csv
archivo_csv = 'poblacion.csv'
años_interesados = [2000, 2005, 2010, 2015, 2020]

# Cargar el archivo CSV en un DataFrame
data = pd.read_csv(archivo_csv)

# Filtrar solo los años de interés
datos_filtrados = data[data['year'].isin(años_interesados)]

# Crear el gráfico de barras
plt.bar(datos_filtrados['year'], datos_filtrados['poblacion'])

# Añadir título y etiquetas
plt.title("Población Histórica Mundial")
plt.xlabel("Año")
plt.ylabel("Población en millones")

# Mostrar el gráfico
plt.show()
