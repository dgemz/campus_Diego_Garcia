import random
numa = random.randint(1, 100)
while True:
    num=int(input("Escriba un número entre 1-100 "))
    if num>numa:
        print("El número para adivinar es menor.")
    elif num<numa:
        print("El número para adivinar es mayor.")
    if num==numa:
        print("GANASTE")
        break