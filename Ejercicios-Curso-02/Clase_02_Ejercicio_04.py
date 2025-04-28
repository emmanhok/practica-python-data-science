"""
Crea una lista de los cuadrados de los números de la siguiente lista [1, 2, 3, 4, 5, 6, 7, 8, 9, 10].
Recuerda utilizar las funciones lambda y map() para calcular el cuadrado de cada elemento de la lista.
"""
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
cuadrados = list(map(lambda x: x * x, lista))
print(cuadrados)
