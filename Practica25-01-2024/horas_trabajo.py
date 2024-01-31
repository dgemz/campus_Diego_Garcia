horastrab=int(input("Cuantas horas trabajo hoy? "))
if horastrab>0 and horastrab<=10: 
    pago=horastrab*5
    print(f"Su pago es de {pago}")
elif horastrab<=20:
    pago=horastrab*10
    print(f"Su pago es de {pago}")
elif horastrab>20:
    pago=horastrab*15
    print(f"Su pago es de {pago}")
else:
    print("Hora no valida.")
