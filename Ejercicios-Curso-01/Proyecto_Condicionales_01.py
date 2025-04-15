# Un programa debe ser escrito para leer dos números y luego preguntar a la persona usuaria qué operación desea realizar.
# El resultado de la operación debe incluir información sobre el número, si es par o impar, positivo o negativo,
# entero o decimal.

# Primero creo funciones para validar la información sobre el tipo de número que es el resultado
def informacion_resultado(resultado):
    if resultado % 2 == 0:
        print('El resultado es PAR')
    else:
        print('El resultado es IMPAR')
    if resultado > 0:
        print('El resultado es POSITIVO')
    else:
        print('El resultado es NEGATIVO')
    if type(resultado) == int:
        print('El número es ENTERO')
    else:
        print('El resultado es DECIMAL')
# Se pide al usuario los 2 números
primer_numero = int(input('Ingrese el primer número: '))
segundo_numero = int(input('Ingrese el segundo número: '))
# Se pide al usuario la operación que desea realizar con esos dos números
operacion = int(input("Ingrese la opción que desea realizar:\n1.Suma\n2.Resta\n3.Multiplicación\n4.División\n"))
if operacion == 1:
    resultado = primer_numero + segundo_numero
    print(f'La suma es: {resultado}')
    informacion_resultado(resultado)
elif operacion == 2:
    resultado = primer_numero - segundo_numero
    print(f'La resta es: {resultado}')
    informacion_resultado(resultado)
elif operacion == 3:
    resultado = primer_numero * segundo_numero
    print(f'La multiplicación es: {resultado}')
    informacion_resultado(resultado)
elif operacion == 4:
    resultado = primer_numero / segundo_numero
    print(f'La división es: {resultado}')
    informacion_resultado(resultado)
else:
    print('Opción inválida')
print('Fin del Programa')
