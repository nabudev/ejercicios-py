es_par = lambda x: x % 2 == 0


numero = int(input("Ingrese un número: "))
if es_par(numero):
    print(f"{numero} es par.")
else:
    print(f"{numero} es impar.")