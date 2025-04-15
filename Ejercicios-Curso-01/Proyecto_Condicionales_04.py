"""
En una empresa de venta de bienes raíces, debes crear un código que analice los datos de ventas anuales
para ayudar a la dirección en la toma de decisiones.
El código debe recopilar los datos de cantidad de ventas durante los años 2022 y 2023 y calcular la variación porcentual.
A partir del valor de la variación, se deben proporcionar las siguientes sugerencias:
•	Para una variación superior al 20%: bonificación para el equipo de ventas.
•	Para una variación entre el 2% y el 20%: pequeña bonificación para el equipo de ventas.
•	Para una variación entre el 2% y el -10%: planificación de políticas de incentivo a las ventas.
•	Para bonificaciones inferiores al -10%: recorte de gastos.
"""
ventas_2022 = 1000
ventas_2023 = 899

variacion_porcentual = (ventas_2023 - ventas_2022) / ventas_2022 * 100
print(variacion_porcentual)

if variacion_porcentual > 20:
    print('Bonificación para el equipo de ventas')
elif 2 <= variacion_porcentual <= 20:
    print('Pequeña bonificación para el equipo de ventas')
elif  2 > variacion_porcentual >= -10:
    print('Planificación de políticas de incentivo a las ventas')
elif variacion_porcentual < -10:
    print('Recorte de gastos')
