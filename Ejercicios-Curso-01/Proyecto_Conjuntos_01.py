"""
Escribe un programa que genere la tabla de multiplicar de un número entero del 1 al 10, según la elección del usuario.
"""
tabla = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numero = int(input('Ingrese un número para mostrar su tabla de multiplicar: '))
print(f'Tabla de multiplicar del {numero}:')
for i in tabla:
    resultado = numero * i
    print(f'{numero} X {i} = {resultado}')
