"""
Escribe una función que genere la tabla de multiplicar de un número entero del 1 al 10, según la elección del usuario.
Como ejemplo, para el número 7, la tabla de multiplicar se debe mostrar en el siguiente formato:
    Tabla del  7:
        7 x 0 = 0
        7 x 1 = 7
        [...]
        7 x 10 = 70
"""
def tabla_multiplicar(numero):
    for i in range(0, 11):
        resultado = numero * i
        print(f'{numero} x {i}= {resultado}')
numero = int(input('Ingrese un número entero del 1 al 10: '))
if 11 > numero > 0:
    tabla_multiplicar(numero)
else:
    print("Error: no ingresó un número entero entre el 1 y el 10")