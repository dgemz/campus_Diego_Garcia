num=int(input("Ingrese el número para saber si es primo. "))
if num>0:
    for n in range(1, num):
        if num%n==0:
            contador=contador+1
            if contador>1:
                print("El número no es primo.")
            else:
                print("El número es primo.")
else:
    print("El número no es primo por ser negativo.")