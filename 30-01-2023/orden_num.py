def ordenar_lista(lista):
    negativos = []
    positivos = []
    for num in lista:
        if num < 0:
            negativos.append(num)
        elif num == 'fin':
            break
        else:
            positivos.append(num)
    positivos.sort()
    negativos.sort()
    return negativos + positivos
entrada_usuario = input("Ingrese un número entero (o escriba 'fin' para terminar): ")
lista = []
while entrada_usuario.lower() != 'fin':
    lista.append(int(entrada_usuario))
    entrada_usuario = input("Ingrese un número entero (o escriba 'fin' para terminar): ")
lista_ordenada = ordenar_lista(lista)
print("Lista ordenada:", lista_ordenada)