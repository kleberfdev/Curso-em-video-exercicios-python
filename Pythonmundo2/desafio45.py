from random import randint
from time import sleep
print('''Escolha uma das opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
jogada = int(input('Qual a sua jogada? '))
computador = randint(0, 2)
itens = ('Pedra', 'Papel', 'Tesoura')
if jogada >= 0 and jogada < 3:
    print('JO')
    sleep(1)
    print('KEN')
    sleep(1)
    print('PÔ')
    sleep(1)
    print(f'Você jogou {itens[jogada]} e o computador jogou {itens[computador]}')
    if jogada == 0: #PEDRA
        if computador == 0:
            print('EMPATE')
        elif computador == 1:
            print('PERDEU')
        else:
            print('VENCEU')
    elif jogada == 1: #PAPEL
        if computador == 0:
            print('VENCEU')
        elif computador == 1:
            print('EMPATE')
        else:
            print('PERDEU')
    elif jogada == 2: #TESOURA
        if computador == 0:
            print('PERDEU')
        elif computador == 1:
            print('VENCEU')
        else:
            print('EMPATE')
else:
    print('JOGADA INVÁLIDA')