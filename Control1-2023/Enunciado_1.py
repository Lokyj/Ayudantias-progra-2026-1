
fans_harley = int(input("Ingrese la cantidad de fans de Harley Quinn: "))
fans_joker = int(input("Ingrese la cantidad de fans de The Joker: "))

total_fans = fans_harley + fans_joker

if fans_harley >= (0.58 * total_fans):
    print("Ganador: Harley Quinn")

elif fans_joker >= (0.54 * total_fans):
    print("Ganador: The Joker")

else:
    print("Ganador: Mr. Freeze")
