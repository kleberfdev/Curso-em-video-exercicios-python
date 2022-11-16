
idade = m18 = hm = ml = 0
while True:
    sexo = conti =  ' '
    idade = int(input('Digite a sua idade: '))
    while sexo not in 'MF':
        sexo = str(input('Digite o Sexo: [M/F] ')).upper()
    print('Cadastrado com Sucesso')
    if idade >= 18:
        m18 = m18 + 1
    if sexo == 'M':
        hm = hm + 1
    if sexo == 'F' and idade < 20:
        ml = ml + 1
    while conti not in 'SN':
        conti = str(input('Deseja continuar [S/N] ')).upper()
    if conti == 'N':
        break
print(f'{m18} tem mais de 18 anos')
print(f'{hm} homens foram cadastrados')
print(f'{ml} mulheres abaixo de 20 anos')
