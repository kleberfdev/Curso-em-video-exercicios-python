lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim')
print(len(lanche))
print(lanche[1])
for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]} na posição {cont}')
for pos,comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}')
for comida in lanche:
    print(f'Eu vou comer {comida}')
print('Comi pra caramba ')
for c, b in enumerate('Kleber'):
    print(c, b)
print(sorted(lanche))
a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b
print(c)
print(c.count(9))
print(c.index(8))
print(c.index(2, 4))
pessoa = ('Kleber', 33, 'M', 99.88 )
print(pessoa)

print(pessoa)