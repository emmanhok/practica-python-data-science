"""
Crea un código que recoja en una lista 5 números enteros aleatorios e imprima la lista. Ejemplo: [1, 4, 7, 2, 4].
"""
import random

lista = []
for i in range(0, 6):
    numero_aleatorio = int(random.randint(0, 100))
    lista.append(numero_aleatorio)
print(lista)
"""
Recoge nuevamente 5 números enteros e imprime la lista en orden inverso al enviado.
"""
# print(lista.reverse()) Aquí he descubierto que las funciones, por lo menos, en listas, deben aplicarse fuera del print
lista.reverse()
print(lista)

"""
Los números primos tienen diversas aplicaciones en Ciencia de Datos, como en criptografía y seguridad.
Un número primo es aquel que es divisible solo por sí mismo y por 1.
Por lo tanto, crea un programa que solicite un número entero y determine si es un número primo o no.
"""
# Se crea lista vacía
lista = []
# Se pide un número al usuario
numero = int(input('Ingresa un número: '))
# Se crea un primer ciclo para recorrer números del 2 al 30
for i in range(2, numero):
# Se utiliza una bandera que se mantiene si el numero es_primo, sino será transformada a False y no se agrega a la lista
    es_primo = True
# Se crea un segundo ciclo para ir verificando si el numero del rango entre 2 y sí mismo da resto 0 o no
    for divisor in range(2, i):
# Condicional para saber si el resto da 0 la bandera es_primo será falsa y se corta el ciclo y no se agrega a la lista
        if i % divisor == 0:
            es_primo = False
            break
# Condicional que agrega el numero i(que es el que va iterando dentro del rango 2 hasta el numero que ingreso el usuario)
# Si se mantiene la bandera es_primo como True, es decir que no encontró otro divisor que de resto 0 se agrega a la lista
    if es_primo:
        lista.append(i)
# Se imprime la listaa completa de los números primos entre el rango establecido en el primer ciclo for
print(lista)
