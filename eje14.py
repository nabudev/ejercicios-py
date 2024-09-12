def eliminar_claves(diccionario, claves_a_eliminar):
    exito = False
    for clave in claves_a_eliminar:
        if clave in diccionario:
            del diccionario[clave]
        exito = True
    return diccionario, exito


diccionario = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
claves_a_eliminar = ['a', 'c']

diccionario_modificado, exito = eliminar_claves(diccionario, claves_a_eliminar)

print("Diccionario modificado:", diccionario_modificado)
if exito:
    print("Operación exitosa.")
else:
    print("No se encontraron claves para eliminar.")