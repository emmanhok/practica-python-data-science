"""
Crea una función que lea la siguiente lista y devuelva una nueva lista con los múltiplos de 3:
[97, 80, 94, 88, 80, 1, 16, 53, 62, 32, 24, 99]
"""
lista_1 = [97, 80, 94, 88, 80, 1, 16, 53, 62, 32, 24, 99]
lista_2 = []
def multiplicar_lista(lista: list):
    for numero in lista:
        if numero % 3 == 0:
            lista_2.append(numero)
    return print(lista_2)
multiplicar_lista(lista_1)
