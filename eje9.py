def ordenada(lista):
    for i in range(len(lista) - 1):
        if lista[i] > lista[i + 1]:
            return False
    return True


lista = [int(x) for x in input("Ingrese una lista de números separados por espacios: ").split()]
if ordenada(lista):
    print("La lista está ordenada en forma ascendente.")
else:
    print("La lista no está ordenada en forma ascendente.")