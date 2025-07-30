peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura em metros: "))

imc = peso/(altura**2)
if imc < 18.5:
    print("Abaixo do Peso")
elif imc < 25:
    print("Peso Normal")
elif imc < 30:
    print("Acima do Peso")
else:
    print("Obeso")