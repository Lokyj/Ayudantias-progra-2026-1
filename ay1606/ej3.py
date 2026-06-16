import csv
import matplotlib.pyplot as plt

alumnos = []
notas = []
colores = []

with open("alumnos.csv", encoding = "utf-8") as f:
    lector = csv.DictReader(f)
    for linea in lector:
        alumnos.append(linea["nombre"])
        notas.append(float(linea["nota_final"]))

for nota in notas: 
    if nota >= 4.0:
        colores.append("green")
    else:
        colores.append("red")

promedio = sum(notas)/len(notas)

plt.axvline(4, label="Aprobacion")
plt.axvline(promedio, label= "Promedio")

plt.barh(alumnos,notas, color= colores)
plt.title("Notas por alumno")
plt.xlabel("Alumnos")
plt.ylabel("Notas")
plt.legend()
plt.show()
        