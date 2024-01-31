peso=int(input("Ingrese su peso en Kilogramos "))
estatura=float(input("Ingrese su altura en metros "))
imc=(peso/estatura**2)
if imc<18.5:
    print("Peso insuficiente.")
elif imc>=18.5 and imc<=24.9:
    print("Peso normal, eres saludable.")
elif imc>=25 and imc<=29.9:
    print("Estas en sobrepeso, tu riesgo es aumentado.")
elif imc>=30 and imc<=34.9:
    print("Estas en obesidad grado I, tu riesgo es moderado.")
elif imc>=35 and imc<=39.9:
    print("Estas en obesidad grado II, tu riesgo es severo.")
elif imc>=40:
    print("Estas en obesidad grado III, tu riesgo es muy severo.")