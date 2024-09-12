def imprimir_centrada(cadena):
    espacios = (80 - len(cadena)) // 2
    print(' ' * espacios + cadena)


cadena = input("Ingrese una cadena de caracteres: ")
imprimir_centrada(cadena)