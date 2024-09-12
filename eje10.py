def es_capicua(cadena):
    longitud = len(cadena)
    for i in range(longitud // 2):
        if cadena[i] != cadena[longitud - i - 1]:
            return False
    return True


cadena = input("Ingrese una cadena de caracteres: ")
if es_capicua(cadena):
    print("La cadena es capicúa.")
else:
    print("La cadena no es capicúa.")