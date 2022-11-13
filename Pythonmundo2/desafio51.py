#primeiro termo e razão de uma PA
pt = int(input('Digite o valor do primeiro termo: '))
razão = int(input('Digite o valor da razão: '))
ut = pt + (10 - 1) * razão
for c in range(pt, ut + razão, razão):
    print(c, end=' ')

