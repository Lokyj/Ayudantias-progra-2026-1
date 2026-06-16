import matplotlib.pyplot as plt

lenguajes = []
puntajes = []

with open('lenguajes.txt', 'r') as archivo:
    for linea in archivo:
        partes = linea.strip().split(',')
        if len(partes) == 2:
            lenguajes.append(partes[0])
            puntajes.append(int(partes[1]))

colores = ['green' if p >= 70 else 'red' for p in puntajes]

plt.barh(lenguajes, puntajes, color=colores, alpha=0.7, edgecolor='black')
promedio = sum(puntajes) / len(puntajes)
plt.axvline(x=promedio, color='grey', linestyle='--', linewidth=2, label=f'Promedio ({promedio})')


plt.title('Radiografía de Popularidad de Lenguajes')
plt.xlabel('Puntaje')
plt.ylabel('Lenguaje')

plt.gca().invert_yaxis() 

plt.xlim(0, 100)

plt.legend()
plt.tight_layout()
plt.show()