def es_fecha_valida(dia, mes, año):
    meses_31_dias = [1, 3, 5, 7, 8, 10, 12]
    meses_30_dias = [4, 6, 9, 11]
    
    if año < 0:
        return False
    if mes < 1 or mes > 12:
        return False
    if mes in meses_31_dias and (dia < 1 or dia > 31):
        return False
    if mes in meses_30_dias and (dia < 1 or dia > 30):
        return False
    if mes == 2:
        if (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0):  # Año bisiesto
            if dia < 1 or dia > 29:
                return False
        else:
            if dia < 1 or dia > 28:
                return False
    return True

dia = int(input("Ingrese el día: "))
mes = int(input("Ingrese el mes: "))
año = int(input("Ingrese el año: "))

if es_fecha_valida(dia, mes, año):
    print("La fecha es válida.")
else:
    print("La fecha no es válida.")