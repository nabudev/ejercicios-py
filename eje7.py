N = int(input("Ingrese el valor de N: "))
cuadrados = [x ** 2 for x in range(1, N + 1)]


print("Los últimos 10 cuadrados son:", cuadrados[-10:])
