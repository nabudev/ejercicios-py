def patron_1(filas):
    for i in range(1, filas + 1):
        print('*' * i)


filas = int(input("Ingrese la cantidad de filas: "))
patron_1(filas)
def patron_2(filas):
    for i in range(filas, 0, -1):
        print('*' * i)


filas = int(input("Ingrese la cantidad de filas: "))
patron_2(filas)