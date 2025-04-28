"""
Se debe escribir un programa para sortear a un seguidor de una red social para ganar un premio.
La lista de participantes está numerada y debemos elegir aleatoriamente un número según la cantidad de participantes.
Pide a la persona usuaria que proporcione el número de participantes del sorteo y devuelve el número sorteado.
"""
# Importación de choice
from random import choice

# Creación de una lista vacía para luego rellenar
lista_participantes = []
# Se pide al usuario la cantidad de participantes
cantidad_participantes = int(input('Ingrese el número de participantes del sorteo: '))
# Ciclo for en el rango de 1 hasta el número ingresado por el usuario para llenar la lista de participantes
for participante in range(1, cantidad_participantes + 1):
    lista_participantes.append(participante)  # Se agrega el número de los participantes a la lista
# Se utiliza la funcion choice para seleccionar un participante de la lista
seguidor_sorteado = choice(lista_participantes)
# Se imprime el número de participante elegido por choice()
print(f'El seguidor elegido es el número: {seguidor_sorteado}')
