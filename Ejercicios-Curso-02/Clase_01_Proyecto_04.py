"""
Has recibido un desafío para calcular la raíz cuadrada de una lista de números,
identificando cuáles resultan en un número entero.
La lista es la siguiente:
numeros = [2, 8, 15, 23, 91, 112, 256]
"""
from math import sqrt
# Creación de lista con números para calcular la raíz cuadrada
numeros = [2, 8, 15, 23, 91, 112, 256]
# Ciclo for para obtener raíz cuadrada de cada número de la lista
for numero in numeros:
    raiz_cuadrada = sqrt(numero) # sqrt calcula la raíz cuadrada del numero
    if raiz_cuadrada % 1 == 0: # Aquí se verifica si es un entero no: siendo entero si MOD 1 da 0
        print(f'Raíces cuadradas que resultan en un número entero: raíz cuadrada de {numero} = {raiz_cuadrada}')

