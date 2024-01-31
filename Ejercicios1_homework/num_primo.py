num=int(input("Ingrese el número para saber si es primo. "))
contador=0
if num>0:
    for n in range(2, num):
        if num%n==0:
            contador=contador+1
    if contador>1:
        print("El número no es primo.")
    else:
        print("El número es primo.")
elif num==1:
    print("No es primo.")
elif num==2:
    print("Es primo.")

else:
    print("El número no es primo por ser negativo.")