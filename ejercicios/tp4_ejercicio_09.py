# Lucia Velloso
# TP4_Ejercicio_09.py



import numpy as np
import matplotlib.pyplot as plt

# Crear los valores de x
x = np.linspace(0, 100, 500)  # Genera 500 puntos entre 0 y 100

# Crear los valores de y basados en alguna función (ejemplo)
y = 10 * np.sin(x / 10)  # Función sinusoidal ajustada

# Crear el gráfico
plt.figure(figsize=(8, 6))

# Dibujar la curva
plt.plot(x, y, label="Ej_9", color='green')

# Añadir título y etiquetas
plt.title("Valores x e y")
plt.xlabel("x")
plt.ylabel("y")

# Añadir leyenda
plt.legend()

# Mostrar el gráfico
plt.grid(True)
plt.show()
