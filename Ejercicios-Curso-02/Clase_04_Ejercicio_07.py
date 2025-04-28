"""
Una clínica analiza datos de pacientes y almacena el valor numérico de la glucosa en una base de datos y
le gustaría etiquetar los datos de la siguiente manera:
•	Glucosa igual o inferior a 70: 'Hipoglicemia'
•	Glucosa entre 70 y 99: 'Normal'
•	Glucosa entre 100 y 125: 'Alterada'
•	Glucosa superior a 125: 'Diabetes'
La clínica proporcionó parte de los valores y tu tarea es crear una lista de tuplas
usando la comprensión de listas que contenga la etiqueta y el valor de la glucemia en cada tupla.
glicemia = [129, 82, 60, 97, 101, 65, 62, 167, 87, 53, 58, 92, 66, 120, 109, 62, 86, 96, 103, 88, 155, 52, 89, 73]
"""
glicemia = [129, 82, 60, 97, 101, 65, 62, 167, 87, 53, 58, 92, 66, 120, 109, 62, 86, 96, 103, 88, 155, 52, 89, 73]
categorias = ['Hipoglicemia', 'Normal', 'Alterada', 'Diabetes']
lista_hipoglicemia = [(categorias[0], valor) for valor in glicemia if valor <= 70]
lista_normal = [(categorias[1], valor) for valor in glicemia if 69 < valor < 100]
lista_alterada = [(categorias[2], valor) for valor in glicemia if 99 < valor < 126]
lista_diabetes = [(categorias[3], valor) for valor in glicemia if valor > 125]
lista_completa = lista_hipoglicemia + lista_normal + lista_alterada + lista_diabetes
print(lista_completa)


"""
Mejora propuesta por GitHub Copilot:
La cuestión de esta solución es que lo da en orden a la lista glicemia
En cambio mi forma de hacerlo lo hace en forma ordenada dando en orden según cada categoria

glicemia = [129, 82, 60, 97, 101, 65, 62, 167, 87, 53, 58, 92, 66, 120, 109, 62, 86, 96, 103, 88, 155, 52, 89, 73]

lista_completa = [
    ('Hipoglicemia', valor) if valor <= 70 else
    ('Normal', valor) if 70 < valor < 100 else
    ('Alterada', valor) if 100 <= valor < 126 else
    ('Diabetes', valor)
    for valor in glicemia
]

print(lista_completa)
"""
