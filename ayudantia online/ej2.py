
def calcular_venta(tipo_impresion_func, cantidad_func):
    if tipo_impresion_func == 1:
        valor = 50 * cantidad_func 
        return valor
    elif tipo_impresion_func == 2:
        valor = 150 *cantidad_func
        return valor
    else:
        return 0
        
def mostrar_reporte(total_bn, total_color, dinero, stock):
    print(f"se vendieron {total_bn} blanco y negro, {total_color} a color")
    print(f"se recaudó {dinero} y quedaron {stock} hojas ")
   


stock = 500
dinero_recaudado = 0

total_bn = 0
total_color = 0

while stock > 0:
    print("Seleccione una opcion: 1- Registrar venta 2- Ver reporte y 3- Salir")
    opcion = int(input("que desea hacer?"))
    if opcion == 1:
        tipo_impresion = int(input("Que tipo de impresion desea?"))
        cantidad = int(input("Cuantas desea?")) 
        if cantidad > stock:
            continue
        if tipo_impresion == 1:
            total_bn = total_bn + monto
        elif tipo_impresion == 2:
            monto = calcular_venta(tipo_impresion, cantidad)
            total_color = total_color + monto
            
        dinero_recaudado = total_color + total_bn
        stock = stock - cantidad
        
    elif opcion == 2:
        mostrar_reporte(total_bn, total_color, dinero_recaudado, stock)
    elif opcion == 3:
        break

print("aca")
