def mayor_estricto(a, b, c):
    mayor = max(a, b, c)
    if (mayor == a) + (mayor == b) + (mayor == c) == 1:
        return mayor
    return -1

a = int(input("Ingrese el primer número: "))
b = int(input("Ingrese el segundo número: "))
c = int(input("Ingrese el tercer número: "))

resultado = mayor_estricto(a, b, c)
if resultado != -1:
    print(f"El mayor estricto es: {resultado}")
else:
    print("No existe un mayor estricto.")