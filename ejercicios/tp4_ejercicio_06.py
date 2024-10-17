# lucia velloso 
# TP4_Ejercicio_06.py

import matplotlib.pyplot as plt

mes = [3, 4, 5, 6]
gasto_carne = [1650, 2600, 3100, 4000]
gasto_verdura = [2500, 2200, 1800, 600]

# Calcular el gasto total como la suma de las dos listas
gasto_total = [gasto_carne[i] + gasto_verdura[i] for i in range(len(mes))]

# Crear el gráfico "multi line plot"
plt.plot(mes, gasto_carne, label='Gasto Carne', marker='o')
plt.plot(mes, gasto_verdura, label='Gasto Verdura', marker='o')
plt.plot(mes, gasto_total, label='Gasto Total', marker='o')

# Añadir título y etiquetas
plt.title('Gastos Mensuales')
plt.xlabel('Mes')
plt.ylabel('Gasto (en pesos)')
plt.legend()

plt.show()
