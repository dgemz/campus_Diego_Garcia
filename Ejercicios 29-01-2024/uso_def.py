def compras(*productos):
    print(productos)

compras("Camisa", "Televisor", "Arroz")

def persona(**datos):
    print(datos)
 
persona(Nombre = str(input("Ingrese su nombre ")), Email = str(input("Ingrese su correo "))) 
#Esto imprime: {'Nombre': 'Pepe Perez', 'Email': 'pepe@email.com'}