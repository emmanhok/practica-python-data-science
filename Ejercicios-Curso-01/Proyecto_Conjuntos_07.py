"""
Un instituto de meteorología desea realizar un estudio de la temperatura media de cada mes del año.
Para ello, debes crear un código que recoja y almacene esas temperaturas medias en una lista.
Luego, calcula el promedio anual de las temperaturas y
muestra todas las temperaturas por encima del promedio anual y
en qué mes ocurrieron, mostrando los meses por su nombre (Enero, Febrero, etc.).
"""
# Creo listas de meses y tempraturas según cada mes
meses = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre']
temperatura_media_por_mes = [33.2, 29.5, 28.0, 21.5, 15.7, 9.3, 7.0, 14.2, 19.9, 22.0, 25.0, 30.5]
# Creo listas vacías donde se cargaran tanto la temperatura como el mes que sea superior al promedio anual
temperaturas_por_encima_del_promedio_anual = []
mes_superior_al_promedio_anual = []

# Se calcula el total para despues dividirlo en 12 y obtener el promedio anual
total_temperaturas_anual = sum(temperatura_media_por_mes)
print(f'La temperatura total sumando todos los meses es: {total_temperaturas_anual:.2f}°C')
promedio_anual = total_temperaturas_anual / 12
print(f'El promedio anual de temperaturas es: {promedio_anual:.2f}°C')

# En un ciclo for si coloca un conidional si la temperatura del mes es superior al promedio anual
# Se agrega la temperatura y el mes de sus respectivas listas a las listas vacias
# Luego se van imprimiendo uno a uno el mes con su respectiva temperatura superior al promedio anual
print('Los meses que superaron el promedio anual de temperatura son: ')
for i in range(len(temperatura_media_por_mes)):
    if temperatura_media_por_mes[i] > promedio_anual:
        temperaturas_por_encima_del_promedio_anual.append(temperatura_media_por_mes[i])
        mes_superior_al_promedio_anual.append(meses[i])
        print(f"{meses[i]}: {temperatura_media_por_mes[i]:.2f}°C")
