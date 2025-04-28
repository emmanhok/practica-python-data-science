"""
Para diversificar y atraer nuevos clientes, una lanchonete creó un ítem misterioso en su menú llamado
"ensalada de frutas sorpresa".
En este ítem, se eligen aleatoriamente 3 frutas de una lista de 12 para componer la ensalada de frutas del cliente.
Crea el código que realice esta selección aleatoria según la lista dada.
frutas = ["manzana", "banana", "uva", "pera", "mango", "coco", "sandia", "fresa", "naranja", "maracuya", "kiwi", "cereza"]
"""
from random import choice
# Creación de la lista con las frutas
frutas = ["manzana", "banana", "uva", "pera", "mango", "coco", "sandia", "fresa", "naranja", "maracuya", "kiwi", "cereza"]
# Creación de una lista vacía donde se agregaran las 3 frutas aleatoriamente
frutas_aleatorias = []
# Creación de un contador para el bucle while
contador_frutas = 0
# Bucle while que repetirá el proceso hasta que el contador llegue a 3 (para sumar sólo 3 frutas a la lista vacía)
while contador_frutas < 3:
    contador_frutas += 1
    fruta_seleccionada= choice(frutas) # con choice() se elige una fruta aleatoriamente de la lista frutas[...]
    frutas.remove(fruta_seleccionada) # se remueve la fruta que eligió choice() para que en la próxima vuelta del ciclo no se repita la fruta
    frutas_aleatorias.append(fruta_seleccionada) # se agrega la fruta elegida por choice() a la lista fritas_aleatorias[]
print(f'Su ensalada de frutas contendrá las siguientes frutas: {frutas_aleatorias}')
# random.sample() es una opción de obtener sin repetición un elemento de una lista
# Solución de Alura:
"""
frutas = ["manzana", "banana", "uva", "pera", "mango", "coco", "sandia", "fresa", "naranja", "maracuya", "kiwi", "cereza"]
seleccion_frutas = random.sample(frutas, 3)
print("Ensalada de frutas sorpresa:", seleccion_frutas)
"""
