def calcular_vuelto(total_compra, dinero_recibido):
    if dinero_recibido < total_compra:
        print("Error: El dinero recibido es insuficiente.")
        return

    vuelto = dinero_recibido - total_compra
    billetes = [500, 100, 50, 20, 10, 5, 1]
    cantidades = {}

    for billete in billetes:
        cantidades[billete] = vuelto // billete
        vuelto %= billete

    print("El vuelto a entregar es:")
    for billete, cantidad in cantidades.items():
        if cantidad > 0:
            print(f"{cantidad} billete(s) de ${billete}")


total_compra = int(input("Ingrese el total de la compra: "))
dinero_recibido = int(input("Ingrese el dinero recibido: "))

calcular_vuelto(total_compra, dinero_recibido)