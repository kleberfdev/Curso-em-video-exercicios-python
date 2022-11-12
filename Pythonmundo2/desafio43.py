peso = float(input('Digite seu peso '))
altura = float(input('Digite sua altura '))
imc = peso / (altura **2)
print(f'Seu IMC é {imc:.2f} Você está ', end = '')
if imc < 18.5:
    print('abaixo do peso')
elif imc < 25:
    print('com o peso ideal')
elif imc < 30:
    print('com sobrepeso')
elif imc < 40:
    print('com obesidade')
else:
    print('obesidade mórbida')
