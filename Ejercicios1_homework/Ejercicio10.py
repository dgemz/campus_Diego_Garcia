import random
while True:
    numa = random.randint(1, 6)
    if numa!=6:
        print(f"El dado cayó {numa}.")
        sis=input("Intentalo de nuevo")
    else:
       print(f"El dado cayó en {6}. Ganaste") 
       break