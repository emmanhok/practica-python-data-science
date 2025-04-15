"""
Un establecimiento está vendiendo combustibles con descuentos variables.
Para el etanol, si la cantidad comprada es de hasta 15 litros, el descuento será del 2% por litro.
En caso contrario, será del 4% por litro.

Para el diésel, si la cantidad comprada es de hasta 15 litros, el descuento será del 3% por litro.
En caso contrario, será del 5% por litro.

Precio por litro:
etanol = R$1,70
diésel = R$2,00

Escribe un programa que lea la
    cantidad de litros vendidos
    tipo de combustible (E para etanol y D para diésel)
    calcule el valor a pagar por el cliente.
"""
E = 1.70
D = 2.00

combustible = int(input('¿Qué combustible cargó?\n1. Etanol\n2. Diesel\n'))
if combustible == 1:
    litros_cargados = float(input('¿Cuántos litros cargó?:\n'))
    if 0 < litros_cargados < 16:
        descuento = (E * 0.02) * litros_cargados
        print(f'El descuento es de: ${descuento}')
        print(f'El pago total es de: ${(E * litros_cargados) - descuento}')
    elif litros_cargados > 15:
        descuento = (E * 0.04) * litros_cargados
        print(f'El descuento es de: ${descuento}')
        print(f'El pago total es de: ${(E * litros_cargados) - descuento}')
elif combustible == 2:
    litros_cargados = float(input('¿Cuántos litros cargó?:\n'))
    if 0 < litros_cargados < 16:
        descuento = (D * 0.03) * litros_cargados
        print(f'El descuento es de: ${descuento}')
        print(f'El pago total es de: ${(D * litros_cargados) - descuento}')
    elif litros_cargados > 15:
        descuento = (D * 0.05) * litros_cargados
        print(f'El descuento es de: ${descuento}')
        print(f'El pago total es de: ${(D * litros_cargados) - descuento}')
else:
    print('Opción inválida')

