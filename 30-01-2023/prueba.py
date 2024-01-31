tareas={}

def add_hw(name, impt):
   tareas[name]= impt 
   
   
def prin_hw():
    for tarea in sorted(tareas.items(), key=lambda x: x[1], reverse=True):
        print(tarea)

def delete_hw(borrar):
    del tareas [borrar]

print("Bienvenido.")
print("1 - Añadir tarea.")
print("2 - Mostrar tareas pendientes.")
print("3 - Eliminar tarea.")
seleccion=int(input("Ingrese la selección del menú.  "))
while seleccion!=0:

    if seleccion==1:
        num=int(input("Cuantas tareas desea añadir?  "))
        for n in range (1, num+1): 
            name=str(input("Ingrese el nombre de la tarea  "))
            impt=int(input("Ingrese la prioridad de la tarea de 1 a 5 (Por defecto sera 5) "))
            if impt<=0 or impt>=6:
                impt=5
            add_hw(name, impt)

    elif seleccion==2:
        prin_hw()
    elif seleccion==3:
        borrar = str(input("Ingrese el nombre de la tarea que desea borrar.  "))
        delete_hw(borrar)

    print("1 - Añadir tarea.")
    print("2 - Mostrar tareas pendientes.")
    print("3 - Eliminar tarea.")
    print("0 - salir del programa.")
    seleccion=int(input("Ingrese la selección del menú.  "))