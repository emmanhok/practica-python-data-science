"""
Para una selección de productos alimenticios, debemos separar el conjunto de IDs proporcionados por números enteros,
sabiendo que los productos con ID par son dulces y los que tienen ID impar son amargos.
Crea un código que recoja 10 IDs.
Luego, calcula y muestra la cantidad de productos dulces y amargos.
"""
# MI SOLUCION
# Creacion de arreglo donde irán las ids
productos_alimenticios = []
# Inicialización de contador de alimentos dulces y amargos
contador_alimentos_dulces = 0
contador_alimentos_amargos = 0
# Creación de bucle for para pedirle 10 ids al usuario que se irán agregando a la lista
for ids in range(1, 11):
    id_producto = int(input('Ingrese el Id del producto: '))
    productos_alimenticios.append(id_producto)
# Con condicionales se verifica si es par o impar para sumar a dulces si es par el id y a amargos si es impar
    if id_producto % 2 == 0:
        contador_alimentos_dulces += 1
    elif id_producto % 2 != 0:
        contador_alimentos_amargos += 1
# Se imprime la lista y la cantidad de alimentos dulces y amargos
print(f'Lista de Ids: {productos_alimenticios}')
print(f'La cantidad de alimentos dulces es: {contador_alimentos_dulces}')
print(f'La cantidad de alimentos amargos es: {contador_alimentos_amargos}')
