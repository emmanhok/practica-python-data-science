"""
Crea un programa que lea la siguiente lista de números y elija uno al azar.
lista = [8, 12, 54, 23, 43, 1, 90, 87, 105, 77]
"""
from random import choice
lista = [8, 12, 54, 23, 43, 1, 90, 87, 105, 77]
numero_al_azar = choice(lista)
print(numero_al_azar)
