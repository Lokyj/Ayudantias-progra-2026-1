precio = 2500
total_extra= 0
recaudado = 0
while True:
  nombre = input("ingrese su nombre ")
  if nombre == "Fin":
    break
  cantidad = int(input("cuantos completos desea comprar?"))
  for i in range(cantidad):
    extra = input("desea agregar palta extra?")
    if extra == "s":
      recaudado = recaudado + precio + 500
      total_extra = total_extra + 1 
    else:
      recaudado = recaudado + precio

print(f"se recaudó: {recaudado}")
print(f"se pidió {total_extra} veces la palta extra")
