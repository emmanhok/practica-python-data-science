"""
Has recibido una demanda para tratar 2 listas con los nombres y apellidos de cada estudiante
concatenándolos para presentar sus nombres completos en la forma Nombre Apellido.
Las listas son:
    nombres = ["juan", "MaRia", "JOSÉ"]
    apellidos = ["SILVA", "sosa", "Tavares"]
Normalizar nombres y apellidos y crear una nueva lista con los nombres completos
Puedes apoyarte en la función map()
"""

nombres = ["juan", "MaRia", "JOSÉ"]
apellidos = ["SILVA", "sosa", "Tavares"]

nombres_normalizados = map(lambda x: x.capitalize(), nombres)
apellidos_normalizados = map(lambda x: x.capitalize(), apellidos)
nombres_completos = list(map(lambda x, y: f"Nombres completos: {x} {y}", nombres_normalizados, apellidos_normalizados))
print(nombres_completos)
