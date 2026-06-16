import csv
import matplotlib.pyplot as plt

nombres = []
puntajes = []

with open("videojuegos.csv", "r", encoding="utf-8") as f:
    lector = csv.reader(f, delimiter=";")
    next(lector) 
    
    for fila in lector:
        nombres.append(fila[0])
        puntajes.append(int(fila[1]))

plt.barh(nombres, puntajes, color="coral")
plt.title("Puntajes de Videojuegos en Metacritic")
plt.xlabel("Puntaje")
plt.tight_layout() 
plt.show()