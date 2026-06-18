import csv
import matplotlib.pyplot as plt

juegos = []
rating = []

with open("videojuegos.csv",mode="r", encoding="utf-8") as f:
    lector = csv.reader(f,delimiter=";")
    headears = next(lector)
    for linea in lector:
        juegos.append(linea[0])
        rating.append(int(linea[1]))

plt.barh(juegos,rating)
plt.ylabel("Juegos")
plt.xlabel("rating")
plt.title("rating por juego")
#maximo = max(rating)
#minimo = min(rating)
#plt.xlim(minimo,maximo)
#plt.margins(y=0.5)
plt.show()