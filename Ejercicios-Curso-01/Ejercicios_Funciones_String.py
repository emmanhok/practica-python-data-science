frase1 = input('Ingresar frase: ')
print('Frase original:\n')
def modificar_frase(frase):
    # Crea un código que solicite una frase al usuario y luego imprima la misma frase ingresada pero en mayúsculas.
    print(f'A mayúsculas:\n{frase1.upper()}')
    # Crea un código que solicite una frase al usuario y luego imprima la misma frase ingresada pero en minúsculas.
    print(f'A minúsculas:\n{frase1.lower()}')
    # Crea una variable llamada "frase" y asígnale una cadena de texto de tu elección. Luego, imprime la frase sin espacios en blanco al principio y al final.
    print(f'Sin espacios en blanco al inicio y final:\n{frase1.strip()}')
    # Crea un código que solicite una frase al usuario y luego imprima la misma frase con todas las vocales "e" reemplazadas por la letra "f".
    print(f'Reemplazo de "e" por "f":\n{frase1.replace('e', 'f')}')
    # Crea un código que solicite una frase al usuario y luego imprima la misma frase con todas las vocales "a" reemplazadas por el carácter "@".
    print(f'Reemplazo de "a" por "@":\n{frase1.replace('a', '@')}')
modificar_frase(frase1)
