from random import randint
c = 0
while True:
    num = int(input('Digite um valor: '))
    pi = ' '
    comp = randint(0, 10)
    while pi not in 'pi':        
        pi = str(input('Par ou Impar? [P/I] ')).lower()
    print(f'Você jogou {num} e o Computador jogou {comp}')
    if pi == 'p':
        pi = 0
    elif pi == 'i':
        pi = 1
    p = (num + comp) % 2
    if pi == p:
        print('Ganhou')
    else:
        print('perdeu')
        break
    c = c + 1
    print('Vamos jogar novamente...')
print(f'GAME OVER - Você venceu {c} vezes')