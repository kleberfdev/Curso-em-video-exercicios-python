peso = float(input('Qual é o seu peso ? (Kg)'))
altura = float(input('Qual é a sua altura ? (Metros)'))
imc = peso / (altura **2)
print (" O IMC dessa pessoa é de {:.2f}".format(imc))

if imc < 16:
    print("Abaixo do peso (Grave)!")
elif imc < 17:
    print("Abaixo do peso (Moderado)!")
elif imc < 18.5:
    print("Abaixo do peso!")
elif imc < 25:
    print("Saudável!")
elif imc < 30:
    print("Sobrepeso!")
elif imc < 35:
    print("Obesidade Grau I!")
elif imc < 40:
    print("Obesidade Grau II (severa)!")
else:
    print("Obesidade Grau III (mórbida)!")
