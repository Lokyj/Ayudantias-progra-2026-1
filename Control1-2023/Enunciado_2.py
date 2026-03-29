# Solicitar la cantidad de sacos - 0,4pts 
cantSacos = int(input("Ingrese la cantidad de sacos a vender --> "))

# Libras que comprende la cantidad a vender -- 0,7 por todo lo que involucra 
# Se calcula multiplicando los sacos por 25kg y dividiendo por la equivalencia de la libra
libras = (float(cantSacos) / 0.453592) * 25
print(f"La cantidad ingresada de sacos corresponde a {libras} libras del producto")

# Cantidad en pesos chilenos a cobrar -- 0,7 por todo lo que involucra
# Cada saco de 25 kilos cuesta $4500 CLP 
pesos = cantSacos * 4500
print(f"La cantidad ingresada de sacos corresponde a {pesos} pesos chilenos")

# Cantidad de dólares a cobrar -- 0,7 
# Se divide el total en pesos por el valor del dólar (810.73 CLP) 
dolares = float(pesos) / 810.73
print(f"La cantidad ingresada de sacos corresponde a {dolares} dolares")

# Último mensaje -- 0,3pts
print("Le voy a vender Oxido de Calcio a su papa, a su mama y a su perro y si no tiene perro, le regalo uno para que le compre a el tambien")

# Sumar 0,2pts por tener todo correcto 