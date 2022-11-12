valor1 = int(input('Digite o primeiro valor:'))
valor2 = int(input('Digite o segundo valor:'))

if valor1 > valor2:
    print(f'O Número maior entre {valor1} e {valor2} é {valor1}')
elif valor1 < valor2:
    print(f'O Número maior entre {valor1} e {valor2} é {valor2}')
elif valor1 == valor2:
    print('Não existe valor maior, os dois são iguais.')