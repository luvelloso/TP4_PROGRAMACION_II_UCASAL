
# lucia velloso 
# TP4_Ejercicio_07.py

import matplotlib.pyplot as plt
import csv

# Supongamos que el archivo poblacion.csv contiene las columnas 'Year' y 'Poblacion'
years = []
poblacion = []

# Leer el archivo poblacion.csv
with open('poblacion.csv', mode='r', newline='') as archivo:
    lector_csv = csv.DictReader(archivo)
    for fila in lector_csv:
        years.append(int(fila['Year']))
        poblacion.append(int(fila['Poblacion']))

# Crear la figura y los gráficos
plt.figure()

# Gráfico de líneas
plt.plot(years, poblacion, color='green', label='Línea')

# Gráfico de dispersión
plt.scatter(years, poblacion, color='red', label='Scatter')

# Añadir título y etiquetas
plt.title('Población Histórica Mundial')
plt.xlabel('Años')
plt.ylabel('Población (millones)')
plt.legend()

# Mostrar los gráficos
plt.show()
