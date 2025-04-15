"""
Los números primos tienen diversas aplicaciones en Ciencia de Datos, como en criptografía y seguridad.
Un número primo es aquel que es divisible solo por sí mismo y por 1.
Por lo tanto, crea un programa que solicite un número entero y determine si es un número primo o no.
"""
numero = int(input('Ingrese un número para determinar si es o no primo: '))
for i in range(2, int(numero ** 0.5) + 1):
    if numero % i == 0:
        print('El número NO ES PRIMO')
        break
else:
    print('El número SI ES PRIMO')
