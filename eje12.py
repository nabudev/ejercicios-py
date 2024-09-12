def fecha_extendida(fecha):
    dia, mes, año = fecha
    meses = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre']
    return f"{dia} de {meses[mes - 1]} de {año}"


fecha = (int(input("Ingrese el día: ")), int(input("Ingrese el mes: ")), int(input("Ingrese el año: ")))
print(fecha_extendida(fecha))