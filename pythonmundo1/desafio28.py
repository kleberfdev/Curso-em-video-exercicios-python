from random import randint
from time import sleep


numero = int(input('Digite seu número de 1 a 5 e verei se você acertou: '))

sorteio = randint(0, 5)
print('Processando...')
sleep(5)
if sorteio == numero:
    print(f"O número sorteado foi {numero} Parabens Você acertou")
else:
    print(f"O número sorteado foi {sorteio} computador venceu")
