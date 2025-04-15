"""
El departamento de Recursos Humanos de tu empresa te pidió ayuda para analizar las edades de los colaboradores
de 4 sectores de la empresa.
Para ello, te proporcionaron los siguientes datos:
{'Setor A': [22, 26, 30, 30, 35, 38, 40, 56, 57, 65],
 'Setor B': [22, 24, 26, 33, 41, 49, 50, 54, 60, 64],
 'Setor C': [23, 26, 26, 29, 34, 35, 36, 41, 52, 56],
 'Setor D': [19, 20, 25, 27, 34, 39, 42, 44, 50, 65]}
Dado que cada sector tiene 10 colaboradores,
construye un código que calcule la media de edad de cada sector,
la edad media general entre todos los sectores y
cuántas personas están por encima de la edad media general.
"""
# Creación de variables para calcular medias y el contador de personas con edad mayor a la media general
suma_total_edades = 0
total_personas = 0
personas_encima_del_promedio_general = 0
# Creación del diccionario con Sector como llave y listas como valores
sectores_edades = {'Setor A': [22, 26, 30, 30, 35, 38, 40, 56, 57, 65],
                   'Setor B': [22, 24, 26, 33, 41, 49, 50, 54, 60, 64],
                   'Setor C': [23, 26, 26, 29, 34, 35, 36, 41, 52, 56],
                   'Setor D': [19, 20, 25, 27, 34, 39, 42, 44, 50, 65]}
# Primer ciclo for para obtener media de cada sector e imprimirla
for sector, edades in sectores_edades.items():
    suma_total_sector = sum(edades)  # Suma de edades de cada sector
    edad_media_de_cada_sector = suma_total_sector / len(edades)  # Media de cada sector dividiendo por la cantidad de elementos de cada lista (10)
    # Impresion del sector y su media con dos decimales (:.2f)
    print(f'Promedio del {sector} = {edad_media_de_cada_sector:.2f}')
    suma_total_edades += suma_total_sector  # Calculo de la suma total de todas las edades de todas las listas usa de dividendo en la media general
    total_personas += len(edades)  # Contador del total de personas para usar de divisor en la media general
edad_media_general = suma_total_edades / total_personas  # Cálculo de la media general
print(f'La edad media general es: {edad_media_general:.2f}')  # Impresión de la media general
# Segundo ciclo for para obtener las edades que sean mayores a la media general
for sector, edades in sectores_edades.items():  # Se accede a keys y values con .items()
    for edad in edades:  # Se itera cada lista para ir comparandolo con la media general
        if edad > edad_media_general:  # Condicional: si edad es mayor se suma 1 al contador de personas con mayor edad que la media general
            personas_encima_del_promedio_general += 1
# Impresion de la cantidad de personas con edad mayor a la media general
print(f'El total de personas con edad mayor al promedio general son: {personas_encima_del_promedio_general}')
