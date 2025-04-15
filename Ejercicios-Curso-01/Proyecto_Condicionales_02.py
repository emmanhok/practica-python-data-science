"""
Escribe un programa que pida a la persona usuaria tres números que representan los lados de un triángulo.
El programa debe informar si los valores pueden utilizarse para formar un triángulo y, en caso afirmativo,
si es equilátero, isósceles o escaleno.
Ten en cuenta algunas sugerencias:
•	Tres lados forman un triángulo cuando la suma de cualesquiera dos lados es mayor que el tercero;
•	Triángulo Equilátero: tres lados iguales;
•	Triángulo Isósceles: dos lados iguales;
•	Triángulo Escaleno: tres lados diferentes.
"""
# Función para verificar el tipo de triángulo
def tipo_de_triangulo(lado1, lado2, lado3):
    if lado1 == lado2 and lado2 == lado3:
        print('Es un tríangulo Equilátero')
    elif lado1 == lado2 or lado2 == lado3 or lado3 == lado1:
        print('Es un tríangulo Isóseles')
    else:
        print('Es un triángulo Escaleno')
# Pedido de datos al usuario
primer_lado = int(input('Ingrese el primer lado del triángulo: '))
segundo_lado = int(input('Ingrese el segundo lado del triángulo: '))
tercer_lado = int(input('Ingrese el tercer lado del triángulo: '))
# Llamado a la función
tipo_de_triangulo(primer_lado, segundo_lado, tercer_lado)
