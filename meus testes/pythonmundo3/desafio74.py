from random import randint
numeros = tuple(randint(0, 100) for c in range(5))
for c in numeros:
    print(c, end=' ')
print(f'\nO menor valor da Tupla é {min(numeros)}')
print(f'O Maior número da Tupla é {max(numeros)}')