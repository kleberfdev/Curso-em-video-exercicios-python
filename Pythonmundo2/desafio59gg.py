from time import sleep
vlr1 = int(input('Digite o primeiro Valor: '))
vlr2 = int(input('Digite o segundo Valor: '))
c = 0
res = 0
while c != 5:
    print('''Digite uma das opções:
    [1] Somar
    [2] Multiplicar
    [3] Maior
    [4] novos números
    [5] Sair do programa''')
    c = int(input('Digite a opção: '))

    if c == 1:
        res = vlr1 + vlr2
        print(f'A soma é de {res}')
    elif c == 2:
        res = vlr1 * vlr2
        print(f'A multiplicação é de {res}')
    elif c == 3:
        res = max(vlr1, vlr2)
        print(f'O maior valor é {res}')
    elif c == 4:
        print('Vamos recomeçar')
        print('Aguarde') 
        sleep(2) 
        vlr1 = int(input('Digite o primeiro Valor: '))
        vlr2 = int(input('Digite o segundo Valor: '))  
    if c == 5:
        print('Programa encerrado')
    else:
        print("-"*20)
        sleep(2)
