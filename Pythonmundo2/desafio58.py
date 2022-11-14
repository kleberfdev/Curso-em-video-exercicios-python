from random import randint
numero = int(input('Descubra o número entre 0 e 10 que estou pensando: '))
cont = 1
sorteio = randint(0, 10)
while sorteio != numero:
    print(sorteio)
    numero = int(input('Você errou tente novamente: '))    
    cont = cont + 1
print(f'Você acertou depois de {cont} vezes')