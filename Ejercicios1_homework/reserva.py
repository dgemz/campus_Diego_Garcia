print("Bienvenido, porfavor ingrese su edad y la calidad de la membrecia. ")
edad=int(input("Digite su edad. "))
membresia=int(input("Seleccione el nivel de la membresia (0 si no tiene y niveles de membrecia 1, 2 y 3). "))
print("El precio del boleto entre los 15 a 25 años es de $50, para las personas que tiene entre 26 y 40 años se les cobra $45 y para los mayores de 50 de $40.")
precio=0
if edad<15:
    print("Edad no valida, tienes que ser mayor a 15 años")
elif edad>=15 and edad<25:
    precio=50
elif edad>=25 and edad<40:
    precio=45
elif edad>=40:
    precio=40

if membresia==0:
    print(f"El precio de su boleta es de {precio}")
    print("Gracias por su compra.")
if membresia==1:
    precio=precio-(precio*0.1)
    print(f"El precio de su boleta es de {precio} por ser nivel {membresia}, de le aplicó un descuento del 10%.")
    print("Gracias por su compra.")
elif membresia==2:
    precio=precio-(precio*0.2)
    print(f"El precio de su boleta es de {precio} por ser nivel {membresia}, de le aplicó un descuento del 20%.")
    print("Gracias por su compra.")
elif membresia==3:
    precio=precio-(precio*0.3)
    print(f"El precio de su boleta es de {precio} por ser nivel {membresia}, de le aplicó un descuento del 30%.")
    print("Gracias por su compra.")
else:
    print("Nivel de membresia no valido, intentelo más tarde.")