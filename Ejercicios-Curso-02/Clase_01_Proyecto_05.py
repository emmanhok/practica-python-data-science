"""
Haz un programa para una tienda que vende césped para jardines.
Esta tienda trabaja con jardines circulares y
el precio del metro cuadrado de césped es de $25,00.
Pide a la persona usuaria el radio del área circular y
devuelve el valor de cuánto tendrá que pagar
A=πr2
"""
import math

precio_por_metro_cuadrado = 25.00

radio = float(input('Ingrese el radio del área circular: '))
area = math.pi * (radio**2)
precio_a_pagar = area * precio_por_metro_cuadrado
print(f'Precio por el trabajo en el jardín: ${precio_a_pagar:.2f}')
