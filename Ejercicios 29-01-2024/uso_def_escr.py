def compra(nombre, precio, cant):
    total=precio*cant
    print(f"Hola, {nombre}, el total de su compra es {total} "  )

print("Bienvenido, a su calculadora de compras. ")
nombre = str(input("Ingrese su nombre "))
precio = float(input("Ingrese el precio del producto "))
cant = int(input("Ingrese la cantidad del producto "))
compra(nombre, precio, cant ) 