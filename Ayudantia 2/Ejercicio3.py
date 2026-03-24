jugado = int(input("Ingrese su número jugado (5 cifras): "))
ganador = int(input("Ingrese el número ganador (5 cifras): "))

if jugado == ganador:
    print("Premio Mayor")

elif (jugado // 100 == ganador // 100) or (jugado % 1000 == ganador % 1000):
    print("Terna")

elif jugado % 10 == ganador % 10:
    print("Terminación")

else:
    print("Siga participando")
