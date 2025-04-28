"""
Crea una lista usando la comprensión de listas (list comprehension) que almacene
solo el valor numérico de cada tupla en caso de que el primer elemento sea 'Apartamento',
a partir de la siguiente lista de tuplas:
    alquiler = [('Apartamento', 1700), ('Apartamento', 1400), ('Casa', 2150), ('Apartamento', 1900), ('Casa', 1100)]
"""
alquiler = [('Apartamento', 1700), ('Apartamento', 1400), ('Casa', 2150), ('Apartamento', 1900), ('Casa', 1100)]
list_comprehension = [elemento[1] for elemento in alquiler if elemento[0] == 'Apartamento']
print(list_comprehension)
