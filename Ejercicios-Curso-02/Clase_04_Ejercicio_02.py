"""
Crea un código para generar una lista que almacene el tercer elemento de cada tupla contenida
en la siguiente lista de tuplas:
lista_de_tuplas = [('Pedro', 1.74, 81), ('Júlia', 1.65, 67), ('Otávio', 1.81, 83)]
"""
lista_de_tuplas = [('Pedro', 1.74, 81), ('Júlia', 1.65, 67), ('Otávio', 1.81, 83)]
tercer_elemento = [elemento[2] for elemento in lista_de_tuplas]
print(tercer_elemento)
