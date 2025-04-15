"""
Una empresa de comercio electrónico está interesada en analizar las ventas de sus productos.
Los datos de ventas se han almacenado en un diccionario:
{'Producto A': 300, 'Producto B': 80, 'Producto C': 60, 'Producto D': 200, 'Producto E': 250, 'Producto F': 30}
Escribe un código que calcule el total de ventas y el producto más vendido.
"""
ventas_productos = {'Producto A': 300, 'Producto B': 80, 'Producto C': 60, 'Producto D': 200, 'Producto E': 250, 'Producto F': 30}

total_de_ventas = sum(ventas_productos.values())

# Inicializo dos variables para poder recorrer luego el diccionario y encontrar el que tiene más ventas
producto_mas_vendido = None  # Es None porque aún no se encuentra dicho producto, sino que se buscará en el ciclo for
# Luego, se crea la siguiente variable para que cada producto iterado en su cantidad en el ciclo for
# sea superior a esta variable y después se pueda tener a ese producto como referencia con los demás
cantidad_mas_vendida = -1

# Ciclo for para recorrer la cantidad de ventas (se requiere usar .items()) y se va actualizando con un conidiconal
# Para ir reemplazando la variable producto más vendido en comparación al que tiene mayor cantidad
for producto, cantidad in ventas_productos.items():
    if cantidad > cantidad_mas_vendida:
        cantidad_mas_vendida = cantidad
        producto_mas_vendido = producto

# Se imprime el total de ventas
print(f'El total de ventas realizadas es: {total_de_ventas}')
# Por último, se imprime el producto con la cantidad tomando las variables obtenidas en el ciclo for
print(f"El producto más vendido es: {producto_mas_vendido} con {cantidad_mas_vendida} ventas.")
