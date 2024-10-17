# Lucia Velloso
# TP4_Ejercicio_10.py

import numpy as np
import matplotlib.pyplot as plt

# Crear los valores de x
x = np.linspace(-4, 4, 400)  # Genera 400 puntos entre -4 y 4

# Definir las dos funciones
y1 = x ** 2  # Función cuadrática
y2 = x ** 3  # Función cúbica

# Crear el gráfico
plt.figure(figsize=(8, 6))

# Graficar la primera función (cuadrática)
plt.plot(x, y1, label="**2", color='blue')

# Graficar la segunda función (cúbica)
plt.plot(x, y2, label="**3", color='orange')

# Añadir título y etiquetas
plt.title("Ejercicio_10")
plt.xlabel("x")
plt.ylabel("y")

# Añadir leyenda
plt.legend()

# Mostrar la cuadrícula
plt.grid(True)

# Mostrar el gráfico
plt.show()
