"""Crear dos funciones
Función imprimirSaludo para que no retorne valor y solo imprima el mensaje “Hola nombre”
Función calcularArea retorne el valor del área de un cuadrado solo pidiendo el lado de entrada y retornando el resultado, se debe imprimir en el método principal.
"""

def saludo(nombre ):
    print(f"Hola, {nombre}" )
    
def calculararea(lado):
    total=lado*lado
    print(f"el area del cuadrado es {total} centimetros cuadrados")
    
print("Bienvenido")
nombre=(str(input("Ingrese su nombre ")))
lado=int(input("Ingrese la medida del lado en cm "))
print=(saludo(nombre) + calculararea(lado))