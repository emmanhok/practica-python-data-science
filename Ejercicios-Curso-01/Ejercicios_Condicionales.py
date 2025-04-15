
primer_numero = int(input('Ingrese un número: '))
segundo_numero = int(input('Ingrese otro número: '))
print(f'Primer número: {primer_numero}')
print(f'Segundo número: {segundo_numero}')
# Escribe un programa que pida a la persona usuaria que proporcione dos números y muestre el número más grande.
if primer_numero > segundo_numero:
    print(f'El número mayor es: {primer_numero}')
elif segundo_numero > primer_numero:
    print(f'El número mayor es: {segundo_numero}')
else:
    print('Ambos números son iguales')
# Escribe un programa que solicite el porcentaje de crecimiento de producción de una empresa
# e informe si hubo un crecimiento (porcentaje positivo) o una disminución (porcentaje negativo).
porcentaje = float(input('Ingrese el porcentaje de crecimiento o de decremento de su empresa: '))
if porcentaje > 0:
    print(f'Hubo un crecimiento del: {porcentaje}%')
elif porcentaje < 0:
    print(f'Hubo un decremento del: {porcentaje}%')
else:
    print(f'Hubo un estancamiento')
# Escribe un programa que determine si una letra proporcionada por la persona usuaria es una vocal o una consonante.
letra1 = input('Ingrese una letra del abecedario: ')
if letra1 == 'a' or letra1 == 'e' or letra1 == 'i' or letra1 == 'o' or  letra1 == 'u':
    print('Es vocal')
else:
    print('Es consonante')
