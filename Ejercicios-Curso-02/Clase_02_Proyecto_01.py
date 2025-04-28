"""
Has sido contratado como científico(a) de datos de una asociación de skate.
Para analizar las notas recibidas por los skaters en algunas competiciones a lo largo del año,
necesitas crear un código que calcule la puntuación de los atletas.
Para ello, tu código debe recibir 5 notas ingresadas por los jueces.
"""
notas = []
def puntuacion(lista):
    puntaje_total = round(sum(lista) / len(lista), 2)
    return f'El puntaje total es: {puntaje_total}'
for i in range(1, 5):
    notas.append(float(input(f'Ingresa la puntuación {i}: ')))
resultado = puntuacion(notas)
print(resultado)
