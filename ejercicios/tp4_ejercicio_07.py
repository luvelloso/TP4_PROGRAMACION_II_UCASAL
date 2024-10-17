# Lucia Velloso
# TP4_Ejercicio_07.py


# Realizar los gráficos "plot" y "scatter" en la misma figura
import matplotlib.pyplot as plt

# Definir los datos para los ejes x (años) e y (población)
x = data['year']
y = data['poblacion']

# Crear una figura y dos gráficos en la misma
plt.figure(figsize=(10, 6))

# Gráfico de línea (plot)
plt.plot(x, y, color='green', label='Línea de Población')

# Gráfico de dispersión (scatter)
plt.scatter(x, y, color='red', label='Puntos de Población')

# Añadir título y etiquetas
plt.title("Población Histórica Mundial")
plt.xlabel("Año")
plt.ylabel("Población en millones")

# Añadir leyenda
plt.legend()

# Mostrar el gráfico
plt.show()
