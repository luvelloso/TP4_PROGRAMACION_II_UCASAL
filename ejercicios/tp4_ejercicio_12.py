# Lucia Velloso
# TP4_Ejercicio_12.py

import numpy as np

# Crear un array a partir de la lista l1
l1 = list(range(10))
arr = np.array(l1)

# a) Crear un nuevo array con números mayores a 3 y el resto reemplazado por 0
nuevo_arr_mayores3 = np.where(arr > 3, arr, 0)

# b) Crear un nuevo array con solo números pares y el resto reemplazado por 0
nuevo_arr_pares = np.where(arr % 2 == 0, arr, 0)

# Mostrar los resultados
print("Array original:", arr)
print("Array con números mayores a 3:", nuevo_arr_mayores3)
print("Array con números pares:", nuevo_arr_pares)
