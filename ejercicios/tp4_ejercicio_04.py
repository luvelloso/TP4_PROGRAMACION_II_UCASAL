# lucia veloso 
# TP4_Ejercicio_04py

import csv

contador_2_ambientes = 0
contador_3_ambientes = 0

# Abrimos el archivo propiedades.csv en modo lectura
with open('propiedades.csv', mode='r', newline='') as archivo:
    lector_csv = csv.DictReader(archivo)
    
    # Recorremos cada fila del archivo
    for fila in lector_csv:
        # Verificamos si la columna "ambientes" no está vacía
        ambiente = fila['ambientes']
        if ambiente:
            try:
                ambiente = int(ambiente)
                
                # Contamos departamentos de 2 y 3 ambientes
                if ambiente == 2:
                    contador_2_ambientes += 1
                elif ambiente == 3:
                    contador_3_ambientes += 1
            except ValueError:
                # Si ocurre un error de conversión, lo ignoramos y seguimos
                pass

# Mostramos los resultados
print(f"Cantidad de departamentos de 2 ambientes: {contador_2_ambientes}")
print(f"Cantidad de departamentos de 3 ambientes: {contador_3_ambientes}")
