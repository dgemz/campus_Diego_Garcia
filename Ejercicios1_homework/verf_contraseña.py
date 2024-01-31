print("La contraseña debe tener 8 caracteres, mínimo una mayúscula y una minúscula, y un número.")
contraseña = input("¿Cuál es la contraseña? ")

mayus = any(c.isupper() for c in contraseña)
minus = any(c.islower() for c in contraseña)

if len(contraseña) == 8:
    if contraseña.isalnum():
        if mayus and minus:
            print("Contraseña válida.")
        else:
            print("La contraseña debe contener al menos una mayúscula y una minúscula.")
    else:
        print("La contraseña solo puede contener números y caracteres.")
else:
    print("Contraseña no válida debe tener mas de 8 caracteres.")