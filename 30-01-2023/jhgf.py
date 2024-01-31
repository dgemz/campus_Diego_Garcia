tareas={"Tarea1": 3, "Tarea2": 5, "Tarea3": 1, "Tarea4": 4}

tuplas = list(tareas.items())

tuplas.sort(key=lambda x: x[1], reverse=True)

for tarea in tuplas:
    print(tarea)