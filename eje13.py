def procesar_frase(frase):
    palabras = frase.split()
    conjunto_palabras = set(palabras)  
    lista_ordenada = sorted(conjunto_palabras, key=len)  
    return lista_ordenada


frase = input("Ingrese una frase: ")
resultado = procesar_frase(frase)
print("Palabras únicas ordenadas por longitud:", resultado)