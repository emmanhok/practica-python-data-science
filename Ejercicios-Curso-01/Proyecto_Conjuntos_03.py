"""
Vamos a comprender la distribución de edades de los pensionistas de una empresa de seguros.
Escribe un programa que lea las edades de una cantidad no informada de clientes y
muestre la distribución en los intervalos [0-25], [26-50], [51-75] y [76-100].
La entrada de datos se detendrá al ingresar un número negativo.
"""
# Primero creo las listas vacías
lista_0_a_25 = []
lista_26_a_50 = []
lista_51_a_75 = []
lista_76_a_100 = []
# Inicializo en un int positivo para que comience el ciclo while
edad = 1
# Ciclo while para que se ejecute el código mientras edad sea un entero positivo
while edad > 0:
    # Pedido del ingreso de la edad o un entero negativo para finalizar
    edad = int(input('Ingrese la edad del pensionista del seguro (ingrese un número negativo para finalizar programa): '))
    # Condicionales para verificar en qué lista se deben ir agregando las edades ingresadas por el usuario
    if 0 < edad < 26:
        lista_0_a_25.append(edad)
    elif 25 < edad < 51:
        lista_26_a_50.append(edad)
    elif 50 < edad < 76:
        lista_51_a_75.append(edad)
    elif 75 < edad < 101:
        lista_76_a_100.append(edad)
# Ordeno las listas de menor a mayor
lista_0_a_25.sort()
lista_26_a_50.sort()
lista_51_a_75.sort()
lista_76_a_100.sort()
# Impresión de las listas
print(f'Intervalo [0-25]: {lista_0_a_25}')
print(f'Intervalo [26-50]: {lista_26_a_50}')
print(f'Intervalo [51-75]: {lista_51_a_75}')
print(f'Intervalo [75-100]: {lista_76_a_100}')
