seleccion=int(input("Escriba 1 para convertir de fahrenheir a celcius o 2 para converitr de celcius a fahrenheit"))
if seleccion==1:
    temp1=int(input("Ingrese la temperatura en fahrenheit"))
    rta=(temp1-32)*(5/9)
    print (f"La temperatura de {temp1} son {rta} celcius.")
elif seleccion==1:
    temp2=int(input("Ingrese la temperatura en fahrenheit"))
    rta=(temp2*5/9)+32
    print (f"La temperatura de {temp2} son {rta} celcius.")
else:
    print("Instruccion no valida.")