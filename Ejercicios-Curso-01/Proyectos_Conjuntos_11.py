"""
Un equipo de científicos de datos está estudiando la diversidad biológica en un bosque.
El equipo recopiló información sobre el número de especies de plantas y animales en cada área del bosque y
almacenó estos datos en un diccionario. En él, la clave describe el área de los datos y
los valores en las listas corresponden a las especies de plantas y animales en esas áreas, respectivamente.
{'Área Norte': [2819, 7236], 'Área Leste': [1440, 9492], 'Área Sul': [5969, 7496], 'Área Oeste': [14446, 49688], 'Área Centro': [22558, 45148]}
Escribe un código para calcular el promedio de especies por área e identificar el área con la mayor diversidad biológica.
"""
#MISOLUCION
# Creación del diccionario de las areas con listas donde se almacenan plantas y animales respectivamente
areas = {'Área Norte': [2819, 7236],
         'Área Leste': [1440, 9492],
         'Área Sul': [5969, 7496],
         'Área Oeste': [14446, 49688],
         'Área Centro': [22558, 45148]}
# Creación de 2 variables: una para calcular el area de mayor biodiversidad y otra para asignar el área con mayor biodiversidad
area_de_mayor_diversidad = -1
nombre_area_de_mayor_diveresidad = ''
# En un ciclo for que accede con .items() a las llaves y sus valores
# Se obtiene la suma de las especies de cada llave y se calcula su promedio
for area, especies in areas.items():
    suma_especies = sum(especies)
    promedio = suma_especies / len(especies)
    print(f'Promedio del {area} es: {promedio}')  # Se imprime promedio de cada área
# Condicional para calcular y asignar el area de mayor biodiversidad
    if suma_especies > area_de_mayor_diversidad:
        area_de_mayor_diversidad = suma_especies
        nombre_area_de_mayor_diveresidad = area
# Por último, se imprime el area con mayor diversidad y la cantidad total de especies que tiene
print(f'El área de mayor diversidad es: {nombre_area_de_mayor_diveresidad} con {area_de_mayor_diversidad}')
