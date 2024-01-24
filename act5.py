def palindroma(palabra):
    return palabra == palabra[::-1]

palabra = input("Introduce una palabra: ")
if palindroma(palabra):
    print(f"{palabra} es una palabra palindroma.")
else:
    print(f"{palabra} no es una palabra palindroma.")