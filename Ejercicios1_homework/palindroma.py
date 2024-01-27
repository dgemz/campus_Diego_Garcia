def palindroma(frase):
    quitespa = frase.replace(" ", "").lower()
    return quitespa == quitespa[::-1]

frase = input("Introduce una palabra o frase: ")
if palindroma(frase):
    print(f"'{frase}' es una palabra o frase palíndroma.")
else:
    print(f"'{frase}' no es una palabra o frase palíndroma.")