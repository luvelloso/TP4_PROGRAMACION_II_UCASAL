# lucia velloso #
# TP4_Ejercicio_02.py

# Diccionario inicial con stock en cero
stock = {'tornillos': 0, 'tuercas': 0, 'arandelas': 0}

# Bucle infinito para agregar stock
while True:
    # Consultar al usuario qué producto desea agregar
    producto = input("Ingrese el producto que desea agregar al stock (o 'FIN' para terminar): ").lower()

    # Si el usuario ingresa "FIN", terminamos el bucle
    if producto == "fin":
        break

    # Verificar si el producto está en el diccionario
    if producto in stock:
        # Pedir al usuario la cantidad de stock a agregar
        try:
            cantidad = int(input(f"Ingrese la cantidad de {producto} a agregar: "))
            # Acumular la cantidad en el diccionario
            stock[producto] += cantidad
        except ValueError:
            print("Error: Ingrese una cantidad válida.")
    else:
        print("Error: Producto no reconocido.")

# Imprimir el stock final
print("Stock final:", stock)
