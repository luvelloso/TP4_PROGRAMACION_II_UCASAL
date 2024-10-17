# Lucia Velloso
# TP4_Ejercicio_13.py

import numpy as np

# Dado el array
arr = np.array([1, 2, 4, 7])

# a) Máscara para quedarnos con números mayores a 1
mascara_mayores1 = arr > 1
arr_mayores1 = arr[mascara_mayores1]

# b) Máscara para quedarnos con números pares
mascara_pares = arr % 2 == 0
arr_pares = arr[mascara_pares]

# Mostrar los resultados
print("Array original:", arr)
print("Números mayores a 1:", arr_mayores1)
print("Números pares:", arr_pares)
