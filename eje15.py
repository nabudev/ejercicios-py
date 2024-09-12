def eliminar_subcadena(cadena, posicion, cantidad):
    return cadena[:posicion] + cadena[posicion + cantidad:]


cadena = input("Ingrese una cadena de caracteres: ")
posicion = int(input("Ingrese la posición donde empezar a eliminar: "))
cantidad = int(input("Ingrese la cantidad de caracteres a eliminar: "))

nueva_cadena = eliminar_subcadena(cadena, posicion, cantidad)
print("Cadena resultante:", nueva_cadena)