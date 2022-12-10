from random import randint
jog1 = int(input('Jogador 1 Digite seu número: '))
jog2 = int(input('Jogador 2 Digit seu número: '))
sorteio = randint(0, 1)
lista = dict([(jog1, 'Jogador 1'), (jog2, 'Jogador 2')])
if jog1 != jog2:
    print(f"Números diferentes, número sorteado é o número {sorteio}")
    if sorteio == 0:
        print(f'O jogador {min(lista.values())} Venceu')
    else:
        print(f'O jogador {max(lista.values())} Venceu')
else:
    print('Os Números São Iguais')
        