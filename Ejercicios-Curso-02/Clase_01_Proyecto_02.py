"""
Has recibido una solicitud para generar números de token para acceder a la aplicación de una empresa.
El token debe ser par y variar de 1000 a 9998.
Escribe un código que solicite el nombre de la persona usuaria y
muestre un mensaje junto a este token generado aleatoriamente:
    print(f"Hola, {nombre_usuario}, tu token de acceso es {token_generado} ¡Bienvenido/a!")
"""
from random import choice
# Creación de lista vacía
lista_tokens = []
# Ciclo for para llenar la lista entre el 1000 y 9998
for token in range(1000, 9999):
    if token % 2 == 0: # Condicional para que solo se eliga un número PAR
        lista_tokens.append(token)
# Se pide al usuario su nombre
nombre_usuario = input('Ingrese su nombre: ')
# Se elige al azar un número de la lista
token_generado = choice(lista_tokens)
# Impresión del mensaje de bienvenida
print(f"Hola, {nombre_usuario}, tu token de acceso es {token_generado} ¡Bienvenido/a!")
