"""
A partir de la lista: lista = ['Pedro', 'Júlia', 'Otávio', 'Eduardo'],
crea un código para generar una lista de tuplas en la que cada tupla tenga
el primer elemento como la posición del nombre en la lista original y
el segundo elemento siendo el propio nombre.
"""
#[expresion for item in lista]
lista = ['Pedro', 'Júlia', 'Otávio', 'Eduardo']
lista_de_tuplas = [(lista.index(nombre), nombre) for nombre in lista]
print(lista_de_tuplas)
