"""
Crea un programa que genere aleatoriamente un número entero menor que 100.
"""
from random import choice

numero_entero_menor_a_100 = choice(range(0, 101))
print(numero_entero_menor_a_100)
