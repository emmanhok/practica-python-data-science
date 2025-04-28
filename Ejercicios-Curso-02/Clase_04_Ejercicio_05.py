"""
Crea un diccionario usando la comprensión de diccionarios (dict comprehension) en el que
las claves estén en la lista meses =
    ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez']
y los valores estén en gasto =
    [860, 490, 1010, 780, 900, 630, 590, 770, 620, 560, 840, 360]
"""
meses = ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez']
pagos = [860, 490, 1010, 780, 900, 630, 590, 770, 620, 560, 840, 360]
diccionario_meses_pagos = {mes: pago for mes, pago in zip(meses, pagos)}
print(diccionario_meses_pagos)

