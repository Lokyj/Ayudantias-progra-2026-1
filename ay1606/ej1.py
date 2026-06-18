import matplotlib.pyplot as plt
dias = []
ventas= []
with open("ventas_diarias.txt",mode="r" ,encoding= "utf-8") as f:
    for i,linea in enumerate(f):
        linea = linea.strip()
        dias.append(i+1)
        ventas.append(int(linea))

venta_prom = sum(ventas)/len(ventas)

plt.bar(dias,ventas)
plt.ylabel("Venta")
plt.xlabel("Dia")
plt.title("Ventas por dia")

plt.axhline(venta_prom,color="red")
plt.show()