
fecha = int(input("Ingrese la fecha: "))

anio = fecha // 10000
mes = (fecha % 10000) // 100
dia = fecha % 100

print(f"Año {anio}, Mes {mes}, Día {dia}")

if mes == 1 or mes == 2:
    estacion = "Verano"
elif mes == 3:
    if dia < 21:
        estacion = "Verano"
    else:
        estacion = "Otoño"
elif mes == 4 or mes == 5:
    estacion = "Otoño"
elif mes == 6:
    if dia < 21:
        estacion = "Otoño"
    else:
        estacion = "Invierno"
elif mes == 7 or mes == 8:
    estacion = "Invierno"
elif mes == 9:
    if dia < 21:
        estacion = "Invierno"
    else:
        estacion = "Primavera"
elif mes == 10 or mes == 11:
    estacion = "Primavera"
elif mes == 12:
    if dia < 21:
        estacion = "Primavera"
    else:
        estacion = "Verano"

print(f"La estación asociada es: {estacion}")
