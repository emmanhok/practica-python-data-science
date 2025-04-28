"""
Crea un programa que solicite a la persona usuaria ingresar dos números enteros y
calcule la potencia del primer número elevado al segundo.
"""
from math import pow
primer_numero = int(input('Ingrese un número entero: '))
segundo_numero = int(input('Ingrese otro número entero: '))
potencia = pow(primer_numero, segundo_numero)
print(potencia)
