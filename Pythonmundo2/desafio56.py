somaidade = 0
médiaidade = 0
maioridadehomem = 0
nomevelho = ''
totmulher20 = 0
for c in range(1, 5):
    print(f'{c}° Pessoa')
    nome = str(input('Digite o {c}° nome: '))
    idade = int(input('Digite a {c}° idade '))
    sexo = str(input('Qual o sexo do {c}°: "M" ou "F": '))
    somaidade = somaidade + idade
    if c == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        totmulher20 = totmulher20 + 1

médiaidade = somaidade / 4
print(f'A média de idade do grupo é de {médiaidade}')
print(f'A maior idade do homem mais é de {maioridadehomem} e se chama {nomevelho}')
print(f'Ao todo tem {totmulher20} mulheres abaixo de 20 anos')