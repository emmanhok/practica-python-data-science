"""
Un comercio electrónico tiene información de id de venta, cantidad vendida y precio del producto
divididos en las siguientes listas:
    id = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    cantidad = [15, 12, 1, 15, 2, 11, 2, 12, 2, 4]
    precio = [93.0, 102.0, 18.0, 41.0, 122.0, 14.0, 71.0, 48.0, 14.0, 144.0]
La plataforma necesita estructurar estos datos en una tabla que contenga el valor total de la venta,
que se obtiene multiplicando la cantidad por el precio unitario.
Además, la tabla debe contener un encabezado indicando las columnas:
'id', 'cantidad', 'precio' y 'total'.
Crea una lista de tuplas en la que cada tupla tenga
    id, cantidad, precio y valor total, siendo la primera tupla el encabezado de la tabla.
"""
id_producto = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
cantidad = [15, 12, 1, 15, 2, 11, 2, 12, 2, 4]
precio = [93.0, 102.0, 18.0, 41.0, 122.0, 14.0, 71.0, 48.0, 14.0, 144.0]
encabezados = ('id', 'cantidad', 'precio', 'valor total')

listado_completo = [encabezados] + [(x1, x2, x3, x2 * x3) for x1, x2, x3 in zip(id_producto, cantidad, precio)]
print(listado_completo)
