"""
Se realizó una encuesta de mercado para decidir cuál diseño de marca infantil es más atractivo para los niños.
Los votos de la encuesta se pueden ver a continuación:
    Tabla de votos de la marca
        Diseño 1 - 1334 votos
        Diseño 2 - 982 votos
        Diseño 3 - 1751 votos
        Diseño 4 - 210 votos
        Diseño 5 - 1811 votos
Adapta los datos proporcionados a una estructura de diccionario.
A partir de ello, informa el diseño ganador y el porcentaje de votos recibidos.
"""

# MI SOLUCIÓN

# Creación del diccionario con los diseños y su cantidad de votos
tabla_de_votos = {'Diseño 1': 1334, 'Diseño 2': 982, 'Diseño 3': 1751, 'Diseño 4': 210, 'Diseño 5': 1811}
# Creación de dos variables que servirán para obtener el diseño más votado
disenio_ganador = None
votos_disenio_ganador = -1
# Con un ciclo for y condicional if se va obteniendo el diseño con mayor boto
for disenio, voto in tabla_de_votos.items():
    if voto > votos_disenio_ganador:
        disenio_ganador = disenio
        votos_disenio_ganador = voto
# Cálculo del porcentaje de votos del diseño ganador
porcentaje_de_votos_disenio_ganador = votos_disenio_ganador / sum(tabla_de_votos.values()) * 100
# Impresión del diseño ganador, sus votos y el porcentaje obtenido
print(f'El diseño ganador es: {disenio_ganador} con {votos_disenio_ganador} votos')
print(f'Equivalente a un {porcentaje_de_votos_disenio_ganador:.2f}% del total de votos')

# SOLUCIÓN DE ALURA
# Diccionario de votos por diseño
votos = {'Diseño 1': 1334, 'Diseño 2': 982, 'Diseño 3': 1751, 'Diseño 4': 210, 'Diseño 5': 1811}

# Inicializamos las variables
total_votos = 0  # Sumará todos los votos
ganador = ''  # Almacenará el nombre del diseño ganador
voto_ganador = 0  # Almacenará la cantidad ganadora de votos

# Recorremos las claves y elementos del diccionario
for diseño, voto_diseño in votos.items():
    # Sumamos el total de votos
    total_votos += voto_diseño
    # Verificamos si el voto del diseño actual (voto_diseño) es mayor que el valor almacenado en voto_ganador
    # Cada vez que voto_diseño supere el valor en voto_ganador,
    # la variable voto_ganador será igual a voto_diseño, asignando un nuevo valor
    # De manera similar, el ganador también se actualiza con el diseño actual
    if voto_diseño > voto_ganador:
        voto_ganador = voto_diseño
        ganador = diseño
# Calculamos el porcentaje del diseño ganador
porcentaje = 100 * (voto_ganador) / (total_votos)

# Resultado
print(f'{ganador} es el ganador: ')
print(f'Porcentaje de votos: {porcentaje}%')
