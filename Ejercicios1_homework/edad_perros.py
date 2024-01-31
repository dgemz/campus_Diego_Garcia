print("Calculadora de años caninos.")
peso=int(input("Ingrese el peso de su perro en kg "))
yearp=int(input("Ingrese los años humanos que tiene su perro: "))
yearh=15
years=0
if peso<10:
    print(f"La edad de su perro raza pequeña es {yearh}")
else:
    if years==2:
        years=yearh+6
    elif yearp>=3:
        years=4*yearp
        print(f"La edad de su perro raza pequeña es {years}")
    else:
        if peso>=10 and peso<22:
            print(f"La edad de su perro raza mediana es {yearh}")
        elif yearp==2:
            years=yearh+9
        elif yearp>=3:
            years=16*yearp
            print(f"La edad de su perro raza mediana es {years}")
        else:
            if peso>=10 and peso<22:
                print(f"La edad de su perro raza grande es {yearh}")
            elif yearp==2:
                years=yearh+12
            elif yearp>=3:
                years=18*yearp
                print(f"La edad de su perro raza grande es {years}")
