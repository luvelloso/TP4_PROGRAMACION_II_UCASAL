# Lucia Velloso
# TP4_FINAL_INTEGRADOR.py


import csv
import numpy as np
import matplotlib.pyplot as plt

# 1. Leer el archivo CSV
productos = {}
with open('productos.csv', newline='') as archivo:
    lector = csv.reader(archivo)
    next(lector)  # Omitir la cabecera
    for fila in lector:
        nombre = fila[0]
        precio = float(fila[1])
        stock = int(fila[2])
        productos[nombre] = {"precio": precio, "stock": stock}

# 2. Función para mostrar productos y verificar stock
def mostrar_productos():
    print("Productos disponibles:")
    for nombre, datos in productos.items():
        print(f"{nombre.upper()} - Precio: ${datos['precio']} - Stock: {datos['stock']}")

def verificar_stock(producto, cantidad):
    if productos[producto]["stock"] >= cantidad:
        return True
    else:
        print(f"Advertencia: No hay suficiente stock para {producto.upper()}. Stock disponible: {productos[producto]['stock']}")
        return False

# 3. Función principal para procesar la compra
def procesar_compra():
    total = 0
    productos_comprados = []
    cantidades_compradas = []
    
    while True:
        mostrar_productos()
        producto = input("Ingrese el nombre del producto que desea comprar (o 'salir' para finalizar): ").lower()
        
        if producto == 'salir':
            break
        
        if producto in productos:
            cantidad = int(input(f"Ingrese la cantidad de {producto.upper()} que desea comprar: "))
            
            # Verificar stock
            if verificar_stock(producto, cantidad):
                productos_comprados.append(producto)
                cantidades_compradas.append(cantidad)
        else:
            print(f"Producto {producto.upper()} no encontrado.")
    
    return productos_comprados, cantidades_compradas

# 4. Calcular total a pagar y mostrar gráfico
def calcular_total_y_mostrar_grafico(productos_comprados, cantidades_compradas):
    precios = []
    for producto in productos_comprados:
        precios.append(productos[producto]['precio'])

    precios_array = np.array(precios)
    cantidades_array = np.array(cantidades_compradas)
    total_a_pagar = np.sum(precios_array * cantidades_array)

    # Mostrar resultados
    print(f"Total a pagar: ${total_a_pagar:.2f}")
    print(f"Promedio de precio de los productos seleccionados: ${np.mean(precios_array):.2f}")

    # Crear gráfico
    plt.bar(productos_comprados, precios_array)
    plt.title("Precio de los productos seleccionados")
    plt.xlabel("Producto")
    plt.ylabel("Precio")
    plt.show()

# 5. Lógica principal del programa
def main():
    print("Bienvenido a la tienda de productos electrónicos!")
    
    productos_comprados, cantidades_compradas = procesar_compra()
    
    if productos_comprados:
        calcular_total_y_mostrar_grafico(productos_comprados, cantidades_compradas)
    else:
        print("No se compraron productos.")

if __name__ == "__main__":
    main()
