"""
Has comenzado una pasantía en una empresa que trabaja con procesamiento de lenguaje natural (NLP).
Tu líder te solicitó que crees un fragmento de código que reciba una frase escrita por el usuario y
filtre solo las palabras con un tamaño mayor o igual a 5, mostrándolas en una lista.
Esta demanda se centra en el análisis del patrón de comportamiento de las personas al
escribir palabras de esta cantidad de caracteres o más.
Consejo: utiliza las funciones lambda y filter() para filtrar estas palabras.
Recordando que la función integrada filter() recibe una función (en nuestro caso, una función lambda) y filtra
un iterable según la función. Para tratar la frase, utiliza replace() para cambiar ',' '.', '!' y '?' por espacio.
Utiliza la frase "Aprender Python aquí en Alura es muy bueno" para probar el código.
"""

frase_1 = "Aprender Python aquí en Alura es muy bueno"
frase_limpia = frase_1.replace(',', ' ').replace('.', ' ').replace('!', ' ').replace('?', ' ')
obtener_palabras_largas = lambda frase1: filter(lambda palabra: len(palabra) >= 5, frase1.split())
resultado = list(obtener_palabras_largas(frase_limpia))

print(resultado)
