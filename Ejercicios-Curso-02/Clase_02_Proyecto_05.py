"""
Te han desafiado a crear un código que calcule los gastos de un viaje a una de las cuatro ciudades desde Recife,
siendo ellas:
    Salvador, Fortaleza, Natal y Aracaju.
El costo diario del hotel es de 150 reales en todas ellas y
el consumo de gasolina en el viaje en coche es de 14 km/l, siendo que el precio de la gasolina es de 5 reales por litro.
Los gastos con paseos y alimentación a realizar en cada una de ellas por día serían
    [200, 400, 250, 300], respectivamente.
Sabiendo que las distancias entre Recife y cada una de las ciudades son aproximadamente
    [850, 800, 300, 550] km,
crea tres funciones:
    la primera función calcula los gastos de hotel (gasto_hotel),
    la segunda calcula los gastos de gasolina (gasto_gasolina) y
    la tercera los gastos de paseo y alimentación (gasto_paseo).

Para probar, simula un viaje de 3 días a Salvador desde Recife. Considera el viaje de ida y vuelta en coche.
        # Texto probablemente mostrado:
        # Con base en los gastos definidos, un viaje de [dias] días a [ciudad] desde
        # Recife costaría [gastos] reales.
"""

def calcular_gastos_gotel(dias): # Se pasa dias
    coste_hotel = coste_diario_hotel * dias
    return coste_hotel

def calcular_gastos_gasolina(distancia):
    kms_con_litro_gasolina = 14
    precio_por_litro = 5

    gasolina_ida = distancia / kms_con_litro_gasolina
    gasolina_ida_vuelta = gasolina_ida * 2
    gasto_ida_vuelta = gasolina_ida_vuelta * precio_por_litro
    return gasto_ida_vuelta

def calcular_gastos_paseo_alimento(gasto_paseo_por_dia, dias): # Se pasa lista y dias
    gasto_paseo_alimento = gasto_paseo_por_dia * dias
    return gasto_paseo_alimento

coste_diario_hotel = 150.00
distancias = [850, 800, 300, 550]
gastos_paseo_por_dia = [200, 400, 250, 300]

print('Introduzca su ciudad de destino: ')
ciudad_destino = input('1.Salvador\n2.Fortaleza\n3.Natal\n4.Aracaju\n')
dias_de_estadia = int(input('¿Cuántos días de estadía?\n'))

gasto_hotel = calcular_gastos_gotel(dias_de_estadia)

gasto_gasolina = None
gasto_paseo = None
if ciudad_destino == 'Salvador':
    gasto_gasolina = calcular_gastos_gasolina(distancias[0])
    gasto_paseo = calcular_gastos_paseo_alimento(gastos_paseo_por_dia[0], dias_de_estadia)
elif ciudad_destino == 'Fortaleza':
    gasto_gasolina = calcular_gastos_gasolina(distancias[1])
    gasto_paseo = calcular_gastos_paseo_alimento(gastos_paseo_por_dia[1], dias_de_estadia)
elif ciudad_destino == 'Natal':
    gasto_gasolina = calcular_gastos_gasolina(distancias[2])
    gasto_paseo = calcular_gastos_paseo_alimento(gastos_paseo_por_dia[2], dias_de_estadia)
elif ciudad_destino == 'Aracaju':
    gasto_gasolina = calcular_gastos_gasolina(distancias[3])
    gasto_paseo = calcular_gastos_paseo_alimento(gastos_paseo_por_dia[3], dias_de_estadia)
gasto_total = round(gasto_hotel + gasto_gasolina + gasto_paseo, 2)

print(f'Con base en los gastos definidos, un viaje de {dias_de_estadia} días a {ciudad_destino} '
 f'desde Recife costaría {gasto_total} reales')

# SUGERENCIA DE GEMINI:
# MISOLUCION tiene una base arquitectónica más sólida para el crecimiento y la flexibilidad,
# especialmente si se implementa la mejora sugerida utilizando un diccionario para los datos de las ciudades.
