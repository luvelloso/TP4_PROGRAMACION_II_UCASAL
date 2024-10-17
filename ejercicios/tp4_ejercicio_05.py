# lucia velloso 
# TP4_Ejercicio_05py

import matplotlib.pyplot as plt

# Datos proporcionados
years = [1900, 1970, 1990, 2000, 2020]
poblacion = [1650, 3692, 5263, 6070, 7800]

# Crear el gráfico de líneas
plt.plot(years, poblacion, marker='o')

# Añadir título y etiquetas a los ejes
plt.title('Crecimiento de la Población Mundial')
plt.xlabel('Años')
plt.ylabel('Población (millones)')

# Mostrar el gráfico
plt.show()

