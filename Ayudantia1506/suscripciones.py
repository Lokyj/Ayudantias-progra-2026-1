import matplotlib.pyplot as plt

with open("suscripciones.txt", "r") as f:
    encabezados = next(f)
    anio = []
    A = []
    B = []
    for line in f:
        lineas = line.strip().split(',')
        anio.append(int(lineas[0]))
        A.append(int(lineas[1]))
        B.append(int(lineas[2]))

plt.plot(anio, A, marker='o', linestyle='--', color='blue', label='Categoría A')
plt.plot(anio, B, marker='s', linestyle='--', color='red', label='Categoría B')
plt.xlabel('Año')
plt.ylabel('Suscripciones')
plt.title('Suscripciones por año')
plt.legend()
plt.grid(True)
plt.show()