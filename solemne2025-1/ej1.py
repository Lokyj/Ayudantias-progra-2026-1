n = int(input("ingrese la cantidad de vueltas"))

corredorA = int(input("cuanto demora el corredor A en dar una vuelta?"))

corredorB = int(input("cuanto demora el corredor B en dar una vuelta?"))


tiempoTotalA= 0
tiempoTotalB= 0

for vueltas in range(n):
    
    if vueltas == 4:
        corredorA = corredorA + corredorA*0.1
        
    
    if vueltas == 9:
        
        corredorB = corredorB + corredorB*0.15
        
    if vueltas > 4:
        corredorA = corredorA + corredorA*0.02
        if vueltas > 9:
            corredorB = corredorB + corredorB * 0.1
    

    print(f"tiempo que tardo en esta vuelta el corredor A: {corredorA}")
    print(f"tiempo que tardo en esta vuelta el corredor B: {corredorB}")
    
    tiempoTotalB= tiempoTotalB + corredorB
    tiempoTotalA= tiempoTotalA + corredorA
    

if tiempoTotalA < tiempoTotalB:
    print(f"ganó A con un tiempo de {tiempoTotalA}")
    
else: 
    print(f"ganó B con un tiempo de {tiempoTotalB}")
