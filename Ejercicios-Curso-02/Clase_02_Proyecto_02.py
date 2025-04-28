"""
Para cumplir con una demanda de una institución educativa para el análisis del rendimiento de sus estudiantes,
necesitas crear una función que reciba una lista de 4 notas y devuelva:
    mayor nota
    menor nota
    media
    situación (Aprobado(a) o Reprobado(a))
Uso de la función
    Mostrar:
        El estudiante obtuvo una media de `media`, con la mayor nota de `mayor` puntos y la menor nota de
        `menor` puntos y fue `situacion`.)
"""
def rendimiento_estudiante(lista: list) -> str:
    sorted(lista)
    mayor_nota = lista[-1]
    menor_nota = lista[0]
    media_notas = round(sum(lista) / len(lista), 2)
    if media_notas > 6:
        situacion = 'Aprobado'
    else:
        situacion = 'Reprobado'
    return (f'El estudiante obtuvo una media de {media_notas}, con la mayor nota de {mayor_nota} puntos y '
            f'la menor nota de {menor_nota} puntos y fue {situacion}')
notas_rendimiento = []
for i in range(1, 5):
    nota = float(input(f'Ingrese la nota {i}: '))
    notas_rendimiento.append(nota)
situacion_estudiante = rendimiento_estudiante(notas_rendimiento)
print(situacion_estudiante)