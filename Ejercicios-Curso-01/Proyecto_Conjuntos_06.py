"""
Desarrolla un programa que informe la puntuación de un estudiante de acuerdo con sus respuestas.
Debe pedir la respuesta del estudiante para cada pregunta y verificar si la respuesta coincide con el resultado.
Cada pregunta vale un punto y hay opciones A, B, C o D.
Resultado del examen:
01 - D
02 - A
03 - C
04 - B
05 - A
06 - D
07 - C
08 - C
09 - A
10 - B
"""
respuestas_correctas = ['D', 'A', 'C', 'B', 'A', 'D', 'C', 'C', 'A', 'B']
respuestas_estudiante = []
puntaje = []
puntaje_total = 0
for i in range(1, 11):
    respuesta = input('Ingrese la respuesta correcta: (Opciones: A, B, C o D): ')
    respuestas_estudiante.append(respuesta.upper())
print(respuestas_estudiante)

contador_preguntas = 1

for respuesta_estudiante, respuesta_correcta in zip(respuestas_estudiante, respuestas_correctas):
    if respuesta_estudiante == respuesta_correcta:
        puntaje.append(f'Respuesta {contador_preguntas} = 1 punto')
        puntaje_total += 1
    else:
        puntaje.append(f'Respuesta {contador_preguntas} = 0 punto')
    contador_preguntas += 1
print(puntaje)
if puntaje_total > 1:
    print(f'El puntaje total obtenido es: {puntaje_total} puntos')
else:
    print(f'El puntaje total obtenido es: {puntaje_total} punto')


