num=int(input("Ingrese hasta que número de la serie de fibonacci desea saber. "))
num0=0
num1=1
if num<=0:
    print("No hay números que digitar.")
elif num==1:
    print(num0)
else:
    print(num0)
    print(num1)
    for n in range (num-2):
        numero=num1+num0
        print (numero)
        num0=num1
        num1=numero
    