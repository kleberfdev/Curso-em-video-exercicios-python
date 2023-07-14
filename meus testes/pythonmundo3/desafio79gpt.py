lista = []
opcao = ''
while True:
    valor = int(input('Digite um valor: '))
    if valor in lista:
        print('Valor duplicado! Não vou adicionar...')
    else:
        lista.append(valor)
        print('Valor adicionado com sucesso...')
    opcao = input('Deseja continuar? [S/N] ').upper()
    while opcao not in 'SN':
        print('Digite uma opção válida:')
        opcao = input('Deseja continuar? [S/N] ').upper()
    if opcao == 'N':
        break
print(f'Você digitou os valores {sorted(lista)}')
