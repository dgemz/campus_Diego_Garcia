numprod=int(input("Escriba el número de productos va a llevar. "))
total=numprod*18
if numprod<36:
    prom=numprod*0.1
    descuento=numprod-prom
elif numprod>=36:
    prom=numprod*0.15
    descuento=numprod-prom
regalo=0

if numprod>=48:
  
    docenas=numprod/12
    regalo=docenas-3


print(f"El monto final de su compra es {total} pero se le aplico un descuento el cual fue de ${prom}, por lo tanto su monto a pagar es de {descuento}, y se le regala {regalo} unidad del producto.")