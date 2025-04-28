"""
Una empresa tiene sucursales distribuidas en los estados de la región Sudeste de Brasil.
En una de las tablas de registro de las sucursales, hay una columna que contiene la información de
a qué estado pertenece:
estados =['CMX', 'OAX', 'PUE', 'PUE', 'CMX', 'PUE', 'OAX', 'OAX', 'OAX', 'CMX', 'CMX', 'PUE', 'OAX', 'CMX', 'VER', 'PUE', 'VER', 'CMX', 'PUE', 'CMX', 'OAX', 'CMX', 'PUE']
La empresa siempre está abriendo nuevas sucursales, por lo que la tabla está constantemente recibiendo nuevos registros
y al gerente le gustaría tener la información actualizada de la cantidad de sucursales en cada estado.
A partir de la columna con la información de los estados, crea un diccionario utilizando la comprensión de diccionarios
(dict comprehension) con la clave siendo el nombre de un estado y el valor siendo la cantidad de veces que aparece
el estado en la lista.
"""
#from collections import Counter

#Esta Solución es correcta y muy eficiente pero no uso el dict comprehension como se pide asique esa forma la hago más abajo
#from collections import Counter
#estados =['CMX', 'OAX', 'PUE', 'PUE', 'CMX', 'PUE', 'OAX', 'OAX', 'OAX', 'CMX', 'CMX', 'PUE', 'OAX', 'CMX', 'VER', 'PUE', 'VER', 'CMX', 'PUE', 'CMX', 'OAX', 'CMX', 'PUE']
#conteo = Counter(estados)
#diccionario_estados_sucursales = dict(conteo)
#print(diccionario_estados_sucursales)
estados =['CMX', 'OAX', 'PUE', 'PUE', 'CMX', 'PUE', 'OAX', 'OAX', 'OAX', 'CMX', 'CMX', 'PUE', 'OAX', 'CMX', 'VER', 'PUE', 'VER', 'CMX', 'PUE', 'CMX', 'OAX', 'CMX', 'PUE']
estados_sucursales = {estado: estados.count(estado) for estado in set(estados)}

print(estados_sucursales)
"""
En esa misma tabla de registro de sucursales, hay una columna con la información de la cantidad de personas empleadas 
y el gerente quisiera tener un agrupamiento de la suma de esas personas para cada estado. 
Las informaciones contenidas en la tabla son:
    empleados = [('CMX', 16), ('OAX', 8), ('PUE', 9), ('PUE', 6), ('CMX', 10), ('PUE', 4), ('OAX',9),  ('OAX', 7), ('OAX', 12), ('CMX', 7), ('CMX', 11), ('PUE',8), ('OAX',8), ('CMX',9), ('VER', 13), ('PUE', 5),  ('VER', 9), ('CMX', 12), ('PUE', 10), ('CMX', 7), ('OAX', 14), ('CMX', 10), ('PUE', 12)]
"""
empleados = [('CMX', 16), ('OAX', 8), ('PUE', 9), ('PUE', 6), ('CMX', 10), ('PUE', 4), ('OAX',9),  ('OAX', 7), ('OAX', 12), ('CMX', 7), ('CMX', 11), ('PUE',8), ('OAX',8), ('CMX',9), ('VER', 13), ('PUE', 5),  ('VER', 9), ('CMX', 12), ('PUE', 10), ('CMX', 7), ('OAX', 14), ('CMX', 10), ('PUE', 12)]

#empleados_sucursales = {estado: sum(cantidad for empleado, cantidad in empleados if empleado == estado)
#                        for estado in set(estado for estado, estados in empleados)}
#print(empleados_sucursales)

# Almacenando los estados sin repetición de valor
lista_de_estados = list(set([tupla[0] for tupla in empleados])) # Se usa [0] porque se recorren los str que representan los estados
print(f'lista_de_estados: {lista_de_estados}')

# Creando una lista de listas con valores de empleados de cada estado
lista_de_empleados = []
for estado in lista_de_estados:
    # A continuacion se evalua si la tupla[0] de empleados es coincide con 'x' estado se anexa la comprehension de lista con el append
    lista = [tupla[1] for tupla in empleados if tupla[0] == estado] # List comprehension donde se va asignando a un solo estado sus empleados
    lista_de_empleados.append(lista) # Se agregan los elementos de la list comprehension a la lista vacía lista_De_empleados
print(f'lista_de_empleados_segun_cada_estado: {lista_de_empleados}')

# Creando un diccionario con datos agrupados de empleados por estado
# Aquí se unen la lista sin repeticion de los estados con la lista de empleados que agrupa en una lista todos los empleados de x estado
agrupamiento_por_estado = {lista_de_estados[i]: lista_de_empleados[i] for i in range(len(lista_de_estados))}
# La llave es el el string de la lista de estados 'CMX' etc
# El valor es la lista con los valores de empleados que se agrupó en la list comprehension lista_de_empleados
print(f'agrupamiento_por_estado: {agrupamiento_por_estado}')

# Creando un diccionario con la suma de empleados por estado
# Aqui la llave queda igual, solo que se agrega la sumatoria sum de cada lista de empelados de cada estado
suma_por_estado = {lista_de_estados[i]: sum(lista_de_empleados[i]) for i in range(len(lista_de_estados))}
print(f'suma_por_estado: {suma_por_estado}')
