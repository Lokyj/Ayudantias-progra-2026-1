
fecha = int(input("Ingrese la fecha: "))
anio = fecha // 10000
mes_dia = fecha % 10000
mes = mes_dia // 100
dia = mes_dia % 100
print(f"Año {anio}, Mes {mes}, Día {dia}")

if 321 <= mes_dia <= 620: # 321 viene de 0321 -> 21 de marzo
    estacion = "Otoño"
elif 621 <= mes_dia <= 920:
    estacion = "Invierno"
elif 921 <= mes_dia <= 1220:
    estacion = "Primavera"
else:
    # Cubre desde el 21 de diciembre (1221) hasta el 20 de marzo (320)
    estacion = "Verano"

print(f"La estación asociada es: {estacion}")
