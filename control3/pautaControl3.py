
def ingresarCompra():
    nombre = input("Ingrese el nombre del cliente: ")
    edad = int(input("Ingrese la edad del cliente: "))
    rut = input("Ingrese el RUT del cliente: ")
    if edad >= 15 and edad < 23:
        return "Categoria A"
    elif edad >= 23 and edad < 36:
        return "Categoria B"
    elif edad >= 36 and edad <= 60:
        return "Categoria C"
    else:
        return "Fuera de rango"

def verEdades(Categoria_A, Categoria_B, Categoria_C, Total_vendidas):
    Porcentaje_A = (Categoria_A / Total_vendidas) * 100
    Porcentaje_B = (Categoria_B / Total_vendidas) * 100
    Porcentaje_C = (Categoria_C / Total_vendidas) * 100
    print(f"Total actual: {Total_vendidas} personas.")
    print(f"Categoría A: {Porcentaje_A}%")
    print(f"Categoría B: {Porcentaje_B}%")
    print(f"Categoría C: {Porcentaje_C}%")

def verMontoRecaudado(total_vendidas):
    precio_entrada = 10000
    monto_recaudado = total_vendidas * precio_entrada
    print(f"Monto total recaudado: ${monto_recaudado}")

stock_entradas = 1000
Categoria_A_Main = 0
Categoria_B_Main = 0
Categoria_C_Main = 0

while stock_entradas > 0:
    print("Que accion desea realizar?")
    print("Seleccionar: 1) Ingresar compra 2) Ver edades 3) Ver monto recaudado")

    opcion = int(input("Ingrese el numero de la opcion: "))
    if opcion == 1:
        categoria = ingresarCompra()
        if categoria == "Categoria A":
            Categoria_A_Main += 1
            stock_entradas -= 1
        elif categoria == "Categoria B":
            Categoria_B_Main += 1
            stock_entradas -= 1
        elif categoria == "Categoria C":
            Categoria_C_Main += 1
            stock_entradas -= 1
        else:
            print("Cliente fuera de rango, no se registra la compra.")
    elif opcion == 2:
        Total_vendidas_Main = Categoria_A_Main + Categoria_B_Main + Categoria_C_Main
        verEdades(Categoria_A_Main, Categoria_B_Main, Categoria_C_Main, Total_vendidas_Main)
    elif opcion == 3:
        Total_vendidas_Main = Categoria_A_Main + Categoria_B_Main + Categoria_C_Main
        verMontoRecaudado(Total_vendidas_Main)
print("No quedan entradas disponibles.")
Total_vendidas_Main = Categoria_A_Main + Categoria_B_Main + Categoria_C_Main
verEdades(Categoria_A_Main, Categoria_B_Main, Categoria_C_Main, Total_vendidas_Main)
verMontoRecaudado(Total_vendidas_Main)