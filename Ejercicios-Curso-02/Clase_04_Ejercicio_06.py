"""
Una tienda tiene una base de datos con la información de venta de cada representante y de cada año
y necesita filtrar solo los datos del año 2022 con ventas mayores a 6000.
La tienda proporcionó una muestra con solo las columnas de los años y los valores de venta para que puedas
ayudar a realizar la filtración de los datos a través de un código:
ventas = [('2023', 4093), ('2021', 4320), ('2021', 5959), ('2022', 8883), ('2023', 9859), ('2022', 5141), ('2022', 7688), ('2022', 9544), ('2023', 4794), ('2021', 7178), ('2022', 3030), ('2021', 7471), ('2022', 4226), ('2022', 8190), ('2021', 9680), ('2022', 5616)]
Crea una lista usando la comprensión de listas para filtrar los valores de 2022 que sean mayores a 6000.
"""
from os.path import split

ventas = [('2023', 4093), ('2021', 4320), ('2021', 5959), ('2022', 8883), ('2023', 9859), ('2022', 5141),
          ('2022', 7688), ('2022', 9544), ('2023', 4794), ('2021', 7178), ('2022', 3030), ('2021', 7471),
          ('2022', 4226), ('2022', 8190), ('2021', 9680), ('2022', 5616)]
ventas_2022_sup_6000 = [anio_valor[1] for anio_valor in ventas if anio_valor[0] == '2022' and anio_valor[1] > 6000]
print(f'Ventas del año 2022 superiores a $6000: {ventas_2022_sup_6000}')
