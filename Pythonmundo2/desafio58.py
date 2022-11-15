from random import randint
palpites = 0
sorteio = randint(0, 10)
numero = 1
while sorteio != numero:
    numero = int(input('Descubra o número entre 0 e 10 que estou pensando: '))
    palpites = palpites + 1
    if sorteio < numero:
        print(f'Menos... {palpites}° tentativa. Tente novamente: ')
    elif sorteio > numero:
        print(f'Mais... {palpites}° tentativa. Tente novamente: ') 

print(f'Você acertou depois de {palpites} vezes')