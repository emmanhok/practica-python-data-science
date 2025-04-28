"""
Como científico de datos en un equipo de fútbol, necesitas implementar nuevas formas de recopilación
de datos sobre el rendimiento de los jugadores y del equipo en su conjunto.
Tu primera acción es crear una forma de calcular la puntuación del equipo en el campeonato nacional
a partir de los datos de goles marcados y recibidos en cada juego.
Escribe una función llamada calcula_puntos() que recibe como parámetros dos listas de números enteros,
representando los goles marcados y recibidos por el equipo en cada partido del campeonato.
La función debe devolver la puntuación del equipo y el rendimiento en porcentaje, teniendo en cuenta
que la victoria vale 3 puntos, el empate 1 punto y la derrota 0 puntos.
Para calcular el rendimiento, debemos hacer la razón entre la puntuación del equipo y
la puntuación máxima que podría recibir.
Para la prueba, utiliza las siguientes listas de goles marcados y recibidos:
goles_marcados = [2, 1, 3, 1, 0]
goles_recibidos = [1, 2, 2, 1, 3]
# Texto probablemente mostrado:
# La puntuación del equipo fue `puntos` y su rendimiento fue `desempeno`%"
"""
goles_marcados = [2, 1, 3, 1, 0]
goles_recibidos = [1, 2, 2, 1, 3]

def calcular_puntuacion(lista1, lista2):
    puntuacion_maxima = 15
    puntuacion_equipo = 0
    for x, y in zip(lista1, lista2):
        if x > y:
            puntuacion_equipo += 3
        elif x == y:
            puntuacion_equipo += 1
        else:
            puntuacion_equipo += 0
    despempenio = round((puntuacion_equipo / puntuacion_maxima) * 100, 2)
    return f'La puntuación del equipo fue {puntuacion_equipo} puntos y su rendimiento fue {despempenio}'

situacion_del_equipo = calcular_puntuacion(goles_marcados, goles_recibidos)
print(situacion_del_equipo)
