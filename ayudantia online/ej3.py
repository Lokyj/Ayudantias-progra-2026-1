def calcularPorcentaje(votos_opcion, total_emitidos):
    porcentaje = votos_opcion/ total_emitidos * 100
    return porcentaje



def mostrar_urna(votos_listaA, votos_listaB , nulos, total):
    
    porcentaje_A = calcularPorcentaje(votos_listaA,total)
    porcentaje_B = calcularPorcentaje(votos_listaB,total)
    porcentaje_Nulos = calcularPorcentaje(nulos,total)
    
    print(f"hubo un total de {total} votos, un {porcentaje_A}% fueron de la Lista A, un {porcentaje_B}% de la Lista B y un {porcentaje_Nulos} fueron nulos")
    
def emitir_voto():
    voto = int(input("que vota?"))
    if voto == 1:
        return "Lista A"
    elif voto == 2:
        return "Lista B"
    elif voto == 3:
        return "Nulo"

    
votos_listaA = 0
votos_listaB = 0
nulos = 0
total= 0
for i in range(300):
    print("1. Emitir voto, 2. Ver escrutinio parcial y 3. Cerrar mesa")
    opcion = int(input("que desea hacer?"))
    if opcion == 1:
        voto = emitir_voto()
        if voto == "Lista A":
            votos_listaA = votos_listaA + 1
        elif voto == "Lista B":
            votos_listaB = votos_listaB + 1
        elif voto == "Nulo":
            nulos = nulos + 1
        total = total + 1
    elif opcion == 2:
        mostrar_urna(votos_listaA,votos_listaB,nulos, total)
    elif opcion == 3:
        break

        
