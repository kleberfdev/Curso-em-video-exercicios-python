salario = float(input('Qual o seu salário? '))

if salario >= 1250:
    print(f'O aumento vai ser de {salario * 0.1}')
else:
    print(f'O aumento vai ser de {salario * 0.15}')