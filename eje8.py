def eliminar_palabras(lista_original, palabras_a_eliminar):
    return [palabra for palabra in lista_original if palabra not in palabras_a_eliminar]


lista_original = ["manzana", "banana", "uva", "pera", "durazno"]
palabras_a_eliminar = ["banana", "uva"]

lista_resultante = eliminar_palabras(lista_original, palabras_a_eliminar)

print("Lista original:", lista_original)
print("Palabras a eliminar:", palabras_a_eliminar)
print("Lista resultante:", lista_resultante)