frase=str(input("Escriba la palabra o frase para contar sus vocales y consonantes "))
vocales=0
listavo= "aeiouAEIOU"
for char in frase:
    if char in listavo:
        vocales +=1
print (f"El número de vocales es {vocales}.")