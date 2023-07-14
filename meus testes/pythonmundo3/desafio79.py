lista = []
opcao = ''
while True:
    valor = int(input('Digite um valor: '))
    if lista.count(valor) != 0:
        print('Valor duplicado! Não vou adicionar...')
    else:
        lista.append(valor)
        print('Valor adicionado com sucesso...')
    while opcao == '' or opcao == 'S':
        opcao = input('Deseja continuar? [S/N] ').upper()
        if opcao not in 'SN':
            print('Digite uma opção válida:')
            opcao = ''
        else:
            break        
    if opcao == 'N'  :
        break  
print(f'você digitou os valores {sorted(lista)}')