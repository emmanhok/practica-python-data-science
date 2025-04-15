"""
Los empleados de un departamento de tu empresa recibirán una bonificación del 10% de su salario debido a un
excelente rendimiento del equipo. El departamento de finanzas ha solicitado tu ayuda para verificar las consecuencias
financieras de esta bonificación en los recursos.
Se te ha enviado una lista con los salarios que recibirán la bonificación:
[1172, 1644, 2617, 5130, 5532, 6341, 6650, 7238, 7685, 7782, 7903].
La bonificación de cada empleado no puede ser inferior a 200.
En el código, convierte cada uno de los salarios en claves de un diccionario y
la bonificación de cada salario en el valor correspondiente.
Luego:
    informa el gasto total en bonificaciones,
    cuántos empleados recibieron la bonificación mínima y
    cuál fue el valor más alto de la bonificación proporcionada.
"""
# Creación de lista con los salarios a bonificar
salarios_para_bonificar = [1172, 1644, 2617, 5130, 5532, 6341, 6650, 7238, 7685, 7782, 7903]
# Creación de diccionario donde se almacenaran los salarios con sus respectivas bonificaciones
salarios_bonificados = {}
# Se inicializan 2 variables:
# una para calcular la suma de quienes fueron beneficiados con el minimo y
# otra para calcular la bonificación más alta
cantidad_de_bonificaciones_minima = 0
bonificacion_mas_alta = -1
# Utilizo un solo ciclo for para veerificar la bonificacion minima, contar cuántos la obtienen y llenar el diccionario
for salario in salarios_para_bonificar:
    bonificacion = salario * 0.1  # Cálculo del 10% de cada salario
    if bonificacion < 200:  # Condicional para darle un mínimo de 200 de bonificación a quienes no llegan con el 10%
        bonificacion = 200
        cantidad_de_bonificaciones_minima += 1  # Contador para saber cuántos reciben la bonificación mínima
    if bonificacion > bonificacion_mas_alta:  # Condicional para ir verificando cuál es la bonificación más alta
        bonificacion_mas_alta = bonificacion
    salarios_bonificados[f'{salario}'] = bonificacion  # Una vez hechas las comprovaciones se va llenando el diccionario
# Con el diccionario completo se suman los valores
suma_total_bonificaciones = sum(salarios_bonificados.values())
# Se imprime: diccionario, suma total de las bonificaciones, cantidad de bonificaciones mínimas y valor más alto de bonificación
print(salarios_bonificados)
print(f'La suma total en bonificaciones es: {suma_total_bonificaciones:.2f}')
print(f'La cantidad de empleados que recibieron la bonificación mínima es: {cantidad_de_bonificaciones_minima}')
print(f'El valor más alto de las bonificaciones fue: {bonificacion_mas_alta:.2f}')
