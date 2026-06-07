def revisarEstudiante():
    nota1 = int(input("Ingrese nota 1 "))
    nota2 = int(input("Ingrese nota 2 "))
    nota3 = int(input("Ingrese nota 3 ")) 
    asistencia = int(input("Ingrese asistencia ")) 
    
    if asistencia >= 75:
        peor_nota = min(nota1,nota2,nota3)
        promedio = (nota1+nota2+nota3 - peor_nota)/2
    else:
        promedio = (nota1+nota2+nota3)/3
    
    print(f"promedio: {promedio}")
    if promedio >= 40:
        return "Aprobado"
    else:
        return "Reprobado"

def mostrarEstadisticas(aprobados2, reprobados2):
    total = aprobados2 + reprobados2
    print(f"Hubieron en total {total} alumnos")
    por_aprobados = aprobados2/total*100
    por_reprobados = reprobados2/total*100
    print(f"porcentaje aprobados: {por_aprobados} , reprobados : {por_reprobados}")
    
print("esto es main")
aprobados = 0
reprobados = 0

while True:
    resultado = revisarEstudiante()
    if resultado == "Aprobado":
        aprobados = aprobados + 1
    else:
        reprobados = reprobados + 1
    seguir= input("quiere seguir?")
    if seguir == "no":
        break

mostrarEstadisticas(aprobados, reprobados)

