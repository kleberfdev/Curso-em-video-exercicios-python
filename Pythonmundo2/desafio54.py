from datetime import date
hoje = date.today().year
qtdmaior = 0
qtdmenor = 0
for c in range(1,7):
    nascimento = int(input(f'Digite o {c}° ano de nascimento:'))
    idade = hoje - nascimento
    if idade > 18:
        print('maior')
        qtdmaior = qtdmaior + 1
    else:
        print('menor')
        qtdmenor = qtdmenor + 1
print(f'A quantidae de pessoas que não atingiram a maioridade é {qtdmenor} e a que atigiram é {qtdmaior}')